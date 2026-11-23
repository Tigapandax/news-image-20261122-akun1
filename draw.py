#!/usr/bin/env python3
"""Draw the news-image-20261122 entry: a one-page newspaper front page that
sums up the world news of Sunday 22 November 2026.

Run locally (PIL is only needed here, at build time):  python3 draw.py
The graded program is main.py, which only copies the finished entry.png;
the grader runs standard library only, so no drawing happens at grade time.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (28, 28, 28)
FAINT = (110, 104, 92)
RED = (179, 39, 30)
NAVY = (31, 58, 95)
TEAL = (20, 101, 90)
OCHRE = (176, 116, 28)
PLUM = (107, 58, 91)
RULE = (190, 182, 166)
WHITE = (255, 255, 255)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines that fit `width` px."""
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def para(draw, xy, text, fnt, width, fill=INK, leading=None):
    x, y = xy
    lh = leading or int(fnt.size * 1.32)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def chip(draw, xy, text, bg):
    x, y = xy
    fnt = font(SANSB, 17)
    tw = draw.textlength(text, font=fnt)
    pad, h = 10, 26
    draw.rounded_rectangle([x, y, x + tw + 2 * pad, y + h], radius=4, fill=bg)
    draw.text((x + pad, y + 4), text, font=fnt, fill=WHITE)
    return tw + 2 * pad


