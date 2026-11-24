#!/usr/bin/env python3
"""Compose the entry image for make.fun's news-image-20261124 bounty.

Draws a one-page newspaper front page that sums up the world news of
Tuesday 24 November 2026, as reported on the day (Reuters, AP, WSJ and
CNN wires; The Daily Edition No. 279 of 24 Nov 2026; the day's digests).
Every story was cross-checked in at least two independent sources, and
each is an event of 23-24 November 2026 (the US stories broke on Monday
afternoon US time, which is Tuesday across the Pacific and Asia):

  lead   Nvidia's board votes unanimously to reinstate co-founder
         Jensen Huang as CEO, 11 days after his resignation, after
         President Trump pressed for his return; Trump calls him a
         "national treasure", Nvidia shares leap about a third and
         Democrats vow an inquiry (Reuters, AP, WSJ, CNN, Barron's).
  panel  The UN seeks a probe after Ukraine says seven naval drones
         sank the Russian corvette Merkury at Benghazi, Libya, and
         warns Libya must not become a battleground (Daily Edition,
         iqmia world summary, lamediterranee wires).
  panel  Russia probes NATO's skies: 25 airspace violations in 2026,
         four times the 2024 count; Chancellor Merz tells the Kremlin
         to end its provocations (The Conversation via Daily Edition,
         lamediterranee, annagranules).
  panel  COP31 in Antalya collapses: more than 90 nations reject a
         final text that never names fossil fuels, ending the longest
         climate summit in history in failure (Grist via Daily Edition,
         iqmia, lamediterranee).
  panel  Virginia and Oregon sue SpaceX, alleging it profited as its
         Grok AI made sexual images of children - the first state
         suits of their kind (Reuters, Engadget, NY Post).
  panel  A study of leaked government data puts Russia's war dead
         near 700,000; Ukrainian drones set the Novoshakhtinsk oil
         refinery ablaze (Kyiv Independent, annagranules).
  panel  Manchester: about 12,000 fans are evacuated from a Don
         Toliver concert after an unknown substance fills the air at
         the arena, nine years after the bombing there (autoys,
         annagranules global wires).
  strip  Oil falls 3% as Middle East shipments rise; UN talks on
         "killer robots" end with no accord; Melat Kiros, 29, becomes
         the first Gen Z woman in the US Congress; Houthis say a Saudi
         strike killed 17 in Hodeida.

Everything is drawn with PIL shapes and real fonts, so every word stays
crisp - no generated raster text anywhere. Output: entry.png, 1024x1024.

Layout revision (2026-11-24): three panel standfirsts shortened to two
lines each so no text touches a cell rule, and the share-price label
taken out of the lead illustration, where it collided with the chip's
pins - the rising line alone now carries the market move.
"""

from PIL import Image, ImageDraw, ImageFont

W = 1024
PAPER = (248, 245, 238)
INK = (20, 24, 29)
NAVY = (29, 53, 87)
RED = (179, 52, 31)
GOLD = (201, 147, 43)
GREEN = (46, 160, 90)
PANEL_LINE = (198, 192, 178)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, W), PAPER)
d = ImageDraw.Draw(img)

M = 36  # page margin


def centered(text, y, fnt, fill=INK):
    box = d.textbbox((0, 0), text, font=fnt)
    d.text(((W - (box[2] - box[0])) / 2, y), text, font=fnt, fill=fill)


