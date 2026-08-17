#!/bin/zsh
cd /private/tmp/claude-501/-Users-abhay-Desktop-Playground/013149b9-b52f-4a0c-9929-36701edc7534/scratchpad
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
mkdir -p frames
i=0
for t in 5000 5000 5600 6200 6800 7400 8000 8600 9200 9800 10400 11000 11600 12200 12800 13400 14000; do
  n=$(printf "%02d" $i)
  "$C" --headless=new --virtual-time-budget=$t --screenshot=frames/f$n.png \
       --window-size=1200,760 https://www.numinous.one >/dev/null 2>&1
  i=$((i+1))
done
md5 -q frames/f00.png frames/f01.png > frames/determinism.txt
ls frames/*.png | wc -l >> frames/determinism.txt
