"""Generate the profile header, light and dark.

The design is the research site's own: paper column, mono eyebrow, one serif
statement, and the terracotta used exactly once, on the measure that failed.
The strip is the preregistered-precision result from reddit-selfdistance.

    python3 header.py        # writes header-light.svg and header-dark.svg

GitHub serves README images through a proxy, so no webfont can load. The stack
is the site's own declared fallback: Newsreader if the reader has it, Georgia
otherwise.
"""

W, H = 1200, 372
PAD = 80
X0, X1 = PAD, W - PAD          # precision axis, 0.0 to 1.0
AXIS_Y = 268

SERIF = "Newsreader, Georgia, 'Times New Roman', serif"
MONO = "'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace"

THEMES = {
    "light": dict(paper="#FCFCFA", ink="#17171B", soft="#6E6E77",
                  faint="#A6A6AE", rule="#E6E6E1", under="#B4472F"),
    "dark":  dict(paper="#17171B", ink="#F2F2EE", soft="#9A9AA3",
                  faint="#66666E", rule="#2C2C33", under="#D06A4F"),
}


def x(v):
    """Precision value to canvas x."""
    return X0 + v * (X1 - X0)


def svg(t):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">
  <rect width="{W}" height="{H}" fill="{t['paper']}"/>

  <text x="{PAD}" y="76" font-family="{MONO}" font-size="14" letter-spacing="2.4" fill="{t['faint']}">ABHAY METTU</text>

  <text x="{PAD}" y="180" font-family="{SERIF}" font-size="50" font-weight="400" letter-spacing="-0.6" fill="{t['ink']}">Every report here says what did not hold.</text>

  <line x1="{X0}" y1="{AXIS_Y}" x2="{X1}" y2="{AXIS_Y}" stroke="{t['rule']}" stroke-width="1"/>
  <line x1="{x(0.70):.1f}" y1="{AXIS_Y - 26}" x2="{x(0.70):.1f}" y2="{AXIS_Y + 12}" stroke="{t['faint']}" stroke-width="1" stroke-dasharray="3 4"/>
  <text x="{x(0.70):.1f}" y="{AXIS_Y - 36}" text-anchor="middle" font-family="{MONO}" font-size="12" letter-spacing="1.1" fill="{t['faint']}">0.70 PREREGISTERED THRESHOLD</text>

  <circle cx="{x(0.52):.1f}" cy="{AXIS_Y}" r="5.5" fill="{t['under']}"/>
  <text x="{x(0.52):.1f}" y="{AXIS_Y + 32}" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="{t['under']}">0.52 obligation</text>

  <circle cx="{x(0.94):.1f}" cy="{AXIS_Y}" r="5.5" fill="{t['ink']}"/>
  <text x="{X1}" y="{AXIS_Y + 32}" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{t['soft']}">0.94 self-criticism</text>

  <text x="{PAD}" y="{H - 26}" font-family="{MONO}" font-size="11.5" letter-spacing="1.1" fill="{t['faint']}">PRECISION AGAINST 200 BLIND HAND-CODED POSTS &#183; REDDIT-SELFDISTANCE</text>
</svg>
'''


for name, t in THEMES.items():
    open(f"header-{name}.svg", "w").write(svg(t))
    print(f"header-{name}.svg")
