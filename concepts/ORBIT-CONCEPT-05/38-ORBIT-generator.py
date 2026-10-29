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


FONT = load_font('../fonts/SpaceGrotesk-400.woff2')
RINGC='#232c3c'; DOT='#8fb8ff'; TXT='#e8edf5'; SUB='#5b6b85'

def dot(angle, r_orbit, frac, label=''):
    cx,cy = polar(angle, r_orbit)
    a0=0; a1=frac*360
    fill = f'<path d="{arc_path(0, frac*360, 8, cx, cy)}" stroke="{DOT}" stroke-width="3.5" fill="none" stroke-linecap="round"/>' if frac>0 else ''
    return f'''
    <circle cx="{cx:.1f}" cy="{cy:.1f}" r="12" fill="#0a0d14" stroke="#3a4763" stroke-width="1.5"/>
    <g transform="rotate(0 {cx:.1f} {cy:.1f})">{fill}</g>'''

def rings(color=RINGC):
    return '\n    '.join(f'<circle cx="233" cy="233" r="{r}" fill="none" stroke="{color}" stroke-width="1"/>' for r in (148,180,206))

def body(aod=False):
    if aod:
        return f'''
    <circle cx="233" cy="233" r="232" fill="#0a0d14"/>
    {rings('#141a26')}
    <text x="233" y="262" class="time" fill="#55606e" text-anchor="middle">10:08</text>'''
    return f'''
    <circle cx="233" cy="233" r="232" fill="#0a0d14"/>
    {rings()}
    {dot(60, 206, 0.62)}
    {dot(150, 180, 0.84)}
    {dot(240, 148, 0.60)}
    {dot(330, 148, 0.72)}
    <text x="233" y="262" class="time" fill="{TXT}" text-anchor="middle">10:08</text>
    <text x="233" y="304" class="date" fill="{SUB}" text-anchor="middle">FRI 30 OCT</text>'''

css = '.time { font-size:88px; font-weight:500; } .date { font-size:21px; letter-spacing:6px; }'
open('ORBIT-source.html','w').write(page(svg_shell(FONT, 'Space Grotesk', body(), css)))
open('ORBIT-source-AOD.html','w').write(page(svg_shell(FONT, 'Space Grotesk', body(aod=True), css)))
print('ORBIT written')
