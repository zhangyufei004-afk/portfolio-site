"""Verify a resume PDF fits one page by rendering it, not by guessing coordinates.

Earlier attempts compared a value parsed out of the PDF content stream against the
page height; that only worked by coincidence and led to over-trimming. The
authoritative check is visual: screenshot the HTML at exact A4 pixel size and find
the last row containing non-white pixels.
"""
import os
import subprocess
import sys
import time

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
A4_W_PX, A4_H_PX = 794, 1123          # A4 at 96 dpi


def last_content_row(html_path, out_png):
    if os.path.exists(out_png):
        os.remove(out_png)
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
                    "--hide-scrollbars", "--window-size=%d,%d" % (A4_W_PX, A4_H_PX),
                    "--screenshot=" + out_png, "file:///" + html_path.replace("\\", "/")],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    time.sleep(1.5)
    try:
        from PIL import Image
    except ImportError:
        return None, None
    im = Image.open(out_png).convert("L")
    w, h = im.size
    px = im.load()
    last = 0
    for y in range(h):
        if min(px[x, y] for x in range(0, w, 4)) < 240:
            last = y
    return h, last


if __name__ == "__main__":
    html = sys.argv[1] if len(sys.argv) > 1 else \
        r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\site\简历-设计版.html"
    png = os.path.join(os.path.dirname(html), "_fitcheck.png")
    h, last = last_content_row(html, png)
    if h is None:
        print("需要 Pillow 才能检查")
        sys.exit(2)
    print("A4 画布高度 : %d px" % h)
    print("内容最底行 : %d px" % last)
    print("底部空白   : %d px  (%.0f%%)" % (h - last, (h - last) / h * 100))
    if last < h:
        print("结论       : 一页装得下，富余 %d px" % (h - last))
    else:
        print("结论       : 内容贴到页面底边或被裁切，需要减少内容")
