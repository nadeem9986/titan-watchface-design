# HERITAGE / CONCEPT 03

Classic Titan dress-watch DNA on a smart display. Category: **Luxury Analog**.
Canvas: 466 x 466 round.

## Design notes

- Deep charcoal radial-gradient dial; 12 hairline gold indices on the
  30-degree grid; no numerals except a single applied "12".
- Slim dauphine hour/minute hands in ivory; needle second hand in warm gold
  (the single accent, 10% per the 60-30-10 rule).
- One complication only: a subdial at 6 o'clock carrying day + date.
  Restraint is the concept.
- A minimal gold battery arc sits inside the outer minute track.
- Palette: 60 charcoal black, 30 warm ivory, 10 brushed gold.
- AOD state: dim indices and hands only, second hand off, pure black dial.

## Rules compliance

- Text >= 21 px ("12" at 32, subdial date at 21). No logos.
- Font is SIL OFL (free for commercial use).

## Font

**Cormorant Garamond** 500, SIL OFL - https://fonts.google.com/specimen/Cormorant+Garamond

## Files

- `HERITAGE-face-466.png` / `HERITAGE-face-466-2x.png` - active face, 1x and 2x.
- `HERITAGE-face-AOD-2x.png` - always-on state.
- `HERITAGE-source.html` / `HERITAGE-source-AOD.html` - self-contained SVG
  source (font embedded).
- `HERITAGE-generator.py` - the generator that writes the HTML source.

## Re-render

```bash
python3 HERITAGE-generator.py   # adjust the font path at the top first
google-chrome --headless=new --default-background-color=00000000 \
  --window-size=466,466 --force-device-scale-factor=2 \
  --screenshot=HERITAGE-face-466-2x.png "file://$PWD/HERITAGE-source.html"
```