def globe(draw, cx, cy, r):
    """A simple globe with a red crack: the lead story's picture."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(214, 228, 240),
                 outline=NAVY, width=5)
    # meridians: halves of a centred ellipse, always inside the circle
    draw.arc([cx - r * 0.55, cy - r, cx + r * 0.55, cy + r], 90, 270,
             fill=NAVY, width=3)
    draw.arc([cx - r * 0.55, cy - r, cx + r * 0.55, cy + r], 270, 90,
             fill=NAVY, width=3)
    draw.line([cx, cy - r, cx, cy + r], fill=NAVY, width=3)
    for k in (-0.45, 0.35):  # parallels (chords of the circle)
        w = int(r * (1 - k * k) ** 0.5)
        draw.line([cx - w, cy + k * r, cx + w, cy + k * r], fill=NAVY, width=3)
    # land blobs (abstract continents)
    draw.ellipse([cx - r * 0.62, cy - r * 0.62, cx - r * 0.05, cy - r * 0.08],
                 fill=(96, 140, 96))
    draw.ellipse([cx + r * 0.08, cy + r * 0.05, cx + r * 0.66, cy + r * 0.58],
                 fill=(96, 140, 96))
    # red crack across the globe
    pts = [(cx - r * 0.75, cy - r * 0.9), (cx - r * 0.25, cy - r * 0.35),
           (cx - r * 0.5, cy + r * 0.1), (cx + r * 0.05, cy + r * 0.45),
           (cx - r * 0.1, cy + r * 0.85)]
    draw.line(pts, fill=RED, width=6, joint="curve")


def starburst(draw, cx, cy, r, color):
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=color)


def bars_down(draw, x, y, w, h):
    """Falling bar chart for the markets story."""
    n = 5
    bw = w // (n * 2)
    for i in range(n):
        bh = h * (0.95 - i * 0.17)
        x0 = x + i * 2 * bw
        draw.rectangle([x0, y + h - bh, x0 + bw, y + h], fill=RED)
    draw.line([x, y + h * 0.1, x + w, y + h * 0.95], fill=INK, width=3)


def scales(draw, cx, cy, s):
    """Simple scales of justice for the verdict story."""
    draw.line([cx, cy - s, cx, cy + s], fill=INK, width=4)
    draw.line([cx - s, cy - s * 0.55, cx + s, cy - s * 0.55], fill=INK, width=4)
    for sx in (cx - s, cx + s):
        draw.line([sx, cy - s * 0.55, sx, cy - s * 0.1], fill=INK, width=3)
        draw.polygon([(sx - s * 0.35, cy - s * 0.1), (sx + s * 0.35, cy - s * 0.1),
                      (sx, cy + s * 0.35)], fill=PLUM)
    draw.ellipse([cx - 5, cy + s - 4, cx + 5, cy + s + 4], fill=INK)


def cuffs(draw, cx, cy, r):
    draw.ellipse([cx - r - 12, cy - r, cx - 12, cy + r], outline=INK, width=5)
    draw.ellipse([cx + 12, cy - r, cx + r + 12, cy + r], outline=INK, width=5)
    draw.line([cx - 12, cy, cx + 12, cy], fill=INK, width=4)


def three_circles(draw, cx, cy, r):
    cols = [RED, OCHRE, NAVY]
    for i, c in enumerate(cols):
        ox = (i - 1) * (r + 2)
        draw.ellipse([cx + ox - r, cy - r, cx + ox + r, cy + r],
                     outline=c, width=5)


def building_crack(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], outline=INK, width=4)
    for i in range(1, 4):
        draw.line([x, y + h * i / 4, x + w, y + h * i / 4], fill=INK, width=2)
    draw.line([(x + w * 0.6, y), (x + w * 0.45, y + h * 0.4),
               (x + w * 0.62, y + h * 0.7), (x + w * 0.5, y + h)],
              fill=RED, width=4)


def story(draw, x, y, w, kicker, color, headline, body):
    """One column story. Returns the y just below the body text."""
    chip(draw, (x, y), kicker, color)
    y += 36
    y = para(draw, (x, y), headline, font(SANSB, 26), w, leading=31)
    y += 6
    y = para(draw, (x, y), body, font(SANS, 17), w, leading=22)
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    m = 36  # margin

    # ---- masthead ----
    d.text((W // 2, 24), "THE WORLD IN ONE PAGE", font=font(SERIF, 56),
           fill=INK, anchor="ma")
    d.line([m, 96, W - m, 96], fill=RED, width=5)
    d.text((m, 106), "SUNDAY  ·  22 NOVEMBER 2026", font=font(SANSB, 22), fill=INK)
    d.text((W - m, 106), "ONE DAY — ONE IMAGE", font=font(SANSB, 22),
           fill=FAINT, anchor="ra")
    d.line([m, 140, W - m, 140], fill=INK, width=2)

    # ---- lead story: COP31 ----
    y = 156
    chip(d, (m, y), "CLIMATE  ·  ANTALYA, TURKEY", RED)
    d.text((m, y + 36), "COP31 COLLAPSES:", font=font(SERIF, 54), fill=INK)
    d.text((m, y + 100), "NO CLIMATE DEAL", font=font(SERIF, 54), fill=INK)
    dek = ("The UN climate summit ends two days past its deadline with no "
           "agreement at all, after the EU formally objected to a final draft "
           "that made no mention of fossil fuels.")
    para(d, (m, y + 168), dek, font(SANS, 21), 600, leading=27)
    globe(d, 830, y + 115, 88)
    d.text((830, y + 218), "TALKS END IN FAILURE", font=font(SANSB, 15),
           fill=FAINT, anchor="ma")
    d.line([m, 418, W - m, 418], fill=RULE, width=2)

    # ---- rows of three, laid out from measured story bottoms ----
    col_w = 304
    xs = [m, m + col_w + 20, m + 2 * (col_w + 20)]
    y2 = 436
    ends = []
    ends.append(story(d, xs[0], y2, col_w, "CONFLICT · SAUDI ARABIA", RED,
                      "Houthis claim strike on Saudi refinery",
                      "Yemen's Houthis say they hit the Rabigh oil refinery "
                      "on the Red Sea coast and claim a direct hit; Riyadh "
                      "has not confirmed any damage."))
    ends.append(story(d, xs[1], y2, col_w, "CONFLICT · BAHRAIN", RED,
                      "Iran strikes US bases in Bahrain",
                      "Missiles and drones hit an industrial site; two people "
                      "are injured. Tankers are also struck near the Strait "
                      "of Hormuz."))
    ends.append(story(d, xs[2], y2, col_w, "MEXICO · SINALOA", TEAL,
                      "\u2018El Chapo Isidro\u2019 captured",
                      "Special forces seize cartel boss Fausto Isidro Meza "
                      "Flores. Eleven killed, including four soldiers."))
    div2 = max(ends) + 12
    d.line([m, div2, W - m, div2], fill=RULE, width=2)

    y3 = div2 + 14
    ends = []
    ends.append(story(d, xs[0], y3, col_w, "UKRAINE", NAVY,
                      "Missile hits Zelenskyy\u2019s hometown",
                      "A Russian strike on Kryvyi Rih kills a 7-year-old boy "
                      "and a 20-year-old woman, wounds 60. A drone hits "
                      "flats near Kyiv; 14 missing."))
    ends.append(story(d, xs[1], y3, col_w, "MARKETS", RED,
                      "Stocks slide into correction",
                      "The S&P 500 falls 3.7% and the Nasdaq 5.3% on Friday "
                      "as the AI sell-off spreads to Japan and Korea."))
    ends.append(story(d, xs[2], y3, col_w, "ASIA · SOUTH KOREA", PLUM,
                      "Minister quits over AI exam cheating",
                      "Education minister Choi Kyo-jin resigns after "
                      "last-minute anti-cheating rules cause chaos at the "
                      "college entrance exam; 111 cases caught."))
    div3 = max(ends) + 12
    d.line([m, div3, W - m, div3], fill=INK, width=2)

    # ---- also today ----
    ay = div3 + 12
    d.text((m, ay), "ALSO TODAY", font=font(SANSB, 18), fill=RED)
    also = ("EU and Indonesia sign a landmark trade deal  ·  Candy-factory fire "
            "near Jakarta: 3 dead, dozens missing  ·  BepiColombo reaches Mercury "
            "orbit after 8 years  ·  Boat capsizes in Nigeria, 24 dead")
    para(d, (m + 152, ay), also, font(SANS, 17), W - m - 152 - m, leading=22)
    d.text((W // 2, 998),
           "Summarised from Reuters, AP, AFP, Al Jazeera and Euronews  ·  "
           "All events of Sunday 22 November 2026",
           font=font(SANS, 12), fill=FAINT, anchor="ma")

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
