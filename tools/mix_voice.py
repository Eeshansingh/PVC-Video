"""mix_voice.py: place each narration line at its cue and write one 48 kHz track, loudness-normalised to -16 LUFS.
usage: python3 tools/mix_voice.py voice/cues.json voice voice/narration.wav"""
import json, subprocess, sys

cues, folder, out = sys.argv[1:4]
c = json.load(open(cues))
ins, parts = [], []
for i, s in enumerate(c['starts'], 1):
    ins += ['-i', f'{folder}/line{i:02d}.wav']
    ms = int(s * 1000)
    parts.append(f'[{i - 1}]aresample=48000,aformat=channel_layouts=mono,adelay={ms}[a{i}]')
mix = ''.join(f'[a{i}]' for i in range(1, len(c['starts']) + 1))
graph = ';'.join(parts) + f';{mix}amix=inputs={len(c["starts"])}:normalize=0,apad=whole_dur={c["length"]},' \
        f'atrim=0:{c["length"]},loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[out]'
subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', graph, '-map', '[out]', '-ac', '2', out], check=True)
print('wrote', out)
