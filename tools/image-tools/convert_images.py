"""Convert the raw PDF-extracted images into web-ready assets with clean names.

- flattens alpha onto the site's dark background
- downsizes to a max edge of 1600px and re-encodes as JPEG (quality 82)
- also emits a 640px-wide thumbnail for cards
Raw originals are moved to .tools/img_raw/ so they are never lost.
"""
import os, shutil, sys
from PIL import Image

SITE = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\site"
IMG = os.path.join(SITE, "assets", "img")
RAW = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\.tools\img_raw"
BG = (16, 18, 23)

# slug -> {new_name: original_filename}
PLAN = {
    "echos": {
        "cover": "p10_00_e3e7aedcfe18.png",
        "ref-pacman": "p04_00_2edd50ee43ed.png",
        "ref-amnesia": "p04_01_fa3be73d85f0.png",
        "navmesh-bake": "p06_00_99aea4fff413.png",
        "blockout-level": "p07_00_1815b366f08f.png",
        "ai-placeholder": "p07_01_94b5b7cdd1a4.png",
        "architecture": "p08_00_c1be1a9bdfde.png",
        "monster-model": "p09_00_aa98ed6a7cd5.png",
        "hiding-cabinet": "p09_01_79a8e4ce3c1c.png",
        "navmesh-agent-radius-a": "p10_00_e3e7aedcfe18.png",
        "navmesh-agent-radius-b": "p10_01_09d34f70ea0e.png",
        "win-screen": "p11_00_4bd8eba2e3c4.png",
        "death-screen": "p11_01_8b1d913cb309.png",
    },
    "als": {
        "cover": "p33_00_16c1dc12d102.png",
        "mood-1": "p13_00_dd1c6eba5974.png",
        "mood-2": "p13_01_cd20a8808910.png",
        "mood-3": "p13_02_71caf93e6739.png",
        "blockout-a": "p20_00_1119bc2c2492.png",
        "blockout-b": "p20_01_e784d4f338ec.png",
        "alpha-a": "p23_00_ba4216aadbd3.png",
        "alpha-b": "p23_01_57a7512d0d24.png",
        "beta-a": "p27_00_ead0d57046da.png",
        "beta-b": "p27_01_59bbf54cc175.png",
        "gamma-a": "p30_00_2756c85b986d.png",
        "final-a": "p33_00_16c1dc12d102.png",
        "final-b": "p33_01_cdccf6ca2425.png",
        "final-c": "p34_00_1008afad3794.png",
        "final-d": "p35_00_d852c8fbfeb1.png",
    },
    "portal2": {
        "cover": "p21_00_90ae077ec16f.png",
        "sketch-a": "p08_00_eb76809c6654.png",
        "sketch-b": "p09_00_7ff70ea06289.png",
        "sketch-c": "p10_00_a15448e1a735.png",
        "blockout-a": "p12_00_fc6b35d944b2.png",
        "blockout-b": "p12_01_10d77e0393da.png",
        "blockout-c": "p13_00_dddbae6e90ec.png",
        "beta-a": "p16_00_c840ca825b7e.png",
        "beta-b": "p16_01_bca88be83d52.png",
        "beta-c": "p17_00_2014c8bf2e4b.png",
        "gamma-a": "p19_00_bbdeb2fd054d.png",
        "gamma-b": "p20_00_4e59b4453bd8.png",
        "final-a": "p21_00_90ae077ec16f.png",
        "final-b": "p22_00_67f0b39bfc8c.png",
        "final-c": "p23_00_ff70fbf34247.png",
        "final-d": "p24_00_c65c67355faf.png",
    },
    "delver2d": {
        "cover": "p17_00_d4ec109538c0.png",
        "macro": "p05_00_9c7a7c5175a2.png",
        "sketch": "p08_00_20c2fe78b579.png",
        "blockout-a": "p10_00_d223c9ae7362.png",
        "blockout-b": "p10_01_c0141a0b8888.png",
        "alpha-a": "p13_00_6d80d2203c46.png",
        "beta-before": "p14_00_e61a154afca8.png",
        "beta-after": "p15_00_ca808eb816cd.png",
        "final-before": "p17_00_d4ec109538c0.png",
        "final-after": "p18_00_52064debd6db.png",
    },
    "cozy": {
        "cover": "p01_00_9718ff1d7dc0.png",
        "logo": "p01_00_9718ff1d7dc0.png",
        "shot-a": "p02_00_09f2cc06d598.png",
        "shot-b": "p02_01_a40df76a26e4.png",
        "shot-c": "p03_00_3da05883918f.png",
        "board": "p08_00_b0c6042ceff4.png",
    },
}

os.makedirs(RAW, exist_ok=True)
report = []


def flatten(im: Image.Image) -> Image.Image:
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        base = Image.new("RGB", im.size, BG)
        base.paste(im, mask=im.split()[-1])
        return base
    return im.convert("RGB")


for slug, mapping in PLAN.items():
    src_dir = os.path.join(IMG, slug)
    if not os.path.isdir(src_dir):
        report.append("SKIP missing dir %s" % slug)
        continue
    out_dir = os.path.join(RAW, slug + "_converted")
    os.makedirs(out_dir, exist_ok=True)
    for new_name, orig in mapping.items():
        src = os.path.join(src_dir, orig)
        if not os.path.exists(src):
            report.append("  MISSING %s/%s" % (slug, orig))
            continue
        im = flatten(Image.open(src))
        w, h = im.size
        if max(w, h) > 1600:
            scale = 1600 / max(w, h)
            im = im.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)
        big = os.path.join(out_dir, new_name + ".jpg")
        im.save(big, "JPEG", quality=82, optimize=True, progressive=True)
        tw = min(640, im.size[0])
        th = max(1, round(im.size[1] * tw / im.size[0]))
        thumb = im.resize((tw, th), Image.LANCZOS)
        thumb.save(os.path.join(out_dir, new_name + ".thumb.jpg"), "JPEG", quality=78, optimize=True)
        report.append("  %-10s %-26s %sx%s -> %sx%s" % (slug, new_name, w, h, im.size[0], im.size[1]))

with open(r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\.tools\convert_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report))
print("\n".join(report))
print("\nconverted %d images" % sum(1 for r in report if "->" in r))
