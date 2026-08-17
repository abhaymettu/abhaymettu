"""Two images for the profile.

header.svg   a terminal session: the research groups, then a real pipeline run
footer.svg   a dark colour field with the numinous line over it

The pipeline in the header is the actual file list of cms-inpatient-warehouse,
audit highlighted because running it before anything else is the point of the
convention. Nothing here is invented.

    python3 header.py        # writes header.svg and footer.svg
"""

W, H = 1200, 400
MONO = "'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace"
SERIF = "Newsreader, Georgia, 'Times New Roman', serif"

BG, RULE, USER, DIM, TEXT, ACCENT = "#0C0C0F", "#1C1C21", "#5E9E6E", "#8C8C95", "#F2F2EE", "#E4572E"


def prompt(y, command):
    return (
        f'  <text x="40" y="{y}" font-family="{MONO}" font-size="19">'
        f'<tspan fill="{USER}">abhay@mettu</tspan>'
        f'<tspan fill="#4A4A52"> ~ </tspan>'
        f'<tspan fill="{TEXT}">&#10095; {command}</tspan></text>'
    )


def out(y, text, fill=DIM):
    return (f'  <text x="40" y="{y}" font-family="{MONO}" font-size="18" '
            f'fill="{fill}">{text}</text>')


header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <circle cx="40" cy="36" r="6.5" fill="#2E2E34"/>
  <circle cx="62" cy="36" r="6.5" fill="#2E2E34"/>
  <circle cx="84" cy="36" r="6.5" fill="#2E2E34"/>
  <line x1="0" y1="66" x2="{W}" y2="66" stroke="{RULE}" stroke-width="1"/>
{prompt(122, "ls research/")}
{out(158, "machine-learning  quantitative  real-estate  commercial")}
{out(188, "healthcare  psychology  engineering")}
{prompt(238, "python3 05_measure.py --with-baselines")}
  <text x="40" y="274" font-family="{MONO}" font-size="18" fill="{DIM}">llm judge</text>
  <text x="330" y="274" font-family="{MONO}" font-size="18" fill="{TEXT}">85.5%</text>
  <text x="40" y="302" font-family="{MONO}" font-size="18" fill="{DIM}">pick the longer answer</text>
  <text x="330" y="302" font-family="{MONO}" font-size="18" fill="{ACCENT}">70.6%</text>
  <text x="430" y="302" font-family="{MONO}" font-size="18" fill="#4A4A52"># reads none of the text</text>
  <text x="40" y="330" font-family="{MONO}" font-size="18" fill="{DIM}">human ceiling</text>
  <text x="330" y="330" font-family="{MONO}" font-size="18" fill="{TEXT}">88.2%</text>
  <text x="40" y="374" font-family="{MONO}" font-size="19">
    <tspan fill="{USER}">abhay@mettu</tspan><tspan fill="#4A4A52"> ~ </tspan><tspan fill="{TEXT}">&#10095; &#9608;</tspan>
  </text>
</svg>
'''

FW, FH = 1200, 300
footer = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{FW}" height="{FH}" viewBox="0 0 {FW} {FH}" role="img">
  <defs>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="105"/>
    </filter>
  </defs>
  <rect width="{FW}" height="{FH}" fill="#08080B"/>
  <g filter="url(#soft)">
    <ellipse cx="270" cy="70" rx="330" ry="180" fill="#633B28" opacity="0.42"/>
    <ellipse cx="960" cy="250" rx="360" ry="200" fill="#23353F" opacity="0.48"/>
    <ellipse cx="600" cy="30" rx="260" ry="140" fill="#4E3646" opacity="0.34"/>
    <ellipse cx="450" cy="300" rx="300" ry="160" fill="#2B2B42" opacity="0.36"/>
  </g>
  <text x="{FW / 2}" y="{FH / 2 - 10}" text-anchor="middle" font-family="{SERIF}"
    font-size="46" letter-spacing="-0.5" fill="#EFECE5">This loop keeps running only</text>
  <text x="{FW / 2}" y="{FH / 2 + 46}" text-anchor="middle" font-family="{SERIF}"
    font-size="46" letter-spacing="-0.5" fill="#EFECE5">while you keep narrating it</text>
</svg>
'''

if __name__ == "__main__":
    open("header.svg", "w").write(header)
    open("footer.svg", "w").write(footer)
    print("header.svg footer.svg")
