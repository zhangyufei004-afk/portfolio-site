"""Locate the Unity Game view by brightness profile rather than colour saturation.

The editor chrome is uniformly dark; the game view is much brighter. Scanning a
row/column profile and taking the widest run above a brightness threshold is
stable across frames.
"""
import os
import subprocess
from PIL import Image

FFMPEG = None
for root, _, files in os.walk(r"C:\Users\fyhy2\AppData\Local\Microsoft\WinGet\Packages"):
    if "ffmpeg.exe" in files and "Gyan.FFmpeg" in root:
        FFMPEG = os.path.join(root, "ffmpeg.exe")
        break

WORK = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\.tools"
SRC = os.path.join(WORK, "wix", "dl", "vr_video.mp4")
TMP = os.path.join(WORK, "wix", "vr_probe2")
os.makedirs(TMP, exist_ok=True)

SAMPLES = [8.0, 14.0, 18.0, 30.0, 40.0, 50.0, 60.0, 70.0, 84.0, 92.0, 100.0]


def grab(ts, out):
    subprocess.run([FFMPEG, "-v", "error", "-ss", str(ts), "-i", SRC, "-frames:v", "1",
                    "-q:v", "2", out, "-y"], check=True)


def runs(values, thresh):
    """Return (start, end) of runs where value > thresh, longest first."""
    out, s = [], None
    for i, v in enumerate(values):
        if v > thresh and s is None:
            s = i
        elif v <= thresh and s is not None:
            out.append((s, i)); s = None
    if s is not None:
        out.append((s, len(values)))
    return sorted(out, key=lambda r: r[1] - r[0], reverse=True)


THRESH = 60          # game view pixels are clearly brighter than the ~35 chrome

xs, ys = [], []
for ts in SAMPLES:
    p = os.path.join(TMP, "t%05.1f.jpg" % ts)
    grab(ts, p)
    im = Image.open(p).convert("L")
    w, h = im.size
    px = im.load()
    # widest bright run on a horizontal line through the middle of the game view
    col_profile = [sum(px[x, y] for y in range(60, 280)) / 220 for x in range(w)]
    row_profile = [sum(px[x, y] for x in range(140, 560)) / 420 for y in range(h)]
    cr, rr = runs(col_profile, THRESH), runs(row_profile, THRESH)
    cb = cr[0] if cr else None
    rb = rr[0] if rr else None
    print("t=%5.1fs  x-run=%s  y-run=%s" % (ts, cb, rb))
    if cb:
        xs.append(cb)
    if rb:
        ys.append(rb)

if xs and ys:
    x0 = max(a for a, _ in xs)
    x1 = min(b for _, b in xs)
    y0 = max(a for a, _ in ys)
    y1 = min(b for _, b in ys)
    print("\nintersection: x %d..%d  y %d..%d" % (x0, x1, y0, y1))
    w = x1 - x0
    h = round(w * 9 / 16)
    if y0 + h > y1:
        h = y1 - y0
        w = round(h * 16 / 9)
    print("suggested 16:9 crop: (%d, %d, %d, %d) -> %dx%d" % (x0, y0, x0 + w, y0 + h, w, h))
