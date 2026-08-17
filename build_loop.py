"""Build a seamless dissolve loop from the captured numinous frames.

Frames are independent samples: numinous randomises theme, palette and quote on
every load, so they cannot be played as motion. Crossfading them slowly reads
the way the site does anyway, and each dissolve changes the palette.
"""

import subprocess

PICK = ["00", "03", "06", "09", "11", "13", "15", "16"]
HOLD, FADE = 2.2, 1.1          # seconds up, seconds of crossfade
CROP = "crop=1010:520:0:112"   # drop the wordmark, buttons and the side panel
SCALE = "scale=940:-2"

seq = PICK + [PICK[0]]          # come back to the first so the loop closes
step = HOLD - FADE

cmd = ["ffmpeg", "-loglevel", "error", "-y"]
for f in seq:
    cmd += ["-loop", "1", "-t", str(HOLD), "-i", f"frames/f{f}.png"]

chain, prev = [], "0:v"
for i in range(1, len(seq)):
    out = f"v{i}"
    offset = i * step
    chain.append(
        f"[{prev}][{i}:v]xfade=transition=fade:duration={FADE}:offset={offset:.2f}[{out}]"
    )
    prev = out
chain.append(f"[{prev}]{CROP},{SCALE},fps=10[out]")

# ffmpeg here has no webp encoder, so render the dissolve to stills and let
# libwebp's img2webp assemble the animation.
cmd += ["-filter_complex", ";".join(chain), "-map", "[out]", "out/%03d.png"]

import glob, os, shutil
shutil.rmtree("out", ignore_errors=True)
os.makedirs("out")
subprocess.run(cmd, check=True)

stills = sorted(glob.glob("out/*.png"))
subprocess.run(["img2webp", "-loop", "0", "-lossy", "-d", "100", "-q", "52", "-m", "4",
                *stills, "-o", "numinous.webp"], check=True)
print(f"built numinous.webp from {len(stills)} frames")
