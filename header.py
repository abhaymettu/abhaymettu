"""The header: a Van der Pol flow field with its limit cycle drawn once.

Every hairline is a trajectory released somewhere in the plane and followed
forward in time. Wherever it starts it is pulled onto the same closed orbit
and then runs round it forever, which is the object the line names. The orbit
is the only thing in colour, the same accent the research site spends once.

Real RK4 integration of x' = y, y' = mu(1 - x^2)y - x, so the shape is the
attractor rather than a drawing of one. Deterministic from SEED.

    python3 header.py        # writes cycle-light.svg and cycle-dark.svg
"""

import random

W, H = 1200, 420
SERIF = "Newsreader, Georgia, 'Times New Roman', serif"
LINES = ["This loop keeps running only", "while you keep narrating it"]

MU = 1.7
CX, CY, SCALE = 838, 210, 41          # portrait centre and units-to-px
SEED = 5

THEMES = {
    "light": dict(paper="#FCFCFA", ink="#17171B", under="#B4472F", flow=0.16),
    "dark":  dict(paper="#17171B", ink="#F2F2EE", under="#D86A4C", flow=0.20),
}


def step(p, dt):
    def f(s):
        x, y = s
        return (y, MU * (1 - x * x) * y - x)

    def add(s, d, k):
        return (s[0] + d * k[0], s[1] + d * k[1])

    k1 = f(p)
    k2 = f(add(p, dt / 2, k1))
    k3 = f(add(p, dt / 2, k2))
    k4 = f(add(p, dt, k3))
    return (p[0] + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
            p[1] + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))


def trace(start, n, dt=0.009, skip=0):
    p = start
    for _ in range(skip):
        p = step(p, dt)
    pts = [p]
    for _ in range(n):
        p = step(p, dt)
        pts.append(p)
        if abs(p[0]) > 14 or abs(p[1]) > 9:      # ran off, stop following it
            break
    return pts


def draw(pts):
    """Path data, cut into runs so a trajectory that leaves the frame does not
    come back as a straight line across it."""
    runs, cur = [], []
    for x, y in pts:
        px, py = CX + x * SCALE, CY - y * SCALE
        if -60 < px < W + 60 and -60 < py < H + 60:
            cur.append(f"{px:.1f},{py:.1f}")
        elif cur:
            runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    return " ".join("M" + " L".join(r) for r in runs if len(r) > 3)


def field():
    """Seeds on two rings outside the orbit and a few inside it, so every line
    is a visible spiral onto the cycle rather than a streak across the frame."""
    import math
    rng = random.Random(SEED)
    seeds = []
    for ring, n in ((3.5, 24), (4.9, 18)):
        for i in range(n):
            a = 2 * math.pi * i / n + rng.uniform(-.05, .05)
            seeds.append((ring * math.cos(a) * 1.05, ring * math.sin(a) * 0.52))
    for i in range(7):                      # inside: the unstable spiral outward
        seeds.append((0.05 + 0.16 * i, 0.04 * (1 if i % 2 else -1)))
    return seeds


def svg(t):
    out = []
    for i, s in enumerate(field()):
        d = draw(trace(s, 520, dt=0.017))
        if not d:
            continue
        out.append(
            f'  <path d="{d}" fill="none" stroke="{t["ink"]}" '
            f'stroke-opacity="{t["flow"] * (1.15 + 0.35 * (i % 3)):.3f}" '
            f'stroke-width="0.85"/>'
        )

    # On the attractor already, then one full lap. A paper casing goes under it
    # so the transients that arrive and hug the orbit do not double the line.
    lap = draw(trace((2.0, 0.0), 415, dt=0.017, skip=900))
    out.append(
        f'  <path d="{lap}" fill="none" stroke="{t["paper"]}" stroke-width="7"/>'
    )
    out.append(
        f'  <path d="{lap}" fill="none" '
        f'stroke="{t["under"]}" stroke-opacity="0.96" stroke-width="2.1" '
        f'stroke-linecap="round"/>'
    )

    text = "\n".join(
        f'  <text x="92" y="{188 + i * 56}" font-family="{SERIF}" font-size="43" '
        f'letter-spacing="-0.4" fill="{t["ink"]}">{line}</text>'
        for i, line in enumerate(LINES)
    )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img">\n'
        f'  <defs>\n'
        f'    <linearGradient id="fade" x1="0" x2="1">\n'
        f'      <stop offset="0" stop-color="{t["paper"]}" stop-opacity="0.985"/>\n'
        f'      <stop offset="0.42" stop-color="{t["paper"]}" stop-opacity="0.62"/>\n'
        f'      <stop offset="0.74" stop-color="{t["paper"]}" stop-opacity="0"/>\n'
        f'    </linearGradient>\n'
        f'  </defs>\n'
        f'  <rect width="{W}" height="{H}" fill="{t["paper"]}"/>\n'
        + "\n".join(out)
        + f'\n  <rect width="{W}" height="{H}" fill="url(#fade)"/>\n'
        + text
        + "\n</svg>\n"
    )


if __name__ == "__main__":
    for name, theme in THEMES.items():
        open(f"cycle-{name}.svg", "w").write(svg(theme))
        print(f"cycle-{name}.svg")
