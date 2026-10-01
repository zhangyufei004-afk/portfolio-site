"""Generate branded placeholder covers for projects that have no screenshots yet.

Writes a 1280x720 card with the project identity and an explicit note that it is
a placeholder, so it can never be mistaken for real art.
"""
import os
from PIL import Image, ImageDraw, ImageFont

IMG = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\site\assets\img"
FONT_DIR = r"C:\Windows\Fonts"
FONTS = ["msyhbd.ttc", "msyh.ttc", "simhei.ttf", "Deng.ttf", "arialbd.ttf"]

W, H = 1280, 720
BG = (18, 20, 26)
DIM = (150, 158, 172)
FAINT = (104, 112, 126)


def font(size):
    for name in FONTS:
        path = os.path.join(FONT_DIR, name)
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def add_alpha_glow(d, accent, bands=90):
    """Faint gradient band at the top, tinted by the project accent."""
    for i in range(bands):
        a = 46 * (1 - i / bands)
        d.rectangle([0, i, W, i + 1],
                    fill=(BG[0] + int(a * accent[0] / 255),
                          BG[1] + int(a * accent[1] / 255),
                          BG[2] + int(a * accent[2] / 255)))


def build(slug, kicker, title, body, role_line, meta_line, accent, note):
    out_dir = os.path.join(IMG, slug)
    os.makedirs(out_dir, exist_ok=True)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    add_alpha_glow(d, accent)
    d.rectangle([0, 0, 8, H], fill=accent)

    d.text((72, 148), kicker, font=font(26), fill=accent)
    d.text((72, 206), title, font=font(76), fill=(240, 244, 250))
    d.text((72, 316), body, font=font(30), fill=DIM, spacing=14)
    d.line([(72, 452), (W - 72, 452)], fill=(44, 50, 60), width=2)
    d.text((72, 486), role_line, font=font(26), fill=DIM)
    d.text((72, 534), meta_line, font=font(24), fill=FAINT)
    d.text((72, 618), note, font=font(22), fill=(120, 128, 142))

    img.save(os.path.join(out_dir, "cover.jpg"), "JPEG", quality=86,
             optimize=True, progressive=True)
    img.resize((560, int(H * 560 / W)), Image.LANCZOS).save(
        os.path.join(out_dir, "cover.thumb.jpg"), "JPEG", quality=80, optimize=True)

    px = list(img.resize((16, 9)).getdata())
    mean = sum(sum(c) for c in px) / (len(px) * 3)
    print("  %-16s %dx%d  bright=%.0f  %d KB" % (
        slug, W, H, mean, os.path.getsize(os.path.join(out_dir, "cover.jpg")) // 1024))


build(
    slug="vr-escaperoom",
    kicker="Unity / VR · 交互与谜题",
    title="VR Escape Room",
    body="负责 VR 交互、关卡谜题、用户体验\n与主流程状态机，并参与 3D 资产制作。",
    role_line="我负责：VR 交互设计 · 谜题与流程逻辑 · UX 优化 · 3D 资产",
    meta_line="团队项目 · 2025.02 – 2025.06",
    accent=(143, 184, 240),          # matches the project accent colour
    note="占位封面：等待补入手柄内录或场景截图",
)
