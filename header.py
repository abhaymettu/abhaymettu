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
{prompt(246, "cd cms-inpatient-warehouse &amp;&amp; ./run_all.sh")}
  <text x="40" y="282" font-family="{MONO}" font-size="18" fill="{DIM}">00_download <tspan fill="#4A4A52">&#8594;</tspan> <tspan fill="{ACCENT}">01_audit</tspan> <tspan fill="#4A4A52">&#8594;</tspan> 02_build <tspan fill="#4A4A52">&#8594;</tspan> 03_test <tspan fill="#4A4A52">&#8594;</tspan> 04_negative_control <tspan fill="#4A4A52">&#8594;</tspan> 05_report</text>
{out(312, "292,306 discharges  ·  35 checks  ·  7 injected faults caught", "#6E6E77")}
  <text x="40" y="366" font-family="{MONO}" font-size="19">
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
  <rect width="{FW}" height="{FH}" fill="#0C0C0F"/>
  <g filter="url(#soft)">
    <ellipse cx="230" cy="90" rx="330" ry="190" fill="#7A4A32" opacity="0.55"/>
    <ellipse cx="980" cy="230" rx="360" ry="210" fill="#2F4652" opacity="0.60"/>
    <ellipse cx="620" cy="40" rx="260" ry="150" fill="#6B4B5E" opacity="0.45"/>
    <ellipse cx="470" cy="290" rx="300" ry="170" fill="#3A3A57" opacity="0.45"/>
  </g>
  <text x="92" y="152" font-family="{SERIF}" font-size="46" letter-spacing="-0.5"
    fill="#F0EDE6">This loop keeps running only</text>
  <text x="92" y="208" font-family="{SERIF}" font-size="46" letter-spacing="-0.5"
    fill="#F0EDE6">while you keep narrating it</text>
</svg>
'''

if __name__ == "__main__":
    open("header.svg", "w").write(header)
    open("footer.svg", "w").write(footer)
    print("header.svg footer.svg")
