# PULSE / CONCEPT 04

Big, loud, glanceable - the Fastrack youth entry. Category: **Fitness & Metrics**.
Canvas: 466 x 466 round.

## Design notes

- An oversized gradient ring in Zone B fills with daily step-goal progress
  (electric violet -> hot coral, 84% shown). Ring gaps at 12 / 3 / 6 / 9 keep
  it readable and snap to the grid.
- Time is Archivo Black, bottom-weighted so the ring owns the top half.
- Three pill chips along the bottom curve carry steps / calories / heart rate:
  25 px icon + 21 px value, nothing else.
- Palette: 60 near-black, 30 ring gradient, 10 white-hot accent on the time.
- AOD state: ring drops to a dim 3 px outline, time only.

## Rules compliance

- All text >= 21 px; icons 25 px. Ring is Zone B decoration; time and chips
  sit inside Zone A. No logos. Fonts are SIL OFL.

## Fonts

- **Archivo Black**, SIL OFL - https://fonts.google.com/specimen/Archivo+Black
- **Space Grotesk**, SIL OFL - https://fonts.google.com/specimen/Space+Grotesk

## Files

- `PULSE-face-466.png` / `PULSE-face-466-2x.png` - active face, 1x and 2x.
- `PULSE-face-AOD-2x.png` - always-on state.
- `PULSE-source.html` / `PULSE-source-AOD.html` - self-contained SVG source
  (fonts embedded).
- `PULSE-generator.py` - the generator that writes the HTML source.

## Re-render

```bash
python3 PULSE-generator.py   # adjust the font paths at the top first
google-chrome --headless=new --default-background-color=00000000 \
  --window-size=466,466 --force-device-scale-factor=2 \
  --screenshot=PULSE-face-466-2x.png "file://$PWD/PULSE-source.html"
```
