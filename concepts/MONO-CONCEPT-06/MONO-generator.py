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
GREY='#d8d8d8'; SUB='#8a8a8a'

FOOT  = '<g transform="rotate(-22 12.5 12.5)" fill="#e8e8e8"><rect x="7.5" y="2" width="10" height="13.5" rx="5"/><rect x="8.7" y="17.8" width="7.6" height="5.8" rx="2.9"/></g>'
BATT  = '<rect x="1" y="6.5" width="19" height="11" rx="2.5" fill="none" stroke="#e8e8e8" stroke-width="2"/><rect x="21.5" y="9.8" width="2.6" height="4.6" rx="1" fill="#e8e8e8"/><rect x="3.4" y="8.9" width="9.9" height="6.2" rx="1" fill="#e8e8e8"/>'
HEART = '<path d="M12.5 21 C5 14.5 2 10.5 2 7.5 C2 4.5 4.5 2.5 7 2.5 C9 2.5 11 3.7 12.5 5.7 C14 3.7 16 2.5 18 2.5 C20.5 2.5 23 4.5 23 7.5 C23 10.5 20 14.5 12.5 21 Z" fill="none" stroke="#e8e8e8" stroke-width="2"/>'
CLOUD = '<path d="M7 18 L18 18 C21 18 22.5 15.8 22.5 13.8 C22.5 11.6 20.8 10 18.7 10 C18 6.8 15.3 4.5 12 4.5 C8.2 4.5 5.2 7.4 5.2 11.2 C3 11.6 1.8 13.3 1.8 15.2 C1.8 16.9 3.4 18 7 18 Z" fill="none" stroke="#e8e8e8" stroke-width="2"/>'

def icon_at(angle, r, icon):
    cx,cy = polar(angle, r)
    return f'<g transform="translate({cx-12.5:.1f},{cy-12.5:.1f})">{icon}</g>'

def tick(angle=48):  # 8 minutes -> traveling tick
    x1,y1 = polar(angle, 222); x2,y2 = polar(angle, 232)
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#ffffff" stroke-width="2"/>'

def body(aod=False):
    if aod:
        return f'''
    <circle cx="233" cy="233" r="232" fill="#000000"/>
    <text x="233" y="262" class="time" fill="#555555" text-anchor="middle">10:08</text>'''
    return f'''
    <circle cx="233" cy="233" r="232" fill="#000000"/>
    {tick()}
    {icon_at(45, 150, CLOUD)}
    {icon_at(135, 150, BATT)}
    {icon_at(225, 150, FOOT)}
    {icon_at(315, 150, HEART)}
    <text x="233" y="256" class="time" fill="{GREY}" text-anchor="middle">10:08</text>
    <text x="236" y="312" class="date" fill="{SUB}" text-anchor="middle">FRI 30 OCT</text>'''

css = '.time { font-size:100px; letter-spacing:2px; } .date { font-size:22px; letter-spacing:8px; }'
open('MONO-source.html','w').write(page(svg_shell(FONT, 'Departure Mono', body(), css)))
open('MONO-source-AOD.html','w').write(page(svg_shell(FONT, 'Departure Mono', body(aod=True), css)))
print('MONO written')
