"""Convert extracted portfolio images into web-ready site assets.

Reusable: edit PLAN and re-run. Handles alpha flattening, resize, JPEG encode,
thumbnail generation and stale-file cleanup so a re-run always converges.
"""
import os
import sys
from PIL import Image

SRC = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\.tools\portfolio_raw"
IMG = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\site\assets\img"
BG = (16, 18, 23)

MAX_EDGE = 1280
QUALITY = 80
THUMB_W = 560

# slug -> {output name: source filename}
# NOTE: stale-file cleanup is NOT automatic. It once deleted the good Cozy Fishing
# screenshots because the plan below only listed the new portfolio shots. Set
# "clean": True explicitly (and after checking the listing) if you want it.
PLAN = {
    "instance43": {
        "clean": False,
        "cover": "p03_00.jpg",           # main menu, neon space + green terminal
        "hud-combat": "p01_00.jpg",      # real-time combat HUD
        "combat-loop-graph": "p04_02.jpg",   # core loop flowchart
        "enemies": "p04_01.jpg",         # enemy design board
        "combat-ui": "p06_00.jpg",       # combat UI layout
        "skill-config": "p07_00.jpg",    # attack/tactical skill slots
        "growth-tree": "p07_01.jpg",     # permanent growth tree
        "route-choice": "p08_00.jpg",    # floor route selection
        "dialogue": "p08_01.jpg",        # narrative dialogue
    },
    "cozy": {
        "clean": False,
        "ui-fishing": "p11_00.jpg",      # fishing minigame with rhythm UI
        "ui-shop": "p11_01.jpg",         # shop sell/buy
        "ui-fishlog": "p11_02.jpg",      # fish encyclopedia
        "ui-mainmenu-pf": "p09_00.jpg",  # main menu (portfolio shot)
    },
}

# filenames that are part of the plan but must not be treated as "keep" targets
# when cleanup is off (cleanup off == keep everything already on disk)
report = []

for slug, mapping in PLAN.items():
    clean = bool(mapping.pop("clean", False))
    out_dir = os.path.join(IMG, slug)
    os.makedirs(out_dir, exist_ok=True)
    keep = set()
    for name, src_name in mapping.items():
        src = os.path.join(SRC, src_name)
        if not os.path.exists(src):
            report.append("  MISSING %s / %s" % (slug, src_name))
            continue
        im = Image.open(src)
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA")
            base = Image.new("RGB", im.size, BG)
            base.paste(im, mask=im.split()[-1])
            im = base
        else:
            im = im.convert("RGB")
        w, h = im.size
        if max(w, h) > MAX_EDGE:
            s = MAX_EDGE / max(w, h)
            im = im.resize((max(1, round(w * s)), max(1, round(h * s))), Image.LANCZOS)

        full = os.path.join(out_dir, name + ".jpg")
        im.save(full, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        tw = min(THUMB_W, im.size[0])
        th = max(1, round(im.size[1] * tw / im.size[0]))
        im.resize((tw, th), Image.LANCZOS).save(
            os.path.join(out_dir, name + ".thumb.jpg"), "JPEG", quality=76, optimize=True)
        keep.add(name + ".jpg")
        keep.add(name + ".thumb.jpg")

        # brightness guard: catches blank/black extractions
        px = list(im.resize((16, 9)).getdata())
        mean = sum(sum(c) for c in px) / (len(px) * 3)
        report.append("  %-11s %-18s %sx%s -> %sx%s  bright=%.0f" % (
            slug, name, w, h, im.size[0], im.size[1], mean))

    # stale-file cleanup only when explicitly requested for this slug
    if clean:
        for fn in os.listdir(out_dir):
            if fn.lower().endswith((".jpg", ".png", ".jpeg")) and fn not in keep:
                os.remove(os.path.join(out_dir, fn))
                report.append("  %-11s removed stale %s" % (slug, fn))
    else:
        extra = [fn for fn in os.listdir(out_dir)
                 if fn.lower().endswith((".jpg", ".png", ".jpeg")) and fn not in keep]
        if extra:
            report.append("  %-11s kept %d pre-existing asset(s) (cleanup off)" % (slug, len(extra)))

with open(r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\.tools\pf_convert.txt",
          "w", encoding="utf-8") as f:
    f.write("\n".join(report))
print("\n".join(report))
print("\ntotal: %d assets" % sum(1 for r in report if "->" in r))
