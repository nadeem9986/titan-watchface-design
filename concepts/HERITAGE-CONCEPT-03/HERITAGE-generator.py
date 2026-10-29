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


FONT = load_font('../fonts/CormorantGaramond-500.woff2')
GOLD = '#d4af6a'; IVORY = '#ece4d0'; DIM = '#3a3a3a'

def hand(angle, length, w_base, w_tip, tail=10, color=IVORY):
    # tapered dauphine polygon pointing to angle
    bx,by = polar(angle, -tail); tx,ty = polar(angle, length)
    a = math.radians(angle-90)
    nx,ny = -math.sin(a), math.cos(a)  # normal
    p1 = (bx+nx*w_base/2, by+ny*w_base/2); p2 = (bx-nx*w_base/2, by-ny*w_base/2)
    p3 = (tx-nx*w_tip/2, ty-ny*w_tip/2); p4 = (tx+nx*w_tip/2, ty+ny*w_tip/2)
    return f'<polygon points="{p1[0]:.1f},{p1[1]:.1f} {p3[0]:.1f},{p3[1]:.1f} {p4[0]:.1f},{p4[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>'

def indices(color=GOLD, numeral=True):
    out=[]
    for i in range(1,12):  # skip 12, numeral goes there
        x1,y1 = polar(i*30, 190); x2,y2 = polar(i*30, 206)
        out.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" stroke-width="2.5"/>')
    if numeral:
        out.append(f'<text x="233" y="66" class="num" fill="{IVORY}" text-anchor="middle">12</text>')
    return '\n    '.join(out)

def minute_track():
    out=[]
    for i in range(60):
        if i % 5 == 0: continue
        x1,y1 = polar(i*6, 208); x2,y2 = polar(i*6, 213)
        out.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{DIM}" stroke-width="1"/>')
    return '\n    '.join(out)

def subdial():
    return f'''
    <circle cx="233" cy="322" r="38" fill="none" stroke="#4a4a4a" stroke-width="1"/>
    <text x="233" y="330" class="sub" fill="{IVORY}" text-anchor="middle">FRI 30</text>'''

def body(aod=False):
    if aod:
        return f'''
    <circle cx="233" cy="233" r="232" fill="#000000"/>
    {indices(color='#4a4a4a', numeral=False)}
    <text x="233" y="66" class="num" fill="#5a5a5a" text-anchor="middle">12</text>
    {hand(304, 95, 7, 2, color='#6a6a6a')}
    {hand(48, 150, 6, 1.5, color='#6a6a6a')}
    <circle cx="233" cy="233" r="5" fill="#6a6a6a"/>'''
    # second hand: 42s -> 252 deg
    sx1,sy1 = polar(252, -24); sx2,sy2 = polar(252, 192)
    return f'''
    <defs><radialGradient id="dial" cx="50%" cy="42%" r="65%">
      <stop offset="0%" stop-color="#1e1e20"/><stop offset="100%" stop-color="#0c0c0e"/>
    </radialGradient></defs>
    <circle cx="233" cy="233" r="232" fill="url(#dial)"/>
    {minute_track()}
    <path d="{arc_path(0, 0.62*360, 218)}" stroke="{GOLD}" stroke-width="1.5" fill="none" opacity="0.8"/>
    {indices()}
    {subdial()}
    {hand(304, 95, 7, 2)}
    {hand(48, 150, 6, 1.5)}
    <line x1="{sx1:.1f}" y1="{sy1:.1f}" x2="{sx2:.1f}" y2="{sy2:.1f}" stroke="{GOLD}" stroke-width="1.2"/>
    <circle cx="233" cy="233" r="5.5" fill="{GOLD}"/>
    <circle cx="233" cy="233" r="2.5" fill="#0c0c0e"/>'''

css = '.num { font-size:32px; } .sub { font-size:21px; letter-spacing:2px; }'
open('HERITAGE-source.html','w').write(page(svg_shell(FONT, 'Cormorant Garamond', body(), css)))
open('HERITAGE-source-AOD.html','w').write(page(svg_shell(FONT, 'Cormorant Garamond', body(aod=True), css)))
print('HERITAGE written')
