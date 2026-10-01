"""Content consistency linter for the portfolio.

Catches the class of mistake the link checkers cannot: a page that contradicts
itself or still carries a placeholder. This is what let "代码已开源" survive after
the GitHub link was removed for being private.
"""
import os
import re

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ = os.path.join(SITE, "content", "projects")
PAGES = [os.path.join(SITE, "content", "index.md"), os.path.join(SITE, "content", "about.md")]

issues = []


def check(path, text, is_project=True):
    name = os.path.basename(path)

    # 1. claims of open source must be backed by a live GitHub link on the page
    if re.search(r"已开源|开源地址|open[- ]?source", text):
        if "github.com" not in text:
            issues.append((name, "claims to be open source but has no GitHub link"))

    # 2. a page saying the repo is private must not also offer a repo link
    if re.search(r"仓库.*私有|私有仓库|目前是私有", text) and "github.com/zhangyufei004-afk" in text:
        issues.append((name, "says the repo is private but still links the account's GitHub"))

    # 3. placeholder leftovers. "占位符/占位资产" is normal game-dev vocabulary, so
    #    only flag 占位 when it describes the website's own content.
    for pat, msg in [
        (r"占位封面|占位图(?!标|层)", "'占位封面/占位图' still present"),
        (r"待补充|待替换", "'待补充/待替换' callout still present (confirm it is intentional)"),
        (r"lorem ipsum", "placeholder copy"),
        (r"example\.com", "example.com placeholder link"),
    ]:
        if re.search(pat, text, re.I):
            issues.append((name, msg))

    # 4. front matter sanity (project pages only)
    head = text.split("---")[1] if text.startswith("---") else ""
    if is_project:
        for field in ("title", "summary", "year", "type", "role", "slug"):
            if not re.search(r"^%s:\s*\S" % field, head, re.M):
                issues.append((name, "front matter missing field: %s" % field))
    if head:
        for field in ("cover", "thumb"):
            m = re.search(r"^%s:\s*(\S+)" % field, head, re.M)
            if m and not os.path.exists(os.path.join(SITE, m.group(1))):
                issues.append((name, "%s points at a missing file: %s" % (field, m.group(1))))

    # 5. every image referenced must exist
    for src in re.findall(r'src="(assets/[^"]+)"', text):
        if not os.path.exists(os.path.join(SITE, src)):
            issues.append((name, "missing image: %s" % src))

    # 6. section ids must be unique within the file
    ids = re.findall(r'<section[^>]*\bid="([^"]+)"', text)
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        issues.append((name, "duplicate section id: %s" % ", ".join(sorted(dupes))))

    # 7. unbalanced tags
    for tag in ("div", "section", "figure", "table"):
        o = len(re.findall(r"<%s\b" % tag, text))
        c = len(re.findall(r"</%s>" % tag, text))
        if o != c:
            issues.append((name, "<%s> unbalanced: %d open / %d close" % (tag, o, c)))


for path in PAGES:
    with open(path, encoding="utf-8") as fh:
        check(path, fh.read(), is_project=False)
for f in sorted(os.listdir(PROJ)):
    if f.endswith(".md"):
        p = os.path.join(PROJ, f)
        with open(p, encoding="utf-8") as fh:
            check(p, fh.read(), is_project=True)

if issues:
    print("content issues: %d\n" % len(issues))
    for name, msg in issues:
        print("  %-20s %s" % (name, msg))
else:
    print("no content issues found")

raise SystemExit(1 if issues else 0)
