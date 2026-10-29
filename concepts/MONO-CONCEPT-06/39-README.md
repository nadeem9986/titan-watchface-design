# MONO / CONCEPT 06

Grey/white/black only - the anti-everything face. Category: **Minimalist**.
Canvas: 466 x 466 round.

## Design notes

- Matte black dial, one oversized light-grey Departure Mono time (100 px) -
  the pixel texture reads beautifully at 2x export - with the date in
  letterspaced small caps beneath.
- Complications are invisible until needed: four icon-only slots at the
  diagonals (weather, battery, steps, heart rate), white line icons at 25 px,
  no numbers unless a value is abnormal (e.g. battery under 20% shows the
  number - mention this behaviour in the concept note).
- The only motion on the face: a 1 px white tick travels the outer edge once
  per minute (shown at the 8-minute position).
- Palette: 60 black, 30 grey structure, 10 white. 60-30-10 in pure value steps.
- AOD state: dim grey time on black, nothing else.

## Rules compliance

- Text >= 21 px; icons 25 px. No logos. Font is SIL OFL.

## Font

**Departure Mono** v1.500, SIL OFL - https://github.com/rektdeckard/departure-mono
(OTF + license ship in `concepts/GBD-R-CONCEPT-01/`).

## Files

- `MONO-face-466.png` / `MONO-face-466-2x.png` - active face, 1x and 2x.
- `MONO-face-AOD-2x.png` - always-on state.
- `MONO-source.html` / `MONO-source-AOD.html` - self-contained SVG source
  (font embedded).
- `MONO-generator.py` - the generator that writes the HTML source.

## Re-render

```bash
python3 MONO-generator.py   # adjust the font path at the top first
google-chrome --headless=new --default-background-color=00000000 \
  --window-size=466,466 --force-device-scale-factor=2 \
  --screenshot=MONO-face-466-2x.png "file://$PWD/MONO-source.html"
```
