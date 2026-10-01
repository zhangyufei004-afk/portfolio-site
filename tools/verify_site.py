r"""Verify the built site: every local link/image must resolve, and nothing may hit the network.

Checks src / href / poster attributes. The leading (?<![-\w]) guard is required so that
"src" inside "<source ...>" is matched (a plain word boundary fails there because "e"
is a word character).
"""
import os, re, sys

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(SITE, "dist")
ATTR = re.compile(r'(?<![-\w])(src|href|poster)\s*=\s*"([^"]+)"', re.I)

problems = []
pages = 0
checked = 0
external = []

for root, _, files in os.walk(DIST):
    for fn in files:
        if not fn.endswith(".html"):
            continue
        pages += 1
        path = os.path.join(root, fn)
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
        rel_page = os.path.relpath(path, DIST)
        for attr, url in ATTR.findall(html):
            u = url.strip()
            if u.startswith(("http://", "https://", "//", "data:", "mailto:", "#", "javascript:")):
                if u.startswith(("http://", "https://", "//")):
                    external.append((rel_page, u))
                continue
            checked += 1
            target = u.split("#")[0].split("?")[0]
            if not target:
                continue
            resolved = os.path.normpath(os.path.join(root, target))
            if target.endswith("/"):
                resolved = os.path.join(resolved, "index.html")
            if not os.path.exists(resolved):
                problems.append("%s -> %s" % (rel_page, u))

print("HTML pages:      %d" % pages)
print("local links:     %d checked" % checked)
print("external refs:   %d" % len(external))
for p, u in external[:20]:
    print("   ! external in %s: %s" % (p, u))
print("broken links:    %d" % len(problems))
for p in problems[:40]:
    print("   x %s" % p)

# report dist size
total = 0
by_dir = {}
for root, _, files in os.walk(DIST):
    for fn in files:
        p = os.path.join(root, fn)
        sz = os.path.getsize(p)
        total += sz
        top = os.path.relpath(p, DIST).split(os.sep)[0]
        by_dir[top] = by_dir.get(top, 0) + sz
print("\ndist total:      %.1f MB" % (total / 1048576))
for k in sorted(by_dir, key=lambda k: -by_dir[k]):
    print("   %-14s %.2f MB" % (k, by_dir[k] / 1048576))

sys.exit(1 if (problems or external) else 0)
