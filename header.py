"""Footer image for the profile.

loop.svg   black field, the numinous line centred in it, links to the site

    python3 header.py        # writes loop.svg
"""

SERIF = "Newsreader, Georgia, 'Times New Roman', serif"

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
    open("loop.svg", "w").write(footer)
    print("loop.svg")