def wrap(text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if d.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- masthead
d.line([(M, 26), (W - M, 26)], fill=INK, width=5)
d.line([(M, 34), (W - M, 34)], fill=INK, width=2)
centered("THE WORLD IN ONE DAY", 44, font(SERIF_B, 55))
d.line([(M, 122), (W - M, 122)], fill=INK, width=2)
d.line([(M, 128), (W - M, 128)], fill=INK, width=5)

# ---------------------------------------------------------------- date band
d.rectangle([M, 142, W - M, 208], fill=NAVY)
centered("TUESDAY  24 NOVEMBER 2026", 156, font(SANS_B, 43), fill=(255, 255, 255))

# ---------------------------------------------------------------- lead story
LY = 226
# illustration: a GPU chip on a dark board, a rising share-price line
d.rectangle([M, LY, M + 296, LY + 196], fill=(15, 20, 28))
# circuit traces running off the chip
for tx, ty, horiz in [(18, 40, 52), (18, 156, 52), (244, 40, 34), (244, 156, 34)]:
    if tx < 100:
        d.line([(M + tx, LY + ty), (M + tx + horiz, LY + ty)], fill=(52, 68, 92), width=3)
        d.ellipse([M + tx - 4, LY + ty - 4, M + tx + 4, LY + ty + 4], fill=(90, 110, 140))
    else:
        d.line([(M + tx, LY + ty), (M + tx + horiz, LY + ty)], fill=(52, 68, 92), width=3)
        d.ellipse([M + tx + horiz - 4, LY + ty - 4, M + tx + horiz + 4, LY + ty + 4], fill=(90, 110, 140))
# the chip: outer package, gold pins, inner die
CX0, CY0, CX1, CY1 = M + 96, LY + 30, M + 200, LY + 134
for i in range(5):  # pins, top and bottom
    px = CX0 + 12 + i * 20
    d.rectangle([px, CY0 - 10, px + 9, CY0], fill=GOLD)
    d.rectangle([px, CY1, px + 9, CY1 + 10], fill=GOLD)
for i in range(4):  # pins, left and right
    py = CY0 + 14 + i * 24
    d.rectangle([CX0 - 10, py, CX0, py + 9], fill=GOLD)
    d.rectangle([CX1, py, CX1 + 10, py + 9], fill=GOLD)
d.rectangle([CX0, CY0, CX1, CY1], fill=(38, 48, 64))
d.rectangle([CX0 + 26, CY0 + 26, CX1 - 26, CY1 - 26], fill=(24, 32, 46))
d.rectangle([CX0 + 38, CY0 + 38, CX1 - 38, CY1 - 38], fill=(64, 84, 112))
# rising line across the foot of the board, with an arrowhead
pts = [(M + 16, LY + 178), (M + 84, LY + 164), (M + 140, LY + 170),
       (M + 204, LY + 148), (M + 268, LY + 122)]
d.line(pts, fill=GREEN, width=5)
d.polygon([(M + 268, LY + 122), (M + 250, LY + 124), (M + 262, LY + 138)], fill=GREEN)

LX = M + 320
d.text((LX, LY - 4), "THE LEAD STORY · SILICON VALLEY", font=font(SANS_B, 19), fill=RED)
lead_head = wrap("JENSEN HUANG IS BACK AT NVIDIA", font(SANS_B, 41), W - M - LX)
yy = LY + 26
for line in lead_head:
    d.text((LX, yy), line, font=font(SANS_B, 41), fill=INK)
    yy += 50
lead_sub = ("Eleven days after he resigned, Nvidia's board votes unanimously to restore "
            "its co-founder. Trump pressed for his return and calls him a “national treasure.”")
for line in wrap(lead_sub, font(SANS, 21), W - M - LX):
    d.text((LX, yy + 4), line, font=font(SANS, 21), fill=(52, 56, 62))
    yy += 29

d.line([(M, 446), (W - M, 446)], fill=INK, width=3)

# ---------------------------------------------------------------- panels
panels = [
    ("LIBYA · UKRAINE AT SEA", NAVY,
     "UN SEEKS PROBE OF BENGHAZI STRIKE",
     "Kyiv says its drones sank a Russian corvette; UN warns Libya must not be a battleground."),
    ("NATO · THE EASTERN FLANK", RED,
     "RUSSIA PROBES NATO'S SKIES",
     "25 Russian airspace violations this year, four times 2024's count; Berlin warns the Kremlin off."),
    ("CLIMATE · ANTALYA", GOLD,
     "COP31 COLLAPSES OVER FOSSIL FUELS",
     "Over 90 nations reject a text that never names fossil fuels; the longest summit fails."),
    ("US COURTS · AI SAFETY", NAVY,
     "STATES SUE SPACEX OVER GROK",
     "Virginia and Oregon sue, alleging Grok made sexual images of children — the first suits of their kind."),
    ("UKRAINE WAR · THE TOLL", RED,
     "RUSSIA'S WAR DEAD NEAR 700,000",
     "A study of leaked data puts the toll near 700,000; Ukraine's drones set a refinery ablaze."),
    ("MANCHESTER · THE HUMAN STORY", GOLD,
     "12,000 FANS FLEE ARENA CONCERT",
     "A Don Toliver show is halted as an unknown substance fills the air at the arena."),
]

GX, GY = M, 462
CW, CH = (W - 2 * M - 20) // 2, 150
for i, (kicker, kc, head, sub) in enumerate(panels):
    x = GX + (i % 2) * (CW + 20)
    y = GY + (i // 2) * (CH + 9)
    # ruled cell: top and bottom rules make the grid read as columns
    d.line([(x, y), (x + CW, y)], fill=PANEL_LINE, width=2)
    d.line([(x, y + CH - 2), (x + CW, y + CH - 2)], fill=PANEL_LINE, width=2)
    d.text((x + 2, y + 9), kicker, font=font(SANS_B, 17), fill=kc)
    hy = y + 36
    for line in wrap(head, font(SANS_B, 25), CW - 4):
        d.text((x + 2, hy), line, font=font(SANS_B, 25), fill=INK)
        hy += 30
    for line in wrap(sub, font(SANS, 18), CW - 4):
        d.text((x + 2, hy + 2), line, font=font(SANS, 18), fill=(52, 56, 62))
        hy += 24

# ---------------------------------------------------------------- bottom strip
BY = 940
d.rectangle([M, BY, W - M, 996], fill=INK)
strip = ("ALSO TUESDAY: Oil falls 3% as Mideast shipments rise · UN “killer robot” talks end with no accord · "
         "Melat Kiros, 29, first Gen Z woman in Congress · Houthis say Saudi strike killed 17")
sy = BY + 9
for line in wrap(strip, font(SANS_B, 16), W - 2 * M - 24):
    box = d.textbbox((0, 0), line, font=font(SANS_B, 16))
    d.text(((W - (box[2] - box[0])) / 2, sy), line, font=font(SANS_B, 16), fill=(240, 236, 224))
    sy += 22

img.save("entry.png", optimize=True)
print("wrote entry.png", img.size)
