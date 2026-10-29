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


FONT = load_font('../depmono/DepartureMono-1.500/DepartureMono-Regular.woff2')
CYAN = '#35e0ff'; STRUCT = '#2b3440'; TXT = '#9fb0c0'; WHITE = '#f5f5f5'

def ticks12():
    out=[]
    for i in range(12):
        x1,y1 = polar(i*30, 214); x2,y2 = polar(i*30, 228)
        out.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{STRUCT}" stroke-width="2"/>')
    return '\n    '.join(out)

def readout(cx, cy, icon, val):
    return f'''<g transform="translate({cx-12.5},{cy-30})">{icon}</g>
    <text x="{cx}" y="{cy+20}" class="ro" fill="{TXT}" text-anchor="middle">{val}</text>'''

HEART = f'<path d="M12.5 21 C5 14.5 2 10.5 2 7.5 C2 4.5 4.5 2.5 7 2.5 C9 2.5 11 3.7 12.5 5.7 C14 3.7 16 2.5 18 2.5 C20.5 2.5 23 4.5 23 7.5 C23 10.5 20 14.5 12.5 21 Z" fill="none" stroke="{TXT}" stroke-width="2"/>'
CLOUD = f'<path d="M7 18 L18 18 C21 18 22.5 15.8 22.5 13.8 C22.5 11.6 20.8 10 18.7 10 C18 6.8 15.3 4.5 12 4.5 C8.2 4.5 5.2 7.4 5.2 11.2 C3 11.6 1.8 13.3 1.8 15.2 C1.8 16.9 3.4 18 7 18 Z" fill="none" stroke="{TXT}" stroke-width="2"/>'
FOOT  = f'<g transform="rotate(-22 12.5 12.5)" fill="{TXT}"><rect x="7.5" y="2" width="10" height="13.5" rx="5"/><rect x="8.7" y="17.8" width="7.6" height="5.8" rx="2.9"/></g>'
BATT  = f'<rect x="1" y="6.5" width="19" height="11" rx="2.5" fill="none" stroke="{TXT}" stroke-width="2"/><rect x="21.5" y="9.8" width="2.6" height="4.6" rx="1" fill="{TXT}"/><rect x="3.4" y="8.9" width="9.9" height="6.2" rx="1" fill="{TXT}"/>'

def body(aod=False):
    if aod:
        return f'''
    <circle cx="233" cy="233" r="232" fill="#000000"/>
    <path d="{arc_path(0, 252, 224)}" stroke="#8a6d2f" stroke-width="1" fill="none" opacity="0.55"/>
    <text x="233" y="262" class="time" fill="#7a7a7a" text-anchor="middle">10:08</text>'''
    return f'''
    <circle cx="233" cy="233" r="232" fill="#000000"/>
    <circle cx="233" cy="233" r="224" fill="none" stroke="#15202b" stroke-width="1.5"/>
    {ticks12()}
    <path d="{arc_path(0, 252, 224)}" stroke="{CYAN}" stroke-width="3" fill="none" stroke-linecap="round"/>
    {readout(233, 104, CLOUD, '24C')}
    {readout(398, 233, HEART, '72')}
    {readout(233, 372, BATT, '62%')}
    {readout(68, 233, FOOT, '8432')}
    <text x="233" y="262" class="time" fill="{WHITE}" text-anchor="middle">10:08</text>
    <text x="233" y="304" class="term" fill="#6b7c8c" text-anchor="middle">&gt; FRI 30 OCT</text>
    <rect x="359" y="290" width="11" height="18" fill="{CYAN}"/>'''

css = '.time { font-size:80px; letter-spacing:1px; } .term { font-size:21px; letter-spacing:2px; } .ro { font-size:21px; }'
open('REACTOR-source.html','w').write(page(svg_shell(FONT, 'Departure Mono', body(), css)))
open('REACTOR-source-AOD.html','w').write(page(svg_shell(FONT, 'Departure Mono', body(aod=True), css)))
print('REACTOR written')
