"""Check every external link on the built site actually resolves.

The link checker only validated local paths, which is how three 404 GitHub links
went unnoticed. This closes that gap.
"""
import os
import re
import time
import urllib.error
import urllib.request

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(SITE, "dist")
ATTR = re.compile(r'(?<![-\w])(?:src|href)\s*=\s*"(https?://[^"]+)"', re.I)

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
}

found = {}
for root, _, files in os.walk(DIST):
    for fn in files:
        if not fn.endswith(".html"):
            continue
        path = os.path.join(root, fn)
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
        for url in ATTR.findall(html):
            found.setdefault(url, set()).add(os.path.relpath(path, DIST))

print("external links on site: %d\n" % len(found))

bad = []
unknown = []
for url in sorted(found):
    where = ", ".join(sorted(found[url])[:2])

    def probe(method):
        req = urllib.request.Request(url, headers=HEADERS, method=method)
        with urllib.request.urlopen(req, timeout=25) as resp:
            return resp.status

    status, note = None, ""
    try:
        status = probe("HEAD")
    except urllib.error.HTTPError as e:
        status = e.code
    except Exception as e:
        note = str(e)[:50]

    # Many servers (Steam, some CDNs) reject HEAD with 404/403 while serving GET
    # fine, so any non-2xx from HEAD must be confirmed with a real GET.
    if status is None or status >= 400:
        get_status = None
        for attempt in range(3):
            try:
                get_status = probe("GET")
                break
            except urllib.error.HTTPError as e:
                get_status = e.code
                if e.code == 429:          # rate limited: back off and retry
                    time.sleep(4 * (attempt + 1))
                    continue
                break
            except Exception as e:
                note = (note + " " if note else "") + "GET failed: %s" % str(e)[:40]
                time.sleep(2)
        note = (note + " " if note else "") + "HEAD=%s, GET=%s" % (status, get_status)
        status = get_status

    ok = status is not None and status < 400
    rate_limited = status == 429
    if not ok and not rate_limited:
        bad.append((url, status, note, where))
    elif rate_limited:
        unknown.append((url, note, where))
    print("  %-6s %-4s %s" % ("OK" if ok else ("??" if rate_limited else "BAD"),
                              status if status else "-", url))
    if note:
        print("          %s  |  used in %s" % (note, where))

print("\nbroken external links: %d" % len(bad))
for url, status, note, where in bad:
    print("  ! %s -> %s  (%s)" % (url, status, where))
if unknown:
    print("\nunverified (rate limited, could not confirm): %d" % len(unknown))
    for url, note, where in unknown:
        print("  ? %s  (%s)" % (url, where))
raise SystemExit(1 if bad else 0)
