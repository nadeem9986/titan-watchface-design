# GBD-R / CONCEPT 01

A round-dial watch face concept for the Titan Smart / Fastrack Smart Watch Face
Design Challenge 2026 ("Design Time Your Way"). Canvas: 466 x 466 round
(Titan Celestor / Fastrack Astor FR2 Pro class AMOLED).

**Inspiration:** the Casio GBD-200 (G-Shock square MIP digital), converted to
round. The square-to-round translation is the whole design exercise.

## Design decisions

- **Square-to-round translation:** the GBD-200's stacked LCD blocks (date top,
  huge time centre, data bottom) were re-architected onto the challenge's
  30-degree radial grid - 60 minute ticks in the outer Zone B ring, a hairline
  inner ring that echoes the GBD-200's LCD frame, and date / time /
  complications stacked on the vertical axis inside Zone A. Nothing is a
  squeezed square grid; the composition is centre-aligned per the kit.
- **Monochrome as the 60-30-10 rule:** instead of three hues, the split is done
  in pure value - black dial (60%), grey structure/readouts (30%), white-hot
  time (10%). It reads as MIP-LCD, is maximally glanceable, and the all-black
  AOD state doubles as a real OLED battery-saving mode.
- **Typography as texture:** Departure Mono's bitmap flavour mimics
  segment-display numerals while staying crisp vector, so the font itself
  carries the G-Shock MIP reference. The seconds field is demoted to a small
  readout right of the minutes, exactly like the GBD-200's hierarchy, keeping
  one focal point (the time) for the 1-2 second glance.

## Rules compliance

- All text >= 21 px (time 96, seconds 28, date 24, complications 23); icons ~28 px (> 25 floor).
- Time + data inside Zone A; decoration (minute ticks) only in Zone B; components snap to the 30-degree grid.
- No brand logos anywhere.
- Font is free for commercial use (SIL OFL, license included).

## Font

**Departure Mono** v1.500 by Helena Zhang / rektdeckard, SIL Open Font License 1.1.
- Source: https://github.com/rektdeckard/departure-mono
- Files: `DepartureMono-Regular.otf`, `DepartureMono-LICENSE.txt`

## Files

- `GBD-R-hero.png` - 1200 x 1200 presentation mock on a dark scene.
- `GBD-R-face-466.png` - the active face at spec size (466 x 466, transparent corners).
- `GBD-R-face-466-2x.png` - 932 px (2x export, per the submission handbook).
- `GBD-R-face-AOD-2x.png` - always-on / ambient state, 932 px.
- `GBD-R-source.html` / `GBD-R-source-AOD.html` - self-contained SVG source with the
  font embedded as base64; opens in any browser.
- `GBD-R-generator.py` - the Python generator that writes the HTML source
  (all geometry is computed; demo values like time/date/steps/battery are one-line edits).

## Re-render

```bash
python3 GBD-R-generator.py        # writes face.html and face_aod.html
google-chrome --headless=new --default-background-color=00000000 \
  --window-size=466,466 --force-device-scale-factor=2 \
  --screenshot=face_2x.png "file://$PWD/face.html"
```

The generator expects the Departure Mono woff2 at
`depmono/DepartureMono-1.500/DepartureMono-Regular.woff2` (adjust the path at
the top of the script, or re-download v1.500 from the font repo above).
