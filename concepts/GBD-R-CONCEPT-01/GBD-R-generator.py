import base64, math, os

FONT = base64.b64encode(open('depmono/DepartureMono-1.500/DepartureMono-Regular.woff2','rb').read()).decode()
CX = CY = 233.0

def polar(angle_deg, r):
    a = math.radians(angle_deg - 90)  # 0 deg = 12 o'clock
    return (CX + r*math.cos(a), CY + r*math.sin(a))

def ticks():
    out = []
    for i in range(60):
        five = (i % 5 == 0)
        a = i * 6.0
        if five:
            x1,y1 = polar(a, 213); x2,y2 = polar(a, 232)
            out.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#c9c9c9" stroke-width="3"/>')
        else:
            x1,y1 = polar(a, 223); x2,y2 = polar(a, 231)
            out.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#4a4a4a" stroke-width="1.5"/>')
    return '\n    '.join(out)

def hour_ticks_dim():
    out = []
    for i in range(12):
        a = i * 30.0
        x1,y1 = polar(a, 216); x2,y2 = polar(a, 232)
        out.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#333333" stroke-width="3"/>')
    return '\n    '.join(out)

# Footprint (steps) icon, drawn at 0,0 in a 28x28 box, stroke style
STEPS_ICON = '''
    <g transform="translate({x},{y}) scale({s}) rotate(-22 14 14)" fill="#d8d8d8">
      <rect x="9.5" y="2" width="10.5" height="15" rx="5.2"/>
      <rect x="10.8" y="19.5" width="8" height="6.5" rx="3.2"/>
    </g>'''

BATTERY_ICON = '''
    <g transform="translate({x},{y}) scale({s})">
      <rect x="1" y="6" width="22" height="12" rx="2.5" fill="none" stroke="#d8d8d8" stroke-width="2"/>
      <rect x="24.5" y="9.5" width="3" height="5" rx="1" fill="#d8d8d8"/>
      <rect x="3.5" y="8.5" width="{fillw}" height="7" rx="1" fill="#d8d8d8"/>
    </g>'''

def face_svg(aod=False):
    if aod:
        body = f'''
    <circle cx="233" cy="233" r="232" fill="#000000"/>
    <circle cx="233" cy="233" r="202" fill="none" stroke="#1c1c1c" stroke-width="1"/>
    {hour_ticks_dim()}
    <text x="233" y="272" class="time" fill="#7a7a7a" text-anchor="middle">10:08</text>'''
    else:
        steps = STEPS_ICON.format(x=77, y=318, s=1.0)
        batt  = BATTERY_ICON.format(x=293, y=322, s=1.1, fillw=17*0.62)
        body = f'''
    <circle cx="233" cy="233" r="232" fill="#000000"/>
    {ticks()}
    <circle cx="233" cy="233" r="202" fill="none" stroke="#262626" stroke-width="1"/>
    <text x="236" y="126" class="date" fill="#a8a8a8" text-anchor="middle">FRI 30 OCT</text>
    <line x1="170" y1="146" x2="296" y2="146" stroke="#2e2e2e" stroke-width="2" stroke-dasharray="5 5"/>
    <text x="225" y="272" class="time" fill="#f2f2f2" text-anchor="middle">10:08</text>
    <text x="402" y="216" class="secs" fill="#8f8f8f" text-anchor="middle">42</text>
    <line x1="170" y1="304" x2="296" y2="304" stroke="#2e2e2e" stroke-width="2" stroke-dasharray="5 5"/>
    {steps}
    <text x="116" y="342" class="comp" fill="#d8d8d8">8,432</text>
    {batt}
    <text x="338" y="342" class="comp" fill="#d8d8d8">62%</text>'''
    return f'''<svg width="466" height="466" viewBox="0 0 466 466" xmlns="http://www.w3.org/2000/svg">
  <style>
    @font-face {{ font-family:'Departure Mono'; src:url(data:font/woff2;base64,{FONT}) format('woff2'); }}
    text {{ font-family:'Departure Mono', monospace; }}
    .time {{ font-size:96px; letter-spacing:1px; }}
    .date {{ font-size:24px; letter-spacing:6px; }}
    .secs {{ font-size:28px; }}
    .comp {{ font-size:23px; }}
  </style>
  {body}
</svg>'''

def page(svg, transparent=False):
    bg = 'transparent' if transparent else '#000'
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;padding:0;background:{bg};}} svg{{display:block;}}
</style></head><body>{svg}</body></html>'''

open('face.html','w').write(page(face_svg(), transparent=True))
open('face_aod.html','w').write(page(face_svg(aod=True), transparent=True))
print('wrote face.html, face_aod.html')
