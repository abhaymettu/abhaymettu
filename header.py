"""The header: one line set on paper, light and dark.

GitHub strips CSS from a README, so the type has to travel inside the image.
No webfont can load through GitHub's image proxy either, which is why the
stack is the research site's own declared fallback: Newsreader if the reader
happens to have it, Georgia otherwise.

    python3 header.py        # writes cycle-light.svg and cycle-dark.svg
"""

W, H = 1200, 360
SERIF = "Newsreader, Georgia, 'Times New Roman', serif"
LINES = ["This loop keeps running only", "while you keep narrating it"]

THEMES = {
    "light": dict(paper="#FCFCFA", ink="#17171B", rule="#E6E6E1"),
    "dark":  dict(paper="#17171B", ink="#F2F2EE", rule="#2C2C33"),
}


def svg(t):
    text = "\n".join(
        f'  <text x="96" y="{168 + i * 62}" font-family="{SERIF}" font-size="49" '
        f'letter-spacing="-0.5" fill="{t["ink"]}">{line}</text>'
        for i, line in enumerate(LINES)
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img">\n'
        f'  <rect width="{W}" height="{H}" fill="{t["paper"]}"/>\n'
        f'  <line x1="96" y1="86" x2="240" y2="86" stroke="{t["rule"]}" stroke-width="1"/>\n'
        f'{text}\n</svg>\n'
    )


if __name__ == "__main__":
    for name, theme in THEMES.items():
        open(f"cycle-{name}.svg", "w").write(svg(theme))
        print(f"cycle-{name}.svg")
