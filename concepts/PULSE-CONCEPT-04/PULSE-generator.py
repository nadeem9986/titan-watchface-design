# Self-contained generator - shared helpers inlined below.
import base64, math
CX = CY = 233.0
def load_font(p): return base64.b64encode(open(p,'rb').read()).decode()
def polar(angle_deg, r, cx=CX, cy=CY):
    a = math.radians(angle_deg - 90)
    return (cx + r*math.cos(a), cy + r*math.sin(a))
def arc_path(angle0, angle1, r, cx=CX, cy=CY):
    x0,y0 = polar(angle0, r, cx, cy); x1,y1 = polar(angle1, r, cx, cy)
    large = 1 if (angle1-angle0) % 360 > 180 else 0
    return f'M {x0:.2f} {y0:.2f} A {r} {r} 0 {large} 1 {x1:.2f} {y1:.2f}'
def page(svg, transparent=True):
    bg = 'transparent' if transparent else '#000'
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>html,body{{margin:0;padding:0;background:{bg};}} svg{{display:block;}}</style></head><body>{svg}</body></html>'
def svg_shell(font_b64, font_family, body, extra_css=''):
    return f'''<svg width="466" height="466" viewBox="0 0 466 466" xmlns="http://www.w3.org/2000/svg">
  <style>
    @font-face {{ font-family:'{font_family}'; src:url(data:font/woff2;base64,{font_b64}) format('woff2'); }}
    text {{ font-family:'{font_family}', monospace; }}
    {extra_css}
  </style>
  {body}
</svg>'''


ARCH = load_font('../fonts/ArchivoBlack-400.woff2')
SG   = load_font('../fonts/SpaceGrotesk-400.woff2')
VIOLET='#8b5cf6'; CORAL='#ff6b5e'; WHITE='#ffffff'; MUT='#8f8a9a'; TRACK='#241f2e'

GOAL = 0.84  # step goal progress

def ring_segments():
    out=[]
    gap=6  # deg half-gap at each cardinal
    for q in range(4):
        a0 = q*90 + gap; a1 = (q+1)*90 - gap
        f0 = a0 + (a1-a0)*GOAL
        # filled part
        out.append(f'<path d="{arc_path(a0, f0, 216)}" stroke="url(#ring)" stroke-width="14" fill="none" stroke-linecap="round"/>')
        # track remainder
        out.append(f'<path d="{arc_path(f0+2, a1, 216)}" stroke="{TRACK}" stroke-width="14" fill="none" stroke-linecap="round"/>')
    return '\n    '.join(out)

def ring_segments_dim():
    out=[]
    gap=6
    for q in range(4):
        a0 = q*90 + gap; a1 = (q+1)*90 - gap
        out.append(f'<path d="{arc_path(a0, a1, 216)}" stroke="{TRACK}" stroke-width="3" fill="none"/>')
    return '\n    '.join(out)

def pill(cx, cy, icon, val):
    return f'''
    <g>
      <rect x="{cx-52}" y="{cy-20}" width="104" height="40" rx="20" fill="#17141d" stroke="#2b2635" stroke-width="1"/>
      <g transform="translate({cx-40},{cy-12.5})">{icon}</g>
      <text x="{cx-6}" y="{cy+7}" class="pv" fill="{WHITE}">{val}</text>
    </g>'''

FOOT  = f'<g transform="rotate(-22 12.5 12.5)" fill="{CORAL}"><rect x="7.5" y="2" width="10" height="13.5" rx="5"/><rect x="8.7" y="17.8" width="7.6" height="5.8" rx="2.9"/></g>'
FLAME = f'<path d="M12.5 2 C13.5 6 17 8.5 17 13.5 C17 17 15 20 12.5 20 C10 20 8 17 8 13.5 C8 11 9 9.5 10 8 C10.4 9.6 11 10.5 12 11 C11.3 8 11.5 5 12.5 2 Z" fill="{CORAL}"/>'
HEART = f'<path d="M12.5 21 C5 14.5 2 10.5 2 7.5 C2 4.5 4.5 2.5 7 2.5 C9 2.5 11 3.7 12.5 5.7 C14 3.7 16 2.5 18 2.5 C20.5 2.5 23 4.5 23 7.5 C23 10.5 20 14.5 12.5 21 Z" fill="{CORAL}"/>'

def body(aod=False):
    if aod:
        return f'''
    <circle cx="233" cy="233" r="232" fill="#0b0a0f"/>
    {ring_segments_dim()}
    <text x="233" y="292" class="time" fill="#6a6a6a" text-anchor="middle">10:08</text>'''
    return f'''
    <defs><linearGradient id="ring" gradientUnits="userSpaceOnUse" x1="80" y1="60" x2="400" y2="420">
      <stop offset="0%" stop-color="{VIOLET}"/><stop offset="100%" stop-color="{CORAL}"/>
    </linearGradient></defs>
    <circle cx="233" cy="233" r="232" fill="#0b0a0f"/>
    {ring_segments()}
    <text x="233" y="116" class="date" fill="{MUT}" text-anchor="middle">FRI 30 OCT</text>
    <text x="233" y="292" class="time" fill="{WHITE}" text-anchor="middle">10:08</text>
    {pill(118, 352, FOOT, '8432')}
    {pill(233, 370, FLAME, '412')}
    {pill(348, 352, HEART, '72')}'''

css = '.time { font-size:78px; font-family:"Archivo Black"; } .date { font-size:21px; letter-spacing:5px; font-family:"Space Grotesk"; } .pv { font-size:21px; font-family:"Space Grotesk"; }'
shell_css = css + ' text { font-family:"Space Grotesk", sans-serif; }'
sg_face = '@font-face { font-family:"Space Grotesk"; src:url(data:font/woff2;base64,' + SG + ') format("woff2"); }'
shell_css = sg_face + shell_css
open('PULSE-source.html','w').write(page(svg_shell(ARCH, 'Archivo Black', body(), shell_css)))
open('PULSE-source-AOD.html','w').write(page(svg_shell(ARCH, 'Archivo Black', body(aod=True), shell_css)))
print('PULSE written')
