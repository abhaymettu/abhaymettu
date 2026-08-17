"""Phase portrait of a Van der Pol oscillator, with the line beside it.

Trajectories started anywhere in the plane spiral onto one closed orbit and
keep going round it. That orbit is the only thing in colour.
"""

W, H = 1200, 400
SERIF = "Newsreader, Georgia, 'Times New Roman', serif"
LINES = ["This loop keeps running only", "while you keep narrating it."]

MU = 1.6
CX, CY, SCALE = 870, 200, 44          # portrait centre and units-to-px

THEMES = {
    "light": dict(paper="#FCFCFA", ink="#17171B", soft="#6E6E77", under="#B4472F"),
    "dark":  dict(paper="#17171B", ink="#F2F2EE", soft="#9A9AA3", under="#D06A4F"),
}


def step(p, dt):
    """One RK4 step of x' = y, y' = mu(1 - x^2)y - x."""
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


def run(start, n, dt=0.012, skip=0):
    p = start
    for _ in range(skip):
        p = step(p, dt)
    pts = [p]
    for _ in range(n):
        p = step(p, dt)
        pts.append(p)
    return pts


def d(pts):
    out = []
    for x, y in pts:
        px, py = CX + x * SCALE, CY - y * SCALE
        if abs(px - CX) > 460 or abs(py - CY) > 250:   # keep it inside the plate
            continue
        out.append(f"{px:.1f},{py:.1f}")
    return "M" + " L".join(out) if out else ""


def svg(t):
    paths = []

    # Transients: start away from the orbit, spiral onto it, then stop.
    starts = [(0.05, 0.05), (0.2, 0.0), (-0.15, 0.1), (3.4, 1.6), (-3.4, -1.6),
              (2.6, -2.4), (-2.6, 2.4), (0.9, 3.1), (-0.9, -3.1), (3.9, 0.2),
              (-3.9, -0.2), (1.8, 2.8), (-1.8, -2.8)]
    for i, s in enumerate(starts):
        pts = run(s, 900)
        paths.append(
            f'  <path d="{d(pts)}" fill="none" stroke="{t["ink"]}" '
            f'stroke-opacity="{0.20 + 0.07 * (i % 3):.2f}" stroke-width="0.9"/>'
        )

    # The attractor itself: run long enough to be on it, then one lap.
    cycle = run((2.0, 0.0), 560, skip=1400)
    paths.append(
        f'  <path d="{d(cycle)}" fill="none" stroke="{t["under"]}" '
        f'stroke-opacity="0.95" stroke-width="1.9" stroke-linecap="round"/>'
    )

    text = "\n".join(
        f'  <text x="96" y="{178 + i * 54}" font-family="{SERIF}" font-size="41" '
        f'letter-spacing="-0.4" fill="{t["ink"]}">{line}</text>'
        for i, line in enumerate(LINES)
    )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img">\n'
        f'  <rect width="{W}" height="{H}" fill="{t["paper"]}"/>\n'
        + "\n".join(paths) + "\n" + text + "\n</svg>\n"
    )


if __name__ == "__main__":
    for name, theme in THEMES.items():
        open(f"header-{name}.svg", "w").write(svg(theme))
        print(f"header-{name}.svg")
