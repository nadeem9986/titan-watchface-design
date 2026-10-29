# ORBIT / CONCEPT 05

Complications as satellites on fixed orbits - the 30-degree grid made visible
as the design itself. Category: **Abstract Art**. Canvas: 466 x 466 round.

## Design notes

- Faint concentric orbit rings etched across the dial. Each complication is a
  small dot on its orbit at a grid position; the dot's fill arc encodes its
  value (battery literally drains, steps fill toward goal).
- Four dots: battery (outer orbit, 2 o'clock), steps (mid orbit, 5 o'clock),
  heart rate (inner orbit, 8 o'clock), sleep (inner orbit, 11 o'clock).
- Time is Space Grotesk 500 at 88 px, centred, with the date directly beneath.
- Interaction story for the concept note: dots brighten in sequence on wake,
  like a system coming online.
- Palette: 60 midnight blue-black, 30 desaturated slate orbits, 10 signal
  blue for the dot fills.
- AOD state: orbits nearly invisible, dim time only.

## Rules compliance

- Text >= 21 px. Time + date inside Zone A. No logos. Font is SIL OFL.

## Font

**Space Grotesk**, SIL OFL - https://fonts.google.com/specimen/Space+Grotesk

## Files

- `ORBIT-face-466.png` / `ORBIT-face-466-2x.png` - active face, 1x and 2x.
- `ORBIT-face-AOD-2x.png` - always-on state.
- `ORBIT-source.html` / `ORBIT-source-AOD.html` - self-contained SVG source
  (font embedded).
- `ORBIT-generator.py` - the generator that writes the HTML source.

## Re-render

```bash
python3 ORBIT-generator.py   # adjust the font path at the top first
google-chrome --headless=new --default-background-color=00000000 \
  --window-size=466,466 --force-device-scale-factor=2 \
  --screenshot=ORBIT-face-466-2x.png "file://$PWD/ORBIT-source.html"
```
