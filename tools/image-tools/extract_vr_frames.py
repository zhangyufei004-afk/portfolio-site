"""Export VR Escape Room stills from the Wix-hosted gameplay recording.

Source: https://video.wixstatic.com/video/80bc9b_7726357e854e4105a808c0b377a173f0/480p/mp4/file.mp4
854x480 / 60fps / 113s. It is a Unity editor recording, so every frame includes the
editor chrome; the game view is the upper-left region, which is what we crop.

Timestamps were picked from a tiled overview of the whole clip.
"""
import os
import subprocess
from PIL import Image

FFMPEG = None
for root, _, files in os.walk(r"C:\Users\fyhy2\AppData\Local\Microsoft\WinGet\Packages"):
    if "ffmpeg.exe" in files and "Gyan.FFmpeg" in root:
        FFMPEG = os.path.join(root, "ffmpeg.exe")
        break
if not FFMPEG:
    raise SystemExit("ffmpeg not found")

WORK = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\.tools"
SRC = os.path.join(WORK, "wix", "dl", "vr_video.mp4")
IMG = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\site\assets\img\vr-escaperoom"
TMP = os.path.join(WORK, "wix", "vr_frames")
os.makedirs(IMG, exist_ok=True)
os.makedirs(TMP, exist_ok=True)

# name -> (timestamp seconds, crop the Unity game view out of the editor frame)
SHOTS = [
    ("briefing", 8.0),          # intro note, full wall visible
    ("room-red", 14.0),         # red room isometric view
    ("room-red-close", 18.0),   # lever + gear up close
    ("room-shelf", 40.0),       # shelf room with VR hand + laser pointer
    ("room-laser", 60.0),       # laser beam across the room
    ("puzzle-buttons", 84.0),   # coloured button puzzle + dial
    ("puzzle-dial", 92.0),      # dial puzzle from above
]
COVER = "room-shelf"

# Game view inside the editor window, measured by brightness profile over 11 frames
# (see .tools/detect_gameview.py): x 120..582, y 50..310.
# Inset 10px on every side to stay clear of the editor borders (scrollbar, tabs),
# then fitted to an exact 16:9 box so the 2x upscale does not letterbox.
CROP = (130, 60, 578, 312)      # 448 x 252 == 16:9


def grab(ts, out):
    subprocess.run([FFMPEG, "-v", "error", "-ss", str(ts), "-i", SRC, "-frames:v", "1",
                    "-q:v", "2", out, "-y"], check=True)


def brightness(im):
    px = list(im.resize((16, 9)).convert("RGB").getdata())
    return sum(sum(c) for c in px) / (len(px) * 3)


def emit(im, name, quality=88):
    b = brightness(im)
    if b < 20:
        raise SystemExit("frame for %s is nearly black (%.1f)" % (name, b))
    w, h = im.size
    tw = w * 2                      # 560 -> 1120
    im2 = im.resize((tw, round(h * tw / w)), Image.LANCZOS)
    im2.save(os.path.join(IMG, name + ".jpg"), "JPEG", quality=quality,
             optimize=True, progressive=True)
    th = max(1, round(im2.size[1] * 560 / im2.size[0]))
    im2.resize((560, th), Image.LANCZOS).save(
        os.path.join(IMG, name + ".thumb.jpg"), "JPEG", quality=80, optimize=True)
    return b, im2.size


report = []
for name, ts in SHOTS:
    raw = os.path.join(TMP, name + ".jpg")
    grab(ts, raw)
    im = Image.open(raw).convert("RGB").crop(CROP)
    b, size = emit(im, name)
    report.append("  %-20s %5.1fs  bright=%5.1f  -> %dx%d" % (name, ts, b, size[0], size[1]))

raw = os.path.join(TMP, "cover.jpg")
grab(dict(SHOTS)[COVER], raw)
im = Image.open(raw).convert("RGB").crop(CROP)
b, size = emit(im, "cover")
report.append("  %-20s %5.1fs  bright=%5.1f  -> %dx%d  (cover)" % (COVER, dict(SHOTS)[COVER], b, size[0], size[1]))

print("\n".join(report))
print("\nfiles:")
for fn in sorted(os.listdir(IMG)):
    print("  %-28s %6d KB" % (fn, os.path.getsize(os.path.join(IMG, fn)) // 1024))
