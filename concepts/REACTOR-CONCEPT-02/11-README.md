# REACTOR / CONCEPT 02

A Tony Stark / JARVIS HUD translated to the wrist. Category: **Retro-Futuristic**.
Canvas: 466 x 466 round.

## Design notes

- True black dial. A thin cyan arc sweeps Zone B as a 60-second progress ring
  (the "arc reactor" charge ring); tick marks snap to the 30-degree grid.
- Time is Departure Mono at 80 px, dead centre - the bitmap flavour keeps it
  HUD, not theme-park. Under it a terminal line `> FRI 30 OCT` with a cyan
  block cursor.
- Four HUD readouts at 12 / 3 / 6 / 9 on the inner grid: weather, heart rate,
  battery, steps - each a 25 px line icon plus a mono value, no labels.
- Palette (60-30-10): 60 black, 30 graphite/cyan-grey structure, 10 electric
  cyan accent (the ring + cursor only).
- AOD state: ring drops to a 1 px dim amber arc, time only, everything else
  off - black everywhere means real OLED power savings.
- Judging-story detail: on wake the ring can do a 300 ms "boot" sweep before
  settling (describe this in the concept note).

## Rules compliance

- All text >= 21 px; icons 25 px. Time + data in Zone A; ring + ticks in Zone B.
- No logos. Font is SIL OFL (free for commercial use).

## Font

**Departure Mono** v1.500, SIL OFL - https://github.com/rektdeckard/departure-mono
(OTF + license ship in `concepts/GBD-R-CONCEPT-01/`).

## Files

- `REACTOR-face-466.png` / `REACTOR-face-466-2x.png` - active face, 1x and 2x.
- `REACTOR-face-AOD-2x.png` - always-on state.
- `REACTOR-source.html` / `REACTOR-source-AOD.html` - self-contained SVG source
  (font embedded); opens in any browser.
- `REACTOR-generator.py` - the generator that writes the HTML source.

## Re-render

```bash
python3 REACTOR-generator.py   # adjust the font path at the top first
google-chrome --headless=new --default-background-color=00000000 \
  --window-size=466,466 --force-device-scale-factor=2 \
  --screenshot=REACTOR-face-466-2x.png "file://$PWD/REACTOR-source.html"
```
