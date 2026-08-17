"""Generate the profile header, light and dark.

No words. Eighteen stacked densities, back to front, the distribution drifting
right and widening as it comes forward. One ridge is terracotta: the row where
the drift is large enough to be called, and the only colour on the page, the
same accent the research site spends exactly once.

Everything is deterministic from SEED, so the file regenerates byte for byte.

    python3 header.py        # writes header-light.svg and header-dark.svg
"""

import math
import random

W, H = 1200, 378
PAD = 96
X0, X1 = PAD, W - PAD

ROWS = 16
CALLED = 10               # counted from the back: the ridge that gets colour
STEP = 14.5               # vertical distance between baselines
AMP = 64                  # tallest ridge, in px
BASE_Y = 278              # baseline of the frontmost ridge
SEED = 11

LINE = "I want to measure depression without asking anyone how they feel."
MONO = "'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace"

THEMES = {
    "light": dict(paper="#FCFCFA", ink="#17171B", under="#B4472F", soft="#6E6E77"),
    "dark":  dict(paper="#17171B", ink="#F2F2EE", under="#D06A4F", soft="#9A9AA3"),
}


def density(row):
    """A two-bump mixture that drifts right and spreads as `row` moves forward."""
    rng = random.Random(SEED + row * 97)
    t = row / (ROWS - 1)
    jitter = lambda s: (rng.random() - 0.5) * s
    bumps = [
        # weight,           centre,                        width
        (1.00,               0.24 + 0.48 * t + jitter(.018), 0.062 + 0.020 * t + jitter(.004)),
        (0.26 + jitter(.14), 0.44 + 0.48 * t + jitter(.040), 0.105 + 0.030 * t + jitter(.010)),
    ]

    def f(x):
        return sum(w * math.exp(-0.5 * ((x - c) / s) ** 2) for w, c, s in bumps)

    peak = max(f(i / 400) for i in range(401))
    return lambda x: f(x) / peak


def path(row):
    """(open curve, closed shape) for one ridge. The curve is what gets stroked."""
    y0 = BASE_Y - (ROWS - 1 - row) * STEP
    # Ridges at the back are flatter, so the stack reads as depth rather than noise.
    amp = AMP * (0.80 + 0.20 * (row / (ROWS - 1)))
    f = density(row)
    pts = [
        f"{X0 + i / 160 * (X1 - X0):.1f},{y0 - amp * f(i / 160):.1f}"
        for i in range(161)
    ]
    curve = f"M{pts[0]} L" + " L".join(pts[1:])
    return curve, f"{curve} L{X1:.1f},{y0:.1f} L{X0:.1f},{y0:.1f} Z"


def svg(t):
    ridges = []
    for row in range(ROWS):
        front = row / (ROWS - 1)
        called = row == CALLED
        stroke = t["under"] if called else t["ink"]
        # Back ridges fade, so the eye lands on the front of the stack.
        opacity = 0.92 if called else 0.30 + 0.62 * front ** 1.3
        curve, closed = path(row)
        # Fill first, unstroked, so the ridge in front occludes the one behind
        # without drawing its own baseline.
        ridges.append(f'  <path d="{closed}" fill="{t["paper"]}"/>')
        ridges.append(
            f'  <path d="{curve}" fill="none" stroke="{stroke}" '
            f'stroke-opacity="{opacity:.3f}" stroke-width="{1.6 if called else 1.05}" '
            f'stroke-linecap="round"/>'
        )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img">\n'
        f'  <rect width="{W}" height="{H}" fill="{t["paper"]}"/>\n'
        + "\n".join(ridges)
        + f'\n  <text x="{PAD}" y="{H - 34}" font-family="{MONO}" font-size="13.5" '
          f'letter-spacing="0.2" fill="{t["soft"]}">{LINE}</text>'
        + "\n</svg>\n"
    )


if __name__ == "__main__":
    for name, theme in THEMES.items():
        open(f"header-{name}.svg", "w").write(svg(theme))
        print(f"header-{name}.svg")
