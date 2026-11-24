"""Draw the 23 November 2026 world-news poster (1024x1024 PNG).

One canvas, four stories in a 2x2 grid, a header naming the day and a
ticker of the day's other headlines along the bottom. Run it and it
writes entry.png next to this file.
"""

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
OUT = "entry.png"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (12, 26, 46)
NAVY_SOFT = (28, 48, 74)
GOLD = (232, 184, 75)
CARD = (248, 250, 253)
INK = (16, 30, 51)
BODY = (51, 65, 90)
MUTED = (120, 133, 153)
LINE = (213, 221, 232)
TICKER_BG = (20, 24, 33)
RED = (178, 34, 34)
WHITE = (255, 255, 255)


def load(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REGULAR, size)


def wrap(draw, text, font, width):
    """Split text into lines that fit inside width pixels."""
    lines, current = [], ""
    for word in text.split(" "):
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=font) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_panel(draw, x, y, w, h, number, accent, kicker, headline, body, tag):
    # soft drop shadow, then the card itself
    draw.rounded_rectangle([x, y + 5, x + w, y + h + 5], radius=18, fill=(7, 15, 27))
    draw.rounded_rectangle([x, y, x + w, y + h], radius=18, fill=CARD)
    # short coloured dash above the kicker
    draw.rounded_rectangle([x + 24, y + 24, x + 86, y + 32], radius=4, fill=accent)
    # story number in a filled circle, top right
    cx, cy, r = x + w - 46, y + 46, 21
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=accent)
    num = load(24, bold=True)
    tw = draw.textlength(str(number), font=num)
    draw.text((cx - tw / 2, cy - 17), str(number), font=num, fill=WHITE)
    # kicker: where the story happened
    kick = load(21, bold=True)
    draw.text((x + 24, y + 44), kicker, font=kick, fill=accent)
    # headline, up to two lines
    head = load(30, bold=True)
    lines = wrap(draw, headline, head, w - 48)[:2]
    ty = y + 78
    for line in lines:
        draw.text((x + 24, ty), line, font=head, fill=INK)
        ty += 36
    # divider
    draw.line([(x + 24, y + 164), (x + w - 24, y + 164)], fill=LINE, width=2)
    # body text, up to four lines
    body_font = load(23)
    blines = wrap(draw, body, body_font, w - 48)[:4]
    by = y + 180
    for line in blines:
        draw.text((x + 24, by), line, font=body_font, fill=BODY)
        by += 30
    # footer tag, bottom left
    tag_font = load(18, bold=True)
    draw.ellipse([x + 24, y + h - 34, x + 34, y + h - 24], fill=accent)
    draw.text((x + 42, y + h - 38), tag, font=tag_font, fill=MUTED)


def main():
    img = Image.new("RGB", (SIZE, SIZE), NAVY)
    draw = ImageDraw.Draw(img)

    # ---- header: masthead on the left, date block on the right ----
    mast = load(58, bold=True)
    draw.text((28, 34), "WORLD NEWS", font=mast, fill=WHITE)
    day_font = load(24, bold=True)
    date_font = load(30, bold=True)
    day = "MONDAY"
    date = "23 NOVEMBER 2026"
    draw.text((SIZE - 28 - draw.textlength(day, font=day_font), 38),
              day, font=day_font, fill=GOLD)
    draw.text((SIZE - 28 - draw.textlength(date, font=date_font), 68),
              date, font=date_font, fill=WHITE)
    draw.line([(28, 140), (SIZE - 28, 140)], fill=GOLD, width=3)
    sub = load(20)
    draw.text((28, 152), "The day in four stories",
              font=sub, fill=(150, 170, 198))

    # ---- four stories, 2 by 2 ----
    stories = [
        (1, (14, 124, 107), "COP31  ·  ANTALYA",
         "Climate talks end, no deal",
         "The UN climate summit in Antalya closed with no comprehensive "
         "deal, after the EU rejected a draft with no fossil-fuel phase-out.",
         "CLIMATE"),
        (2, (37, 99, 168), "BENGHAZI, LIBYA",
         "Ukraine sinks Russian warship",
         "President Zelenskyy said seven Ukrainian sea drones sank the "
         "Russian corvette Merkury off the coast near Benghazi.",
         "CONFLICT"),
        (3, (199, 138, 18), "WALL STREET",
         "Nvidia chief back; stocks soar",
         "Nvidia's board restored Jensen Huang as CEO, 11 days after he "
         "stepped down. The S&P 500 jumped 4.82%.",
         "MARKETS"),
        (4, (179, 38, 30), "WASHINGTON, D.C.",
         "Democrats win record majority",
         "Democrats secured at least 258 seats in the US House \u2014 "
         "their largest majority since 1992.",
         "POLITICS"),
    ]
    gx, gy, gap = 28, 186, 18
    pw = (SIZE - 2 * gx - gap) // 2
    ph = 340
    for i, (num, accent, kicker, head, body, tag) in enumerate(stories):
        px = gx + (i % 2) * (pw + gap)
        py = gy + (i // 2) * (ph + gap)
        draw_panel(draw, px, py, pw, ph, num, accent, kicker, head, body, tag)

    # ---- ticker: the rest of the day along the bottom ----
    draw.rounded_rectangle([28, 902, SIZE - 28, 996], radius=14, fill=TICKER_BG)
    chip = load(20, bold=True)
    label = "LATEST"
    lw = draw.textlength(label, font=chip)
    draw.rounded_rectangle([44, 918, 44 + lw + 28, 956], radius=8, fill=RED)
    draw.text((44 + 14, 926), label, font=chip, fill=WHITE)
    tick = load(21)
    tx = 44 + lw + 28 + 18
    draw.text((tx, 916),
              "Dymer strike kills at least 11  \u2022  Iran vows to defy US naval blockade",
              font=tick, fill=WHITE)
    draw.text((tx, 948),
              "Indonesia candy-factory fire: 24 dead  \u2022  Liverpool 4\u20130 Manchester United",
              font=tick, fill=WHITE)

    img.save(OUT, optimize=True)
    print(f"wrote {OUT} ({SIZE}x{SIZE})")


if __name__ == "__main__":
    main()
