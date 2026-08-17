"""Two images for the profile.

header.svg   a terminal session ending in a --help screen
footer.svg   black field, the numinous line centred in it

Every flag in the help screen is a convention that actually governs the
analysis repos: audit before building, thresholds set in advance, faults
injected to prove the checks can fire.

    python3 header.py        # writes header.svg and footer.svg
"""

W, H = 1200, 400
MONO = "'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace"
SERIF = "Newsreader, Georgia, 'Times New Roman', serif"

BG, RULE, USER, DIM, TEXT, ACCENT = "#0C0C0F", "#1C1C21", "#5E9E6E", "#8C8C95", "#F2F2EE", "#E4572E"

FLAGS = [
    ("--audit-first", "audit the data before building on it", "on"),
    ("--preregister", "set the threshold before looking", "on"),
    ("--negative-control", "inject faults to prove the checks fire", "on"),
    ("--p-hack", "unsupported", None),
]


def prompt(y, command):
    return (
        f'  <text x="40" y="{y}" font-family="{MONO}" font-size="19">'
        f'<tspan fill="{USER}">abhay@mettu</tspan>'
        f'<tspan fill="#4A4A52"> ~ </tspan>'
        f'<tspan fill="{TEXT}">&#10095; {command}</tspan></text>'
    )


rows, y = [], 192
for flag, desc, state in FLAGS:
    last = state is None
    rows.append(
        f'  <text x="40" y="{y}" font-family="{MONO}" font-size="18" '
        f'fill="{ACCENT if last else "#B9B9C0"}">{flag}</text>'
    )
    rows.append(
        f'  <text x="300" y="{y}" font-family="{MONO}" font-size="18" '
        f'fill="{ACCENT if last else DIM}">{desc}</text>'
    )
    if state:
        rows.append(
            f'  <text x="820" y="{y}" font-family="{MONO}" font-size="18" '
            f'fill="{USER}">{state}</text>'
        )
    y += 36

header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <circle cx="40" cy="36" r="6.5" fill="#2E2E34"/>
  <circle cx="62" cy="36" r="6.5" fill="#2E2E34"/>
  <circle cx="84" cy="36" r="6.5" fill="#2E2E34"/>
  <line x1="0" y1="66" x2="{W}" y2="66" stroke="{RULE}" stroke-width="1"/>
{prompt(120, "abhay --help")}
  <text x="40" y="156" font-family="{MONO}" font-size="18" fill="{DIM}">usage: abhay [analysis] [--audit-first] [--preregister] [--negative-control]</text>
{chr(10).join(rows)}
  <text x="40" y="{y + 26}" font-family="{MONO}" font-size="19">
    <tspan fill="{USER}">abhay@mettu</tspan><tspan fill="#4A4A52"> ~ </tspan><tspan fill="{TEXT}">&#10095; &#9608;</tspan>
  </text>
</svg>
'''

FW, FH = 1200, 260
footer = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{FW}" height="{FH}" viewBox="0 0 {FW} {FH}" role="img">
  <rect width="{FW}" height="{FH}" fill="#000000"/>
  <line x1="{FW / 2 - 26}" y1="66" x2="{FW / 2 + 26}" y2="66" stroke="#2A2A2E" stroke-width="1"/>
  <text x="{FW / 2}" y="134" text-anchor="middle" font-family="{SERIF}" font-size="44"
    letter-spacing="-0.5" fill="#EDEAE3">This loop keeps running only</text>
  <text x="{FW / 2}" y="186" text-anchor="middle" font-family="{SERIF}" font-size="44"
    letter-spacing="-0.5" fill="#EDEAE3">while you keep narrating it</text>
  <text x="{FW / 2}" y="228" text-anchor="middle" font-family="{MONO}" font-size="11.5"
    letter-spacing="2.4" fill="#43434A">NUMINOUS.ONE</text>
</svg>
'''

if __name__ == "__main__":
    open("header.svg", "w").write(header)
    open("footer.svg", "w").write(footer)
    print("header.svg footer.svg")
