"""Animated header: numinous's haze, with its lines cycling through it.

The quotes are numinous.one's own, copied from that repo's index.html. GitHub
serves README images as static bytes through a caching proxy and runs no
script inside an <img>, so a genuinely random line per page load is not
available. The lines rotate instead: each one fades up, holds, fades out, and
the cycle is long enough that two visits rarely open on the same one.

Declarative SMIL only. The first frame is composed, so a viewer with reduced
motion sees a finished picture rather than an empty one.

    python3 header.py        # writes header.svg
"""

W, H = 1200, 400
SERIF = "Newsreader, Georgia, 'Times New Roman', serif"

HOLD = 7.0          # seconds each line is up
FADE = 1.4          # seconds of crossfade at each end

QUOTES = [
    "This loop only keeps running while you keep narrating it.",
    "You are the sky. Everything else is just the weather.",
    "The thought is not the thinker. Watch it pass, and notice you remain.",
    "Notice that you are noticing. That is already the way out.",
    "Between stimulus and response there is a space. In that space is our freedom.",
    "The story of you is still being written. Set the pen down; let the page breathe.",
    "You are stuck only because you keep looking down. The next step is small.",
    "Motion, not certainty, dissolves the fog. Take one honest step.",
]

# cx cy rx ry fill opacity drift-x drift-y period
BLOOM = [
    (250, 150, 330, 210, "#2E1B57", 0.46, 70, -40, 29),
    (930, 300, 380, 240, "#1E1238", 0.52, -90, 30, 37),
    (640, 120, 250, 160, "#3A2270", 0.30, 60, 50, 23),
    (1090, 360, 230, 180, "#241640", 0.38, -70, -50, 41),
]


def wrap(quote, limit=42):
    """Two balanced lines. Break at the word nearest the middle."""
    words = quote.split()
    best, gap = 1, None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        if len(a) > limit or len(b) > limit:
            continue
        d = abs(len(a) - len(b))
        if gap is None or d < gap:
            best, gap = i, d
    return [" ".join(words[:best]), " ".join(words[best:])]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def keyed(i, n):
    """opacity values and keyTimes for slot i of n, over the whole cycle."""
    total = n * HOLD
    t0, t1 = i * HOLD, (i + 1) * HOLD
    stops = [(0, 0), (t0, 0), (t0 + FADE, 1), (t1 - FADE, 1), (t1, 0), (total, 0)]
    # The first slot is already up at t=0, so it fades out at the end instead.
    if i == 0:
        stops = [(0, 1), (HOLD - FADE, 1), (HOLD, 0), (total - FADE, 0), (total, 1)]
    times, values = [], []
    for t, v in stops:
        k = min(round(t / total, 5), 1.0)
        if times and k <= times[-1]:
            values[-1] = v          # same instant, keep the later value
            continue
        times.append(k)
        values.append(v)
    if times[-1] != 1.0:
        times.append(1.0)
        values.append(values[-1])
    return ";".join(str(v) for v in values), ";".join(f"{t:.5f}" for t in times)


def quote_group(i, quote, n):
    values, times = keyed(i, n)
    lines = wrap(quote)
    size = 58 if max(len(l) for l in lines) <= 36 else 48
    text = "\n".join(
        f'    <text x="{W / 2}" y="{188 + j * (size + 18)}" text-anchor="middle" '
        f'font-family="{SERIF}" font-size="{size}" letter-spacing="-0.5" '
        f'fill="#F0EDE6">{esc(line)}</text>'
        for j, line in enumerate(lines)
    )
    return (
        f'  <g opacity="{1 if i == 0 else 0}">\n'
        f'    <animate attributeName="opacity" dur="{n * HOLD:.0f}s" '
        f'values="{values}" keyTimes="{times}" calcMode="linear" '
        f'repeatCount="indefinite"/>\n{text}\n  </g>'
    )


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
    f'    <ellipse cx="600" cy="200" rx="{rx}" ry="{ry}" stroke-opacity="{op}" stroke-width="{sw}"/>'
    for rx, ry, op, sw in ((470, 196, 0.40, 1.8), (392, 158, 0.24, 1.4), (310, 120, 0.13, 1.2))
)

quotes = "\n".join(quote_group(i, q, len(QUOTES)) for i, q in enumerate(QUOTES))

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

{quotes}
</svg>
'''

if __name__ == "__main__":
    open("header.svg", "w").write(svg)
    print("header.svg", len(svg), "bytes")

    # self-check: every wrap fits, every keyTimes list is legal
    for q in QUOTES:
        lines = wrap(q)
        assert len(lines) == 2 and all(l for l in lines), q
        assert max(len(l) for l in lines) <= 42, q
    for i in range(len(QUOTES)):
        v, t = keyed(i, len(QUOTES))
        ts = [float(x) for x in t.split(";")]
        assert ts[0] == 0 and ts[-1] == 1, i
        assert all(b > a for a, b in zip(ts, ts[1:])), i
        assert len(v.split(";")) == len(ts), i
    print("checks passed")
