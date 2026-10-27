#!/usr/bin/env bash
# build.sh: rebuild the film from the comic pages.
# usage: bash build.sh [draft|high]
# Needs: Node 22+, ffmpeg, python3 with opencv-contrib-python-headless, the EDSR_x4.pb model
# (https://raw.githubusercontent.com/Saafke/EDSR_Tensorflow/master/models/EDSR_x4.pb) at $EDSR,
# and the Claude Video 2.0 skill at $SKILL (https://github.com/ItsssssJack/claude-video-2).
set -e
cd "$(dirname "$0")"
Q=${1:-draft}
SKILL=${SKILL:-$HOME/.claude/skills/claude-video-studio}
EDSR=${EDSR:-models/EDSR_x4.pb}
python3 tools/crop_panels.py source/pages panels/boxes.json panels/crop
python3 tools/upscale_panels.py panels/crop panels/hd "$EDSR"
python3 tools/build_spreads.py source/pages panels/boxes.json panels/hd proj/media
python3 tools/plan.py
bash "$SKILL/scripts/render.sh" proj "out/somnath-sharma-$Q.mp4" "$Q"
python3 "$SKILL/scripts/pacing_check.py" "out/somnath-sharma-$Q.mp4" --end-hold 5 || true
