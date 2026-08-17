"""Two images for the profile.

header.svg   a REPL session: 98% accuracy on a 98% base rate
footer.svg   black field, the numinous line centred in it, links to the site

    python3 header.py        # writes header.svg and footer.svg
"""

W, H = 1200, 400
MONO = "'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace"
SERIF = "Newsreader, Georgia, 'Times New Roman', serif"

BG, RULE, USER, DIM, TEXT, ACCENT = "#0C0C0F", "#1C1C21", "#5E9E6E", "#8C8C95", "#F2F2EE", "#E4572E"

REPL = [
    ("&gt;&gt;&gt; ", "accuracy_score(y_test, model.predict(X_test))", None),
    ("", "0.98", "out"),
    ("&gt;&gt;&gt; ", "y_test.mean()", None),
    ("", "0.98", "out"),
]


def prompt(y, command):
    return (
        f'  <text x="40" y="{y}" font-family="{MONO}" font-size="19">'
        f'<tspan fill="{USER}">abhay@mettu</tspan>'
        f'<tspan fill="#4A4A52"> ~ </tspan>'
        f'<tspan fill="{TEXT}">&#10095; {command}</tspan></text>'
    )


rows, y = [], 190
for lead, body, kind in REPL:
    if kind == "out":
        rows.append(
            f'  <text x="40" y="{y}" font-family="{MONO}" font-size="18" '
            f'fill="{ACCENT}">{body}</text>'
        )
    else:
        rows.append(
            f'  <text x="40" y="{y}" font-family="{MONO}" font-size="18">'
            f'<tspan fill="#4A4A52">{lead}</tspan>'
            f'<tspan fill="#D8D8DE">{body}</tspan></text>'
        )
    y += 34

header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <circle cx="40" cy="36" r="6.5" fill="#2E2E34"/>
  <circle cx="62" cy="36" r="6.5" fill="#2E2E34"/>
  <circle cx="84" cy="36" r="6.5" fill="#2E2E34"/>
  <line x1="0" y1="66" x2="{W}" y2="66" stroke="{RULE}" stroke-width="1"/>
{prompt(120, "python3")}
  <text x="40" y="156" font-family="{MONO}" font-size="18" fill="{DIM}">Python 3.12  ·  imbalanced clinical outcome, 2,412 rows</text>
{chr(10).join(rows)}
  <text x="40" y="{y + 8}" font-family="{MONO}" font-size="18" fill="#4A4A52"># the model learned to say "no"</text>
  <text x="40" y="{y + 52}" font-family="{MONO}" font-size="19">
    <tspan fill="{USER}">abhay@mettu</tspan><tspan fill="#4A4A52"> ~ </tspan><tspan fill="{TEXT}">&#10095; &#9608;</tspan>
  </text>
</svg>
'''

FW, FH = 1200, 240
footer = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{FW}" height="{FH}" viewBox="0 0 {FW} {FH}" role="img">
  <rect width="{FW}" height="{FH}" fill="#000000"/>
  <text x="{FW / 2}" y="108" text-anchor="middle" font-family="{SERIF}" font-size="44"
    letter-spacing="-0.5" fill="#EDEAE3">This loop keeps running only</text>
  <text x="{FW / 2}" y="160" text-anchor="middle" font-family="{SERIF}" font-size="44"
    letter-spacing="-0.5" fill="#EDEAE3">while you keep narrating it</text>
</svg>
'''

if __name__ == "__main__":
    open("header.svg", "w").write(header)
    open("footer.svg", "w").write(footer)
    print("header.svg footer.svg")
