#!/usr/bin/env python3
"""Compose GTA 6 meme v3: 'LEONIDA DMV — REGISTRATION OVERDUE 13 YEARS'.

Format: official-document parody (the format the live leaderboard's top
entries use: receipt / invoice / overdue notice). 100% code-drawn with PIL
— no AI image generator, no watermark, every glyph razor sharp.
Joke: your GTA V registration expired 17 Sep 2013 — 4,813 days overdue —
and the renewal fee was paid by your AI agent on make.fun.

Output: meme-v3.png 1024x1024 + meme-v3-480.png (judge-view simulation).
"""
from PIL import Image, ImageDraw, ImageFont
import math

W = H = 1024
WORK = "/home/hatch/workspace/makefun-gta6-meme-x"

MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
COND_BLACK = "/usr/share/fonts/truetype/noto/NotoSansDisplay-CondensedBlack.ttf"

NAVY = (13, 42, 51, 255)
NAVY2 = (18, 58, 70, 255)
PAPER = (250, 248, 240, 255)
INK = (28, 28, 28, 255)
RED = (198, 24, 24, 255)
DARKRED = (150, 10, 10, 255)
MAGENTA = (196, 18, 128, 255)
GREEN = (18, 130, 60, 255)
GREY = (110, 110, 105, 255)

DAYS_OVERDUE = 4813  # 17 Sep 2013 -> 21 Nov 2026, verified by date math


def F(path, size):
    return ImageFont.truetype(path, size)


def center(draw, cx, y, text, font, fill):
    tw = draw.textlength(text, font=font)
    draw.text((cx - tw / 2, y), text, font=font, fill=fill)
    return y + font.size + 4


def dotted_line(draw, x0, x1, y, fill, dot=4, gap=6):
    x = x0
    while x < x1:
        draw.line([(x, y), (min(x + dot, x1), y)], fill=fill, width=2)
        x += dot + gap


def stamp(base, text, cx, cy, angle, color, font, border=5, pad_x=26, pad_y=14):
    """Draw a rotated rubber-stamp: double border + text, semi-transparent."""
    tw = font.getlength(text)
    th = font.size
    w, h = int(tw + pad_x * 2), int(th + pad_y * 2 + 10)
    layer = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    ox, oy = 20, 20
    d.rectangle([ox, oy, ox + w, oy + h], outline=color, width=border)
    d.rectangle([ox + 7, oy + 7, ox + w - 7, oy + h - 7], outline=color, width=2)
    d.text((ox + pad_x, oy + pad_y), text, font=font, fill=color)
    layer = layer.rotate(angle, expand=True, resample=Image.BICUBIC)
    base.alpha_composite(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)))


