#!/usr/bin/env bash
# mix_film.sh: voice over the score, music ducked under the voice, mastered to -14 LUFS, peaks at -1.5 dBTP.
# usage: bash tools/mix_film.sh voice/longform/narration.wav voice/longform/score.wav 0.8 out/film-mix.wav
set -e
V=$1; M=$2; OFF=$3; OUT=$4
ffmpeg -v error -y -i "$V" -i "$M" -filter_complex "\
[0]aresample=48000,adelay=$(python3 -c "print(int($OFF*1000))"):all=1,aformat=channel_layouts=stereo,apad=whole_dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"),asplit=2[v][sc];\
[1]aresample=48000,volume=-14dB[m];\
[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=40:release=600[md];\
[v][md]amix=inputs=2:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[out]" \
  -map "[out]" -ar 48000 "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
