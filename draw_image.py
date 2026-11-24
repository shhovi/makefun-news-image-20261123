#!/usr/bin/env python3
"""Poster for Monday 23 November 2026 — built at build time with Pillow.

The day's four lead stories (all happened or first reported 23 Nov 2026):
  * COP31 in Antalya collapsed on Sunday without an overarching deal;
    the EU and others rejected a draft with no fossil-fuel phase-out.
    (AP / Reuters / Al Jazeera, reported 23 Nov 2026)
  * Ukraine said Monday its sea drones sank the Russian corvette
    Merkury off Benghazi, Libya — seven naval drones, Zelenskyy said.
    (Reuters / AP, 23 Nov 2026)
  * Nvidia's board reinstated Jensen Huang as CEO on Monday, 11 days
    after he resigned; US stocks rebounded sharply, S&P 500 +4.82%.
    (AP / Reuters, 23 Nov 2026)
  * Democrats clinched at least 258 US House seats — the largest
    House majority for either party since 1992. (AP, 23 Nov 2026)
Ticker items: Russian strike on Dymer kills at least 11 (AP);
Iran vows to counter the US naval blockade (Reuters); Indonesia
candy-factory fire: 24 dead, ~30 missing (Xinhua); Liverpool
thrash Manchester United 4-0 (Reuters).

The shipped program is main.ts; it copies the finished entry.png to
/output at run time. Text is drawn here so every word stays exact.
"""
from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
PAPER = (250, 246, 236)
CARD = (255, 255, 255)
EDGE = (198, 194, 180)
TEXT = (26, 30, 40)
SUB = (74, 80, 94)
BANNER = (16, 40, 88)
GOLD = (255, 214, 90)
CRIMSON = (176, 32, 32)
FOREST = (16, 118, 60)
SKY = (58, 128, 198)
AMBER = (245, 160, 20)
STEEL = (92, 100, 117)
LAMP = (250, 215, 90)
FLAME = (240, 110, 30)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def fnt(path, px):
    return ImageFont.truetype(path, px)


def shrink(draw, s, limit, start, path=FB):
    px = start
    while px > 18:
        f = fnt(path, px)
        if draw.textlength(s, font=f) <= limit:
            return f
        px -= 2
    return fnt(path, px)


def centred(draw, cx, y, s, f, colour):
    draw.text((cx - draw.textlength(s, font=f) / 2, y), s, font=f, fill=colour)


def globe(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(30, 110, 200), outline=CARD, width=4)
    draw.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r], outline=CARD, width=3)
    draw.line([cx - r, cy, cx + r, cy], fill=CARD, width=3)
    draw.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55], 0, 180, fill=CARD, width=3)
    draw.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55], 180, 360, fill=CARD, width=3)


def glyph_cop(draw, ox, oy):
    # draft text with a big red X + thermometer
    draw.rectangle([ox + 6, oy + 8, ox + 92, oy + 110], fill=(245, 240, 225), outline=EDGE, width=2)
    for i, yy in enumerate(range(oy + 20, oy + 96, 12)):
        w = 70 if i % 2 == 0 else 52
        draw.line([ox + 14, yy, ox + 14 + w, yy], fill=STEEL, width=3)
    draw.line([ox + 16, oy + 22, ox + 84, oy + 98], fill=CRIMSON, width=7)
    draw.line([ox + 84, oy + 22, ox + 16, oy + 98], fill=CRIMSON, width=7)
    # thermometer
    tx = ox + 122
    draw.rounded_rectangle([tx - 9, oy + 12, tx + 9, oy + 84], radius=9, fill=CARD, outline=TEXT, width=3)
    draw.rectangle([tx - 4, oy + 40, tx + 4, oy + 82], fill=CRIMSON)
    draw.ellipse([tx - 14, oy + 78, tx + 14, oy + 106], fill=CRIMSON, outline=TEXT, width=3)
    for yy in (oy + 26, oy + 42, oy + 58):
        draw.line([tx + 9, yy, tx + 17, yy], fill=TEXT, width=2)