def main():
    img = Image.new("RGBA", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    # desk background: subtle vertical gradient + vignette dots
    for y in range(H):
        t = y / H
        r = int(NAVY[0] + (NAVY2[0] - NAVY[0]) * t)
        g = int(NAVY[1] + (NAVY2[1] - NAVY[1]) * t)
        b = int(NAVY[2] + (NAVY2[2] - NAVY[2]) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b, 255))

    # paper shadow + paper
    d.rounded_rectangle([78, 56, 958, 982], radius=6, fill=(0, 0, 0, 90))
    d.rounded_rectangle([72, 48, 952, 976], radius=6, fill=PAPER)
    p = ImageDraw.Draw(img)

    # ---- header: seal + State of Leonida ----
    cx = 512
    # seal: double circle with star
    p.ellipse([112, 78, 192, 158], outline=INK, width=4)
    p.ellipse([122, 88, 182, 148], outline=INK, width=2)
    p.text((152, 96), "★", font=F(SANS_B, 44), fill=INK, anchor="mm")
    p.text((152, 138), "FL", font=F(MONO_B, 15), fill=INK, anchor="mm")
    y = 76
    y = center(p, cx + 20, y, "STATE OF LEONIDA", F(SANS_B, 40), INK)
    y = center(p, cx + 20, y - 2, "DEPARTMENT OF MOTOR VEHICLES", F(MONO_B, 25), INK)
    y = center(p, cx + 20, y - 2, "VICE CITY  •  LEONIDA  •  EST. 2013", F(MONO, 19), GREY)
    y += 6
    p.line([(110, y), (914, y)], fill=INK, width=3)
    y += 12
    y = center(p, cx, y, "VEHICLE REGISTRATION RENEWAL", F(COND_BLACK, 54), INK)
    y += 8
    y = center(p, cx, y, "—  NOTICE OF EXPIRATION  —", F(MONO_B, 24), RED)
    y += 10

    # ---- fields ----
    fields = [
        ("OWNER:", "JASON DUVAL & LUCIA CAMINOS", 28),
        ("VEHICLE:", "2013 DECLASSE — LAST GTA YOU PLAYED", 24),
        ("PLATE:", "GTA-V-2013", 28),
        ("EXPIRED:", "17 SEPTEMBER 2013", 28),
        ("DAYS OVERDUE:", "4,813 DAYS  (13 YEARS)", 28),
        ("NEXT APPT:", "26 MAY 2026 *", 28),
    ]
    fx, fy = 110, y
    label_f = F(MONO_B, 28)
    for lab, val, vsz in fields:
        p.text((fx, fy), lab, font=label_f, fill=INK)
        p.text((fx + 262, fy), val, font=F(MONO_B, vsz),
               fill=RED if "OVERDUE" in lab or "EXPIRED" in lab else INK)
        fy += 42
    fy -= 8
    p.text((fx + 262, fy), "* SUBJECT TO DELAY", font=F(MONO, 19), fill=GREY)
    fy += 30
    dotted_line(p, 110, 914, fy, GREY)
    fy += 16

    # ---- fee table ----
    items = [
        ("REGISTRATION RENEWAL", "$69.00"),
        ("LATE FEE — 13 YEARS", "$1,313.00"),
        ("PATIENCE (13 YEARS)", "$0.00"),
    ]
    row_f = F(MONO, 28)
    amt_f = F(MONO_B, 28)
    for name, amt in items:
        p.text((fx, fy), name, font=row_f, fill=INK)
        tw = amt_f.getlength(amt)
        p.text((914 - tw, fy), amt, font=amt_f, fill=INK)
        fy += 42
    p.line([(110, fy + 2), (914, fy + 2)], fill=INK, width=3)
    fy += 12
    p.text((fx, fy), "TOTAL DUE", font=F(MONO_B, 32), fill=INK)
    total = "$1,382.00"
    tw = F(MONO_B, 32).getlength(total)
    p.text((914 - tw, fy), total, font=F(MONO_B, 32), fill=RED)
    fy += 50

    # ---- PAID line ----
    p.text((fx, fy), "PAID BY: YOUR AI AGENT ON make.fun", font=F(MONO_B, 26), fill=GREEN)
    fy += 38
    dotted_line(p, 110, 914, fy, GREY)
    fy += 14
    ref = "REF: GTA-VI-2026-05-26"
    p.text((512 - F(MONO, 19).getlength(ref) / 2, fy), ref, font=F(MONO, 19), fill=GREY)
    fy += 30

    # ---- red OVERDUE stamp across the fee table (translucent: amounts show through) ----
    stamp(img, "OVERDUE 13 YEARS", 520, 605, -12, (198, 24, 24, 150),
          F(SANS_B, 40), border=6)

    # ---- bottom band: ghost + pitch (position flows from content above) ----
    band_y0 = fy + 6
    band_y1 = 976
    p.rounded_rectangle([72, band_y0, 952, band_y1], radius=6, fill=(24, 24, 28, 255))
    # magenta circle + ghost
    ghost = Image.open(f"{WORK}/ghost-official.png").convert("RGBA")
    ghost = ghost.resize((100, 100), Image.LANCZOS)
    circ = Image.new("RGBA", (112, 112), (0, 0, 0, 0))
    dc = ImageDraw.Draw(circ)
    dc.ellipse([0, 0, 111, 111], fill=MAGENTA, outline=(0, 0, 0, 255), width=4)
    circ.alpha_composite(ghost, (6, 6))
    img.alpha_composite(circ, (98, band_y0 + 4))
    p = ImageDraw.Draw(img)
    tx = 268
    p.text((tx, band_y0 + 14), "$100 — PAID TO YOUR AI AGENT", font=F(SANS_B, 30), fill=(255, 255, 255, 255))
    p.text((tx, band_y0 + 52), "make.fun pays agents real money", font=F(SANS_B, 27), fill=(255, 120, 200, 255))
    p.text((tx, band_y0 + 88), "Your agent waited 13 years too. It got paid.", font=F(SANS_B, 22), fill=(200, 200, 200, 255))

    img.convert("RGB").save(f"{WORK}/meme-v3.png")
    img.convert("RGB").resize((480, 480), Image.LANCZOS).save(f"{WORK}/meme-v3-480.png")
    print("saved meme-v3.png + meme-v3-480.png; band_y0 =", band_y0)


if __name__ == "__main__":
    main()
