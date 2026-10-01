"""Final Bounty Hunter asset export.

Timeline verified by dense sampling of the trailer (see .tools/preview/bh_dense.jpg):
  26s "CRIMINAL" card        27s interior w/ guards + Flair
  28s city street fight      29s boss/duel frame
  30s mountain level + HUD   31s equipment/inventory UI
  32-33s "WILL YOU SUCCEED?" 34s mountain gameplay
  35s mountain gameplay      36s "Cara The Shopkeeper" intro card
  39-41s "BOUNTY HUNTER" title card
  42s credits (background designer: YUFEI ZHANG)
"""
import os, subprocess
from PIL import Image

FFMPEG = None
for root, _, files in os.walk(r"C:\Users\fyhy2\AppData\Local\Microsoft\WinGet\Packages"):
    if "ffmpeg.exe" in files and "Gyan.FFmpeg" in root:
        FFMPEG = os.path.join(root, "ffmpeg.exe")
        break
if not FFMPEG:
    raise SystemExit("ffmpeg not found")

WORK = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\.tools"
SRC = os.path.join(WORK, "bh_trailer.mp4")
IMG = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\site\assets\img\bounty-hunter"
MED = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\site\assets\media\bounty-hunter"
TMP = os.path.join(WORK, "frames_final")
os.makedirs(TMP, exist_ok=True)

STILLS = [
    ("level-mountain", 30.0),     # mountain level, boss health bar + HUD
    ("level-mountain-b", 34.0),   # mountain level, second section
    ("level-city", 28.0),         # city street fight
    ("level-compound", 27.0),     # interior facility with guards
    ("level-compound-b", 35.0),   # mountain/facility traversal
    ("duel", 29.0),               # face-off frame
    ("ui-shop", 36.0),            # "Cara The Shopkeeper" UI card
    ("ui-equipment", 31.0),       # equipment slots
]
POSTER_TS = 42.0                  # credits card
COVER = "ui-shop"

for fn in os.listdir(IMG):
    if fn.endswith((".jpg", ".jpeg", ".png")):
        os.remove(os.path.join(IMG, fn))


def grab(ts, out, width=1280):
    subprocess.run([FFMPEG, "-v", "error", "-ss", str(ts), "-i", SRC, "-frames:v", "1",
                    "-vf", "scale=%d:-2" % width, "-q:v", "3", out, "-y"], check=True)
    if not os.path.exists(out) or os.path.getsize(out) < 2000:
        raise SystemExit("suspiciously small frame at %.1fs -> %s" % (ts, out))


def brightness(im):
    px = list(im.resize((16, 9)).convert("RGB").getdata())
    return sum(sum(c) for c in px) / (len(px) * 3)


def emit(im, name, quality=80):
    """Save a still plus its card thumbnail, refusing near-black frames."""
    b = brightness(im)
    if b < 25:
        raise SystemExit("frame for %s is almost black (brightness %.1f)" % (name, b))
    im.save(os.path.join(IMG, name + ".jpg"), "JPEG", quality=quality,
            optimize=True, progressive=True)
    tw = 560
    im.resize((tw, max(1, round(im.size[1] * tw / im.size[0]))), Image.LANCZOS).save(
        os.path.join(IMG, name + ".thumb.jpg"), "JPEG", quality=76, optimize=True)
    return b


report = []
for name, ts in STILLS:
    raw = os.path.join(TMP, name + ".jpg")
    grab(ts, raw)
    im = Image.open(raw).convert("RGB")
    b = emit(im, name)
    report.append("  %-18s %5.1fs  bright=%5.1f  %dx%d" % (name, ts, b, im.size[0], im.size[1]))

# trailer poster (credits card) lives with the media, not in the image gallery
raw = os.path.join(TMP, "poster.jpg")
grab(POSTER_TS, raw)
Image.open(raw).convert("RGB").save(os.path.join(MED, "poster.jpg"), "JPEG",
                                    quality=84, optimize=True, progressive=True)
report.append("  %-18s %5.1fs" % ("poster", POSTER_TS))

# cover: the shopkeeper UI card shows both a designed character card and the UI style
cover_ts = dict(STILLS)[COVER]
raw = os.path.join(TMP, "cover.jpg")
grab(cover_ts, raw)
im = Image.open(raw).convert("RGB")
b = brightness(im)
if b < 25:
    raise SystemExit("cover frame is almost black (brightness %.1f)" % b)
im.save(os.path.join(IMG, "cover.jpg"), "JPEG", quality=82, optimize=True, progressive=True)
im.resize((560, max(1, round(im.size[1] * 560 / im.size[0]))), Image.LANCZOS).save(
    os.path.join(IMG, "cover.thumb.jpg"), "JPEG", quality=78, optimize=True)
report.append("  %-18s %5.1fs  bright=%5.1f  (cover)" % (COVER, cover_ts, b))

print("\n".join(report))
print("\nfiles in assets/img/bounty-hunter:")
for fn in sorted(os.listdir(IMG)):
    print("  %-30s %6d KB" % (fn, os.path.getsize(os.path.join(IMG, fn)) // 1024))
print("\nfiles in assets/media/bounty-hunter:")
for fn in sorted(os.listdir(MED)):
    print("  %-30s %6d KB" % (fn, os.path.getsize(os.path.join(MED, fn)) // 1024))
