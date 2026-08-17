"""Animated dark bloom: the haze drifts, the rings turn, the line sits still.

Declarative SMIL only, no script, so it runs inside an <img> on GitHub and
still looks right in the first frame if a viewer freezes animation.
"""

W, H = 1200, 400
SERIF = "Newsreader, Georgia, 'Times New Roman', serif"
LINES = ["This loop keeps running only", "while you keep narrating it"]

# cx cy rx ry fill opacity drift-x drift-y period
BLOOM = [
    (250, 150, 330, 210, "#2E1B57", 0.46, 70, -40, 29),
    (930, 300, 380, 240, "#1E1238", 0.52, -90, 30, 37),
    (640, 120, 250, 160, "#3A2270", 0.30, 60, 50, 23),
    (1090, 360, 230, 180, "#241640", 0.38, -70, -50, 41),
]

blobs = "\n".join(
    f'''    <ellipse cx="{b[0]}" cy="{b[1]}" rx="{b[2]}" ry="{b[3]}" fill="{b[4]}" opacity="{b[5]}">
      <animateTransform attributeName="transform" type="translate" dur="{b[8]}s"
        values="0 0; {b[6]} {b[7]}; 0 0" repeatCount="indefinite"/>
      <animate attributeName="opacity" dur="{b[8] * 0.7:.0f}s"
        values="{b[5]};{b[5] * 1.35:.2f};{b[5]}" repeatCount="indefinite"/>
    </ellipse>'''
    for b in BLOOM
)

rings = "\n".join(
    f'''    <ellipse cx="600" cy="200" rx="{rx}" ry="{ry}" stroke-opacity="{op}" stroke-width="{sw}"/>'''
    for rx, ry, op, sw in ((470, 196, 0.40, 1.8), (392, 158, 0.24, 1.4), (310, 120, 0.13, 1.2))
)

text = "\n".join(
    f'  <text x="{W / 2}" y="{182 + i * 78}" text-anchor="middle" font-family="{SERIF}" '
    f'font-size="66" letter-spacing="-0.5" fill="#F0EDE6">{line}</text>'
    for i, line in enumerate(LINES)
)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">
  <defs>
    <filter id="haze" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="92"/>
    </filter>
    <filter id="soften" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8"/>
    </filter>
    <radialGradient id="vignette" cx="50%" cy="45%" r="72%">
      <stop offset="0%" stop-color="#050409" stop-opacity="0"/>
      <stop offset="100%" stop-color="#030308" stop-opacity="0.92"/>
    </radialGradient>
    <filter id="grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
  </defs>

  <rect width="{W}" height="{H}" fill="#050409"/>

  <g filter="url(#haze)">
{blobs}
  </g>

  <rect width="{W}" height="{H}" fill="url(#vignette)"/>

  <g filter="url(#soften)" fill="none" stroke="#8E6BD8">
    <animateTransform attributeName="transform" type="rotate"
      values="-9 600 200; 351 600 200" dur="120s" repeatCount="indefinite"/>
{rings}
  </g>

  <rect width="{W}" height="{H}" filter="url(#grain)" opacity="0.06"/>

{text}
</svg>
'''

open("header.svg", "w").write(svg)
print("header.svg", len(svg), "bytes")