def glyph_warship(draw, ox, oy):
    # sea + warship hull, listing, with a drone above
    sx, sy = ox + 8, oy + 78
    for i, wx in enumerate(range(sx, sx + 150, 22)):
        draw.arc([wx - 12, sy, wx + 12, sy + 16], 0, 180, fill=SKY, width=4)
    # hull (tilted down to the right)
    draw.polygon([(ox + 22, oy + 66), (ox + 138, oy + 78), (ox + 128, oy + 96),
                  (ox + 34, oy + 88)], fill=(70, 76, 88), outline=TEXT, width=2)
    # superstructure
    draw.polygon([(ox + 52, oy + 44), (ox + 84, oy + 48), (ox + 84, oy + 68),
                  (ox + 52, oy + 66)], fill=(110, 116, 128), outline=TEXT, width=2)
    draw.line([ox + 66, oy + 44, ox + 66, oy + 30], fill=TEXT, width=3)
    draw.line([ox + 58, oy + 30, ox + 76, oy + 30], fill=TEXT, width=3)
    # smoke rising from the mast, not floating off the hull
    for (px, py, pr) in ((ox + 62, oy + 20, 8), (ox + 74, oy + 8, 11), (ox + 90, oy + 2, 8)):
        draw.ellipse([px - pr, py - pr, px + pr, py + pr], fill=(150, 150, 155))
    # drone top-left
    dx, dy = ox + 34, oy + 16
    draw.line([dx - 20, dy - 9, dx + 20, dy + 9], fill=TEXT, width=3)
    draw.line([dx + 20, dy - 9, dx - 20, dy + 9], fill=TEXT, width=3)
    for (rx, ry) in ((-20, -9), (20, -9), (-20, 9), (20, 9)):
        draw.ellipse([dx + rx - 8, dy + ry - 3, dx + rx + 8, dy + ry + 3], outline=TEXT, width=2)
    draw.rectangle([dx - 8, dy - 6, dx + 8, dy + 6], fill=CRIMSON, outline=TEXT, width=2)
    # blast star on the hull
    draw.polygon([(ox + 96, oy + 52), (ox + 104, oy + 66), (ox + 88, oy + 66)], fill=FLAME)


def glyph_stocks(draw, ox, oy):
    # bar chart + rising trend line with arrowhead, green
    bx, by = ox + 14, oy + 96
    heights = (34, 52, 30, 66, 58, 88)
    for i, h in enumerate(heights):
        x = bx + i * 22
        draw.rectangle([x, by - h, x + 16, by], fill=(150, 190, 150), outline=FOREST, width=2)
    pts = [(ox + 16, oy + 88), (ox + 44, oy + 66), (ox + 66, oy + 74),
           (ox + 92, oy + 44), (ox + 118, oy + 50), (ox + 146, oy + 16)]
    draw.line(pts, fill=FOREST, width=6, joint="curve")
    ax, ay = pts[-1]
    draw.polygon([(ax, ay - 4), (ax + 16, ay + 2), (ax + 2, ay + 12)], fill=FOREST)
    # "+4.82%" tag (wide enough for the full text at 20px bold)
    draw.rounded_rectangle([ox + 86, oy + 72, ox + 168, oy + 102], radius=8,
                           fill=FOREST, outline=TEXT, width=2)
    draw.text((ox + 93, oy + 77), "+4.82%", font=fnt(FB, 20), fill=CARD)


def glyph_capitol(draw, ox, oy):
    # US Capitol dome + columns
    cx = ox + 80
    # base steps
    draw.rectangle([ox + 18, oy + 96, ox + 142, oy + 104], fill=(200, 195, 180), outline=TEXT, width=2)
    draw.rectangle([ox + 26, oy + 88, ox + 134, oy + 96], fill=(220, 215, 200), outline=TEXT, width=2)
    # columns
    for i in range(5):
        x = ox + 34 + i * 22
        draw.rectangle([x, oy + 56, x + 10, oy + 88], fill=CARD, outline=TEXT, width=2)
    # entablature
    draw.rectangle([ox + 28, oy + 46, ox + 132, oy + 56], fill=(220, 215, 200), outline=TEXT, width=2)
    # dome
    draw.pieslice([cx - 30, oy + 2, cx + 30, oy + 62], 180, 360, fill=(120, 150, 190), outline=TEXT, width=2)
    draw.rectangle([cx - 32, oy + 40, cx + 32, oy + 48], fill=(120, 150, 190), outline=TEXT, width=2)
    # flag on top
    draw.line([cx, oy + 2, cx, oy - 14], fill=TEXT, width=3)
    draw.polygon([(cx, oy - 14), (cx + 16, oy - 10), (cx, oy - 6)], fill=CRIMSON)
    # "258" tag (wide enough for the full text at 20px bold)
    draw.rounded_rectangle([ox + 116, oy + 66, ox + 168, oy + 96], radius=8,
                           fill=BANNER, outline=TEXT, width=2)
    draw.text((ox + 124, oy + 71), "258", font=fnt(FB, 20), fill=CARD)


