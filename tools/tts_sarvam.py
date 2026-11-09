"""tts_sarvam.py: speak each narration line with Sarvam Bulbul v3 (Hindi) and save line01.wav, line02.wav, ...
usage: python3 tools/tts_sarvam.py voice/lines.json voice [speaker] [pace]
The API key is never read here: the session's network proxy adds it to requests for api.sarvam.ai.
Outside such a proxy, set SARVAM_API_KEY and it is sent in the api-subscription-key header."""
import base64, json, os, subprocess, sys, urllib.request

src, out = sys.argv[1], sys.argv[2]
speaker = sys.argv[3] if len(sys.argv) > 3 else 'anand'
pace = float(sys.argv[4]) if len(sys.argv) > 4 else 0.9
lines = json.load(open(src))
for i, text in enumerate(lines, 1):
    dst = os.path.join(out, f'line{i:02d}.wav')
    body = json.dumps({'text': text, 'target_language_code': 'hi-IN', 'speaker': speaker,
                       'model': 'bulbul:v3', 'pace': pace}).encode()
    req = urllib.request.Request('https://api.sarvam.ai/text-to-speech', data=body, method='POST',
                                 headers={'Content-Type': 'application/json',
                                          'api-subscription-key': os.environ.get('SARVAM_API_KEY', 'proxy-injected')})
    d = json.load(urllib.request.urlopen(req, timeout=120))
    open(dst, 'wb').write(base64.b64decode(''.join(d['audios'])))
    dur = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', dst],
                         capture_output=True, text=True).stdout.strip()
    print(f'line{i:02d}: {float(dur):.2f} s  {text[:40]}')
