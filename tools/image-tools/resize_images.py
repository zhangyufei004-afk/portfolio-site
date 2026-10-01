"""Re-encode every site image to a web-appropriate size.

Target: keep the whole site comfortably under ~20 MB so it loads quickly on a
domestic host. Screenshots are re-encoded at a 1280px max edge, quality 76;
nothing is upscaled, and thumbnails are regenerated from the resized source.
"""
import os, sys
from PIL import Image

IMG = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\site\assets\img"
BG = (16, 18, 23)

MAX_EDGE = 1280
QUALITY = 76
THUMB_W = 560
THUMB_Q = 74

# images that are pure flat art or diagrams keep a bit more quality
HIGH_QUALITY = {"architecture", "macro", "sketch", "ref-pacman", "ref-amnesia",
                "favicon", "logo", "plan-jira", "plan-trello", "journal-gui"}
THUMB_SKIP = {"favicon"}

total_before = 0
total_after = 0
rows = []

for dirpath, _, files in os.walk(IMG):
    slug = os.path.basename(dirpath)
    for fn in sorted(files):
        if not fn.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            continue
        if fn.lower().endswith(".svg"):
            continue
        path = os.path.join(dirpath, fn)
        stem = os.path.splitext(fn)[0]
        is_thumb = stem.endswith(".thumb")
        base_name = stem[:-6] if is_thumb else stem
        if base_name in THUMB_SKIP:
            continue

        before = os.path.getsize(path)
        total_before += before

        im = Image.open(path)
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA")
            flat = Image.new("RGB", im.size, BG)
            flat.paste(im, mask=im.split()[-1])
            im = flat
        else:
            im = im.convert("RGB")

        q = 84 if base_name in HIGH_QUALITY else QUALITY
        w, h = im.size

        if is_thumb:
            if w > THUMB_W:
                h2 = max(1, round(h * THUMB_W / w))
                im = im.resize((THUMB_W, h2), Image.LANCZOS)
            out = os.path.join(dirpath, base_name + ".thumb.jpg")
            im.save(out, "JPEG", quality=THUMB_Q, optimize=True, progressive=True)
        else:
            if max(w, h) > MAX_EDGE:
                s = MAX_EDGE / max(w, h)
                im = im.resize((max(1, round(w * s)), max(1, round(h * s))), Image.LANCZOS)
            out = os.path.join(dirpath, base_name + ".jpg")
            im.save(out, "JPEG", quality=q, optimize=True, progressive=True)

        # remove the original if the new name differs (png -> jpg)
        if os.path.abspath(out) != os.path.abspath(path) and os.path.exists(path):
            os.remove(path)

        after = os.path.getsize(out)
        total_after += after
        rows.append("%-12s %-26s %5dx%-5d %7dKB -> %7dKB" % (slug, os.path.basename(out), w, h, before // 1024, after // 1024))

with open(r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\.tools\resize_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(rows))
    f.write("\n\nTOTAL %.1f MB -> %.1f MB\n" % (total_before / 1048576, total_after / 1048576))

print("\n".join(rows))
print("\nTOTAL %.1f MB -> %.1f MB" % (total_before / 1048576, total_after / 1048576))