STORIES = [
    ("COP31 \u00b7 ANTALYA", FOREST, "Climate talks end, no deal",
     ["EU rejects draft with no", "fossil-fuel phase-out."], glyph_cop),
    ("BENGHAZI, LIBYA", CRIMSON, "Ukraine sinks Russian warship",
     ["Zelenskyy: 7 sea drones sank", "corvette Merkury off Libya."], glyph_warship),
    ("WALL STREET", FOREST, "Nvidia chief back; stocks soar",
     ["Huang reinstated as CEO;", "S&P 500 jumps 4.82% Monday."], glyph_stocks),
    ("WASHINGTON, D.C.", BANNER, "Democrats win record majority",
     ["At least 258 seats \u2014 largest", "House majority since 1992."], glyph_capitol),
]


def card(draw, rect, story):
    kicker, band, headline, sublines, glyph = story
    x0, y0, x1, y1 = rect
    room = (x1 - x0) - 44
    draw.rounded_rectangle(rect, radius=18, fill=CARD, outline=EDGE, width=3)
    draw.rounded_rectangle([x0, y0, x1, y0 + 46], radius=18, fill=band)
    draw.rectangle([x0, y0 + 30, x1, y0 + 46], fill=band)
    draw.text((x0 + 22, y0 + 8), kicker, font=shrink(draw, kicker, room, 27), fill=CARD)
    glyph(draw, x0 + 24, y0 + 58)
    draw.text((x0 + 22, y0 + 182), headline,
              font=shrink(draw, headline, room, 38), fill=TEXT)
    yy = y0 + 232
    for s in sublines:
        draw.text((x0 + 22, yy), s, font=shrink(draw, s, room, 30, FR), fill=SUB)
        yy += 38


def build():
    img = Image.new("RGB", (SIZE, SIZE), PAPER)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, SIZE, 168], fill=BANNER)
    globe(d, 86, 84, 52)
    centred(d, 560, 18, "WORLD NEWS", fnt(FB, 74), CARD)
    centred(d, 560, 102, "Monday  \u2022  23 November 2026", fnt(FB, 42), GOLD)
    d.rectangle([0, 168, SIZE, 174], fill=GOLD)

    margin, gap, top = 28, 16, 184
    pw = (SIZE - 2 * margin - gap) // 2
    ph = 330
    spots = [
        [margin, top, margin + pw, top + ph],
        [margin + pw + gap, top, SIZE - margin, top + ph],
        [margin, top + ph + gap, margin + pw, top + 2 * ph + gap],
        [margin + pw + gap, top + ph + gap, SIZE - margin, top + 2 * ph + gap],
    ]
    for rect, story in zip(spots, STORIES):
        card(d, rect, story)

    fy = top + 2 * ph + 2 * gap
    d.rounded_rectangle([margin, fy, SIZE - margin, SIZE - 24], radius=16, fill=TEXT)
    t1 = "ALSO: Dymer strike kills at least 11  \u2022  Iran vows to counter US blockade"
    t2 = "Indonesia factory fire: 24 dead  \u2022  Liverpool 4\u20130 Man Utd"
    centred(d, SIZE // 2, fy + 14, t1, shrink(d, t1, SIZE - 2 * margin - 40, 29), CARD)
    centred(d, SIZE // 2, fy + 58, t2, shrink(d, t2, SIZE - 2 * margin - 40, 29), GOLD)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    build()
