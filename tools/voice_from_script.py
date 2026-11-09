"""voice_from_script.py: record every numbered line of a script sheet with Sarvam Bulbul v3, then join them
with the sheet's pauses into one narration track and a timing file.
usage: python3 tools/voice_from_script.py script/badgam_longform_script_v2.md voice/longform [speaker] [temperature]
Reads table rows "| n | line | pace | pause | tag |". Skips lines already recorded, so it can be re-run.
Writes <out>/lNN.wav, <out>/timing.json (start and end of each line) and <out>/narration.wav (48 kHz, -16 LUFS).
The Sarvam key comes from the session's network proxy, or from SARVAM_API_KEY outside it."""
import base64, json, os, re, subprocess, sys, urllib.request, wave

src, out = sys.argv[1], sys.argv[2]
speaker = sys.argv[3] if len(sys.argv) > 3 else 'anand'
temp = float(sys.argv[4]) if len(sys.argv) > 4 else 0.75
os.makedirs(out, exist_ok=True)
rows = []
for l in open(src, encoding='utf8'):
    m = re.match(r'^\|\s*(\d+)\s*\|(.+?)\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|', l)
    if m:
        rows.append({'n': int(m.group(1)), 'text': m.group(2).strip(), 'pace': float(m.group(3)), 'pause': float(m.group(4))})


def tts(text, pace, use_temp=True):
    body = {'text': text, 'target_language_code': 'hi-IN', 'speaker': speaker, 'model': 'bulbul:v3',
            'pace': pace, 'speech_sample_rate': 48000}
    if use_temp:
        body['temperature'] = temp
    req = urllib.request.Request('https://api.sarvam.ai/text-to-speech', data=json.dumps(body).encode(), method='POST',
                                 headers={'Content-Type': 'application/json',
                                          'api-subscription-key': os.environ.get('SARVAM_API_KEY', 'proxy-injected')})
    return json.load(urllib.request.urlopen(req, timeout=120))


use_temp = True
for r in rows:
    f = os.path.join(out, f"l{r['n']:02d}.wav")
    if os.path.exists(f):
        continue
    try:
        d = tts(r['text'], r['pace'], use_temp)
    except urllib.error.HTTPError as e:
        msg = e.read().decode()[:300]
        if use_temp and 'temperature' in msg:
            use_temp = False
            d = tts(r['text'], r['pace'], False)
        else:
            sys.exit(f"line {r['n']}: {msg}")
    open(f, 'wb').write(base64.b64decode(''.join(d['audios'])))
    print(f"l{r['n']:02d} ok", flush=True)

# join: each line, then its pause, as 48 kHz mono
t, timing, parts = 0.0, [], []
for r in rows:
    f = os.path.join(out, f"l{r['n']:02d}.wav")
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f],
                               capture_output=True, text=True).stdout)
    timing.append({'n': r['n'], 'start': round(t, 3), 'end': round(t + dur, 3), 'pause': r['pause'], 'text': r['text']})
    parts.append((f, r['pause']))
    t += dur + r['pause']
json.dump({'total': round(t, 3), 'lines': timing}, open(os.path.join(out, 'timing.json'), 'w'), ensure_ascii=False, indent=1)
lst = os.path.join(out, 'concat.txt')
with open(lst, 'w') as c:
    for i, (f, p) in enumerate(parts):
        c.write(f"file '{os.path.abspath(f)}'\n")
        if p > 0:
            sil = os.path.join(out, f'sil_{int(p * 1000)}.wav')
            if not os.path.exists(sil):
                subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=mono', '-t', str(p), sil], check=True)
            c.write(f"file '{os.path.abspath(sil)}'\n")
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst,
                '-af', 'aresample=48000,aformat=channel_layouts=mono,loudnorm=I=-16:TP=-1.5:LRA=11',
                '-ar', '48000', os.path.join(out, 'narration.wav')], check=True)
print(f"total {t:.1f} s ({int(t // 60)}:{t % 60:04.1f}), {len(rows)} lines")
