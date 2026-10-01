#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zero-dependency static site builder for the personal portfolio.

Usage (from anywhere):
    python build.py

Reads:
    site.config.json          site-wide settings
    content/*.md              standalone pages (home / about / works overrides)
    content/projects/*.md     one file per project (front matter + sections)
    assets/                   css, js, images (copied verbatim)
Writes:
    dist/                     self-contained static site
      - every internal link is RELATIVE, so it works from any URL prefix,
        from a subfolder, or straight off the filesystem (file://)
      - no external requests at all (no CDN, no web fonts, no analytics)
"""

from __future__ import annotations

import html
import json
import os
import re
import shutil
import sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
PROJECTS = os.path.join(CONTENT, "projects")
ASSETS = os.path.join(ROOT, "assets")
MEDIA = os.path.join(ASSETS, "media")
TEMPLATES = os.path.join(ROOT, "templates")
DIST = os.path.join(ROOT, "dist")

NAV = [
    ("index.html", "首页"),
    ("works.html", "作品"),
    ("about.html", "关于"),
]


# --------------------------------------------------------------------------
# tiny template engine:  {{name}} / {{name.attr}} placeholders
# --------------------------------------------------------------------------
def render(template: str, context: dict) -> str:
    def sub(match: re.Match) -> str:
        expr = match.group(1).strip()
        parts = expr.split(".")
        value = context
        for part in parts:
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return ""
        if value is None:
            return ""
        return str(value)

    out = re.sub(r"\{\{\s*([A-Za-z0-9_.]+)\s*\}\}", sub, template)
    return out


def load_template(name: str) -> str:
    with open(os.path.join(TEMPLATES, name), encoding="utf-8") as fh:
        return fh.read()


# --------------------------------------------------------------------------
# front matter:  --- key: value ---  (values are plain strings or JSON lists)
# --------------------------------------------------------------------------
def parse_front_matter(text: str):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip("\n")
    body = text[end + 4 :].lstrip("\n")
    meta = {}
    for line in raw.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            try:
                meta[key] = json.loads(value)
            except json.JSONDecodeError:
                meta[key] = [v.strip().strip('"') for v in value[1:-1].split(",") if v.strip()]
        elif value.startswith('"') and value.endswith('"'):
            meta[key] = value[1:-1]
        else:
            meta[key] = value
    return meta, body


# --------------------------------------------------------------------------
# section splitting:  <section id="x" title="Y" kicker="Z"> ... </section>
# --------------------------------------------------------------------------
SECTION_RE = re.compile(r'<section\s+([^>]*?)>(.*?)</section>', re.S | re.I)
ATTR_RE = re.compile(r'(\w[\w-]*)\s*=\s*"([^"]*)"')


def parse_sections(body: str):
    sections = []
    for attrs_raw, inner in SECTION_RE.findall(body):
        attrs = dict(ATTR_RE.findall(attrs_raw))
        sections.append(
            {
                "id": attrs.get("id", ""),
                "title": attrs.get("title", ""),
                "kicker": attrs.get("kicker", ""),
                "body": inner.strip(),
            }
        )
    return sections


LOCAL_ATTR = re.compile(r'(?<![-\w])(src|href|poster)\s*=\s*"([^"]+)"', re.I)


def apply_prefix(markup: str, prefix: str) -> str:
    r"""Rewrite page-relative asset/link paths so they work at any nesting depth.

    Content files always write paths as if from the site root ("assets/...",
    "works.html"); this adds the right number of "../" for the output location.
    Handles src, href and poster; absolute URLs, anchors and mailto are untouched.
    Note the (?<![-\w]) guard: a plain word boundary would not match "src" inside
    "<source" because "e" is a word character, which silently skipped <source> tags.
    """
    if not prefix:
        return markup

    def repl(match: re.Match) -> str:
        attr, url = match.group(1), match.group(2)
        low = url.lower()
        if low.startswith(("http://", "https://", "//", "data:", "mailto:", "#", "javascript:")):
            return match.group(0)
        if url.startswith("../") or url.startswith("./"):
            return match.group(0)
        return '%s="%s%s"' % (attr, prefix, url)

    return LOCAL_ATTR.sub(repl, markup)


def slugify_anchors(body: str, seen: set) -> str:
    """Give every <h3> inside a section a unique id so the TOC can link to it."""

    def repl(match: re.Match) -> str:
        tag, attrs, text = match.group(1), match.group(2), match.group(3)
        existing = ATTR_RE.search(attrs)
        if existing and existing.group(1) == "id":
            return match.group(0)
        base = re.sub(r"<[^>]+>", "", text)
        base = re.sub(r"\s+", "-", base.strip())
        base = re.sub(r"[^\w\u4e00-\u9fff-]", "", base) or "h"
        anchor, n = base, 2
        while anchor in seen:
            anchor, n = "%s-%d" % (base, n), n + 1
        seen.add(anchor)
        return '<%s%s id="%s">%s</%s>' % (tag, attrs, anchor, text, tag)

    return re.sub(r"<(h3)([^>]*)>(.*?)</h3>", repl, body, flags=re.S | re.I)


# --------------------------------------------------------------------------
# page assembly
# --------------------------------------------------------------------------
BASE_CTX = {}


def build_page(page_title: str, body_html: str, *, depth: int = 0, body_class: str = "", description: str = "") -> str:
    """Wrap a page body in the shared shell (topbar + footer).

    depth = how many folders below dist/ the output file sits; it decides how
    many "../" the shared shell's own asset/nav links need.
    """
    prefix = "../" * depth
    nav_html = "\n".join(
        '        <a href="{p}{href}">{label}</a>'.format(p=prefix, href=href, label=label)
        for href, label in NAV
    )
    ctx = dict(BASE_CTX)
    ctx.update(
        {
            "page_title": page_title,
            "nav": nav_html,
            "prefix": prefix,
            "content": body_html,
            "body_class": body_class,
            "meta_description": description or BASE_CTX.get("description", ""),
            "year": str(date.today().year),
            "asset": prefix + "assets",
            "home": prefix + "index.html",
        }
    )
    return render(load_template("base.html"), ctx)


def write(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("  wrote %s" % os.path.relpath(path, ROOT))


# --------------------------------------------------------------------------
# project pages
# --------------------------------------------------------------------------
def project_toc(sections) -> str:
    items = []
    for sec in sections:
        if not sec["id"]:
            continue
        items.append(
            '        <li><a href="#{i}">{t}</a></li>'.format(i=sec["id"], t=html.escape(sec["title"]))
        )
    if not items:
        return ""
    return (
        '  <nav class="toc" aria-label="本页目录">\n'
        '    <p class="toc__title">本页目录</p>\n'
        '    <ol class="toc__list">\n' + "\n".join(items) + "\n    </ol>\n  </nav>\n"
    )


def render_project(meta: dict, body: str) -> str:
    sections = parse_sections(body)
    seen: set = set()
    rendered = []
    for sec in sections:
        inner = slugify_anchors(sec["body"], seen)
        inner = apply_prefix(inner, BASE_CTX.get("prefix", ""))
        kicker = (
            '<p class="section__kicker">%s</p>' % html.escape(sec["kicker"])
            if sec.get("kicker")
            else ""
        )
        rendered.append(
            '<section class="section" id="{i}">\n'
            '  <header class="section__head">{k}<h2 class="section__title">{t}</h2></header>\n'
            '  <div class="section__body">\n{b}\n  </div>\n'
            "</section>".format(
                i=html.escape(sec["id"]),
                k=kicker,
                t=html.escape(sec["title"]),
                b=inner,
            )
        )

    facts = []
    for key, label in (
        ("role", "担任"),
        ("team", "团队"),
        ("duration", "周期"),
        ("engine", "引擎 / 工具"),
        ("type", "类型"),
        ("status", "状态"),
    ):
        if meta.get(key):
            facts.append(
                '<div class="fact"><dt>%s</dt><dd>%s</dd></div>' % (label, html.escape(meta[key]))
            )

    tags = "".join(
        '<span class="tag">%s</span>' % html.escape(t) for t in meta.get("tags", [])
    )

    cover = ""
    if meta.get("cover"):
        cover = (
            '\n  <figure class="hero__cover">\n'
            '    <img src="%s%s" alt="%s 封面" loading="lazy" decoding="async">\n'
            "  </figure>" % (BASE_CTX["prefix"], meta["cover"], html.escape(meta["title"]))
        )

    ctx = dict(BASE_CTX)
    ctx.update(
        {
            "prefix": BASE_CTX["prefix"],
            "asset": BASE_CTX["prefix"] + "assets",
            "home": BASE_CTX["prefix"] + "index.html",
            "year": str(date.today().year),
            "project": {
                "title": html.escape(meta["title"]),
                "subtitle": html.escape(meta.get("subtitle", "")),
                "summary": meta.get("summary", ""),
                "year": html.escape(meta.get("year", "")),
                "facts": "\n".join(facts),
                "tags": tags,
                "cover": cover,
                "toc": project_toc(sections),
                "sections": "\n".join(rendered),
                "accent": meta.get("accent", "#5ee0d0"),
                "backlink": BASE_CTX["prefix"] + "works.html",
            },
        }
    )
    return render(load_template("project.html"), ctx)


def project_card(meta: dict, href: str) -> str:
    thumb = meta.get("thumb") or meta.get("cover") or ""
    img = (
        '<img src="%s%s" alt="%s 缩略图" loading="lazy" decoding="async">'
        % (BASE_CTX["prefix"], thumb, html.escape(meta["title"]))
        if thumb
        else '<div class="card__thumb-fallback" aria-hidden="true"></div>'
    )
    tags = "".join('<span class="tag tag--sm">%s</span>' % html.escape(t) for t in meta.get("tags", [])[:4])
    return (
        '<a class="card" href="{href}">\n'
        '  <div class="card__thumb">{img}</div>\n'
        '  <div class="card__body">\n'
        '    <p class="card__meta">{year} · {type}</p>\n'
        '    <h3 class="card__title">{title}</h3>\n'
        '    <p class="card__summary">{summary}</p>\n'
        '    <div class="card__tags">{tags}</div>\n'
        "  </div>\n"
        "</a>".format(
            href=href,
            img=img,
            year=html.escape(meta.get("year", "")),
            type=html.escape(meta.get("type", "")),
            title=html.escape(meta["title"]),
            summary=html.escape(meta.get("summary", "")),
            tags=tags,
        )
    )


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def clean_dist() -> None:
    """Remove dist/, tolerating files that another program has open.

    On Windows a PDF or video left open in a viewer/browser holds a lock, and
    shutil.rmtree then raises PermissionError mid-walk. That used to abort the
    build and leave dist/ half-deleted, so instead we report the locked file,
    keep it, and carry on -- the next build overwrites it anyway.
    """
    if not os.path.isdir(DIST):
        return
    locked = []

    def on_error(func, path, exc_info):
        locked.append(path)

    shutil.rmtree(DIST, onerror=on_error)
    # rmtree reports the directories it could not descend into as well; only the
    # actual files are interesting to a human reading the output.
    locked = [p for p in locked if os.path.isfile(p)]
    if locked:
        print("  ! %d file(s) were locked and kept (close any open viewer):" % len(locked))
        for p in locked:
            print("      %s" % os.path.relpath(p, ROOT))
    os.makedirs(DIST, exist_ok=True)


def copy_assets() -> None:
    """Copy assets/ into dist/assets/, skipping files held open elsewhere."""
    src, dst = ASSETS, os.path.join(DIST, "assets")
    if not os.path.isdir(src):
        return
    skipped = []
    for root, _, files in os.walk(src):
        rel = os.path.relpath(root, src)
        out_dir = dst if rel == "." else os.path.join(dst, rel)
        os.makedirs(out_dir, exist_ok=True)
        for fn in files:
            s, d = os.path.join(root, fn), os.path.join(out_dir, fn)
            try:
                shutil.copy2(s, d)
            except PermissionError:
                if os.path.exists(d):
                    skipped.append(d)
                else:
                    raise
    print("  copied assets/ -> dist/assets/")
    if skipped:
        print("  ! %d asset(s) kept from the previous build (locked):" % len(skipped))
        for p in skipped:
            print("      %s" % os.path.relpath(p, ROOT))


def main() -> int:
    with open(os.path.join(ROOT, "site.config.json"), encoding="utf-8") as fh:
        config = json.load(fh)

    clean_dist()

    # assets are copied verbatim; no processing, no network, no hashing
    copy_assets()

    # report media weight so a bloated video folder is noticed immediately
    if os.path.isdir(MEDIA):
        total = 0
        for dirpath, _, files in os.walk(MEDIA):
            for fn in files:
                total += os.path.getsize(os.path.join(dirpath, fn))
        print("  media/: %d file(s), %.1f MB" % (
            sum(len(f) for _, _, f in os.walk(MEDIA)), total / 1048576))

    BASE_CTX.update(config)
    BASE_CTX["prefix"] = ""
    BASE_CTX["asset"] = "assets"
    BASE_CTX["home"] = "index.html"

    # ---- projects -------------------------------------------------------
    project_metas = []
    if os.path.isdir(PROJECTS):
        for fn in sorted(os.listdir(PROJECTS)):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            with open(os.path.join(PROJECTS, fn), encoding="utf-8") as fh:
                meta, body = parse_front_matter(fh.read())
            slug = meta.get("slug") or os.path.splitext(fn)[0]
            meta["slug"] = slug
            meta.setdefault("title", slug)
            meta.setdefault("summary", "")
            order = int(meta.get("order", 999))
            project_metas.append((order, slug, meta, body))

    project_metas.sort(key=lambda row: (row[0], row[1]))

    for _, slug, meta, body in project_metas:
        out = os.path.join(DIST, "projects", slug, "index.html")
        # project pages live at dist/projects/<slug>/index.html -> two levels below dist/
        saved = BASE_CTX["prefix"]
        BASE_CTX["prefix"] = "../../"
        try:
            article = render_project(meta, body)
        finally:
            BASE_CTX["prefix"] = saved
        write(
            out,
            build_page(
                "%s · %s" % (meta["title"], config["short_name"]),
                article,
                depth=2,
                body_class="page-project",
                description=meta.get("summary", ""),
            ),
        )

    # ---- works index ----------------------------------------------------
    saved = BASE_CTX["prefix"]
    BASE_CTX["prefix"] = ""
    try:
        cards = "\n".join(
            project_card(meta, "projects/%s/" % slug) for _, slug, meta, _ in project_metas
        )
    finally:
        BASE_CTX["prefix"] = saved
    works_body = (
        '<section class="section"><div class="grid grid--cards">\n' + cards + "\n</div></section>"
    )

    # ---- standalone content pages ---------------------------------------
    standalone = {}
    if os.path.isdir(CONTENT):
        for fn in sorted(os.listdir(CONTENT)):
            if fn.endswith(".md"):
                with open(os.path.join(CONTENT, fn), encoding="utf-8") as fh:
                    meta, body = parse_front_matter(fh.read())
                standalone[os.path.splitext(fn)[0]] = (meta, body)

    for key, out_name, title in (
        ("index", "index.html", config["name"]),
        ("about", "about.html", "关于 · " + config["short_name"]),
        ("works", "works.html", "作品 · " + config["short_name"]),
    ):
        if key == "works":
            meta = {"title": title}
            body = works_body
        elif key in standalone:
            meta, body = standalone[key]
            title = meta.get("title", title)
        else:
            continue
        saved = BASE_CTX["prefix"]
        BASE_CTX["prefix"] = ""
        try:
            hero = ""
            if meta.get("hero_title"):
                hero = (
                    '<header class="hero">\n  <div class="wrap">\n'
                    '    <p class="hero__eyebrow">%s</p>\n'
                    '    <h1 class="hero__title">%s</h1>\n'
                    '    <p class="hero__lead">%s</p>\n'
                    "  </div>\n</header>"
                    % (
                        html.escape(meta.get("hero_kicker", config["tagline"])),
                        html.escape(meta["hero_title"]),
                        meta.get("hero_sub", ""),
                    )
                )
            inner = render(load_template("page.html"), {"hero": hero, "content": body})
        finally:
            BASE_CTX["prefix"] = saved

        write(
            os.path.join(DIST, out_name),
            build_page(
                title,
                inner,
                depth=0,
                body_class=meta.get("body_class", "page-" + key),
                description=meta.get("description", config.get("description", "")),
            ),
        )

    # ---- deployment helpers --------------------------------------------
    write(os.path.join(DIST, ".nojekyll"), "")
    write(
        os.path.join(DIST, "robots.txt"),
        "User-agent: *\nAllow: /\n",
    )
    print("\n  build complete -> %s" % DIST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
