"""Deeper live-site verification: real content, video seeking, responsive layout.

Fixes an earlier bug: reading only a few hundred bytes truncated the HTML so
content assertions falsely failed.
"""
import base64
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from measure_layout import WS, CHROME           # reuse the minimal CDP client

BASE = (sys.argv[1] if len(sys.argv) > 1
        else "https://portfolio-site.zhangyufei004.workers.dev").rstrip("/")
HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"),
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}
SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(SITE, ".cache-live-check")
SHOTS = os.path.join(WORK, "live-shots")
os.makedirs(SHOTS, exist_ok=True)


def fetch(url, rng=None):
    h = dict(HEADERS)
    if rng:
        h["Range"] = rng
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.status, r.headers, r.read()


print("=== 1. 首页内容（完整下载）===")
status, headers, body = fetch(BASE + "/")
html = body.decode("utf-8", "replace")
print("  HTTP %s  下载 %d bytes" % (status, len(html)))
checks = [
    ("张宇飞", "作者名"),
    ("游戏与关卡设计作品集", "站点标题"),
    ("projects/echos/", "ECHOES 链接"),
    ("projects/stormhaven/", "Stormhaven 链接（首页精选三张卡片之一）"),
    ("2485357205@qq.com", "邮箱"),
    ("batcat_773", "Discord"),
    ("assets/css/site.css", "样式引用"),
    ("assets/js/site.js", "脚本引用"),
]
missing = []
for needle, what in checks:
    hit = needle in html
    if not hit:
        missing.append(what)
    print("  %-5s %s" % ("FOUND" if hit else "MISSING", what))

print("\n=== 2. 视频能否拖动进度条（HTTP Range）===")
try:
    st, hd, chunk = fetch(BASE + "/assets/media/bounty-hunter/trailer.mp4", "bytes=1000000-1000999")
    cr = hd.get("Content-Range", "(无)")
    print("  HTTP %s   %s" % (st, cr))
    print("  取到 %d 字节" % len(chunk))
    if st == 206 and chunk:
        print("  结果: 支持 Range，可以拖进度条")
    else:
        print("  结果: 不支持 Range（返回 %s 全量 %d 字节）" % (st, len(chunk)))
        print("        已知限制: Cloudflare Workers 静态资源不支持 Range；")
        print("        表现为拖进度条会重新从头加载。预告片仅 3.6MB，影响有限。")
except Exception as e:
    print("  失败: %s" % e)

print("\n=== 3. 两个 PDF 能否下载（这份是给招聘方的）===")
for path, label in [("/assets/docs/zhang-yufei-resume.pdf", "简历"),
                    ("/assets/docs/zhang-yufei-design-portfolio.pdf", "作品集")]:
    try:
        st, hd, data = fetch(BASE + path)
        ctype = hd.get("Content-Type", "?")
        magic = data[:5]
        ok = magic.startswith(b"%PDF")
        print("  %-6s %-8s HTTP %s  %6.0f KB  %s  %s" % (
            "OK" if ok else "BAD", label, st, len(data) / 1024, ctype,
            "PDF 文件头正确" if ok else "文件头异常"))
    except Exception as e:
        print("  BAD    %-8s %s" % (label, e))

print("\n=== 4. 线上响应式（真浏览器，3 个断点）===")
if CHROME is None:
    print("  未找到 Chrome/Edge，跳过")
else:
    PORT = 10021
    prof = os.path.join(WORK, "live-chromeprofile")
    proc = subprocess.Popen(
        [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
         "--no-first-run", "--disable-crash-reporter", "--remote-debugging-port=%d" % PORT,
         "--user-data-dir=" + prof, "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
    try:
        ws_url = None
        for _ in range(60):
            time.sleep(0.5)
            try:
                ws_url = json.load(urllib.request.urlopen(
                    "http://127.0.0.1:%d/json/version" % PORT, timeout=2))["webSocketDebuggerUrl"]
                break
            except Exception:
                continue
        ws = WS(ws_url)
        counter = [0]

        def send(method, params=None, session=None):
            counter[0] += 1
            mid = counter[0]
            msg = {"id": mid, "method": method, "params": params or {}}
            if session:
                msg["sessionId"] = session
            ws.send(json.dumps(msg))
            while True:
                obj = json.loads(ws.recv())
                if obj.get("id") == mid:
                    return obj

        tid = send("Target.createTarget", {"url": "about:blank"})["result"]["targetId"]
        sid = send("Target.attachToTarget", {"targetId": tid, "flatten": True})["result"]["sessionId"]
        send("Page.enable", session=sid)

        jobs = [("live-mobile", "/", 390, 1500, None),
                ("live-tablet", "/", 820, 1300, None),
                ("live-desktop", "/projects/echos/", 1440, 1300, None),
                ("live-video", "/projects/bounty-hunter/", 1280, 900, "video")]
        for name, path, w, h, anchor in jobs:
            send("Emulation.setDeviceMetricsOverride",
                 {"width": w, "height": h, "deviceScaleFactor": 1, "mobile": w < 700}, session=sid)
            send("Page.navigate", {"url": BASE + path}, session=sid)
            time.sleep(3.5)
            if anchor:
                send("Runtime.evaluate",
                     {"expression": "document.querySelector('%s') && document.querySelector('%s').scrollIntoView({block:'center'})" % (anchor, anchor)},
                     session=sid)
                time.sleep(1.5)
            res = send("Runtime.evaluate", {
                "expression": "JSON.stringify({sw:document.documentElement.scrollWidth,vw:window.innerWidth,title:document.title})",
                "returnByValue": True}, session=sid)
            val = res.get("result", {}).get("result", {}).get("value")
            info = json.loads(val) if val else {}
            over = info.get("sw", 0) > info.get("vw", 0) + 1
            print("  %-6s %-16s %dx%d   scrollWidth=%s   %s" % (
                "溢出" if over else "OK", name, w, h, info.get("sw"), info.get("title", "")[:34]))
            shot = send("Page.captureScreenshot", {"format": "png"}, session=sid)
            d = shot.get("result", {}).get("data")
            if d:
                fp = os.path.join(SHOTS, name + ".png")
                with open(fp, "wb") as fh:
                    fh.write(base64.b64decode(d))
        ws.close()
    finally:
        proc.terminate()

print("\n=== 结果 ===")
print("  首页内容缺失项: %d %s" % (len(missing), missing if missing else ""))
print("  截图目录: %s" % SHOTS)
