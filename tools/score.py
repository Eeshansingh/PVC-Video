"""score.py: synthesise the music and sound bed for the long-form film, keyed to the narration lines.
usage: python tools/score.py film/beats.js voice/longform/score.wav
Everything is generated here (no samples), so it is free of copyright claims. Same input, same output (seeded).
Cues (line numbers are the script's):
  cold open    low drone in D, distant shots from line 3, radio crackle at line 4
  childhood    sparse plucked notes (D minor pentatonic) from line 11
  October 1947 drone returns, a slow heartbeat pulse from line 27
  the patrol   pulse quickens from line 39; held tension from line 46
  the attack   drums at 96 bpm, gunfire, mortar thuds from line 50 to line 62
  the message  everything drops to one high drone at line 63, radio crackle
  the shell    one deep boom, then 3 s of wind only (line 69)
  aftermath    slow string chords Dm, Bb, F, C from line 72, brighter for the medal from line 80
  the close    the chords resolve and fade with the end screen"""
import json, sys
import numpy as np
from scipy.signal import butter, sosfilt

src, out = sys.argv[1], sys.argv[2]
B = json.loads(open(src, encoding='utf8').read().split('=', 1)[1].strip().rstrip(';'))
SR = 48000
D = B['D']
N = int(D * SR)
L = lambda n: B['lines'][n - 1]['s']
E = lambda n: B['lines'][n - 1]['e']
rng = np.random.default_rng(1947)
t = np.arange(N) / SR
mix = np.zeros(N)


def lp(x, f, o=2):
    return sosfilt(butter(o, f / (SR / 2), 'low', output='sos'), x)


def bp(x, a, b, o=2):
    return sosfilt(butter(o, [a / (SR / 2), b / (SR / 2)], 'band', output='sos'), x)


def env(a, b, fi=2.0, fo=2.0):
    """1 between a and b with fades, as an array over the whole film"""
    e = np.clip((t - a) / fi, 0, 1) * np.clip((b - t) / fo, 0, 1)
    return e * e * (3 - 2 * e)


def saw(f, detune=0.0):
    ph = (t * f * (1 + detune)) % 1.0
    return 2 * ph - 1


def drone(freqs, amp, a, b, cut=600, fi=3, fo=3):
    s = np.zeros(N)
    for f in freqs:
        s += saw(f, 0.002) + saw(f, -0.0025)
    s = lp(s, cut, 2) * (0.85 + 0.15 * np.sin(2 * np.pi * 0.07 * t))
    return s / len(freqs) * amp * env(a, b, fi, fo)


def pluck(f, at, amp, dec=1.6):
    """Karplus-Strong string"""
    n = int(SR * (dec + 0.5))
    p = int(SR / f)
    buf = rng.uniform(-1, 1, p)
    y = np.zeros(n)
    for i in range(n):
        y[i] = buf[i % p]
        buf[i % p] = 0.996 * 0.5 * (buf[i % p] + buf[(i + 1) % p])
    i0 = int(at * SR)
    seg = y[:max(0, min(n, N - i0))] * amp
    mix[i0:i0 + len(seg)] += seg


def hit(at, amp, f0=55, dec=0.5, noise=0.3):
    """a low drum: pitched thump plus a little noise"""
    n = int(SR * dec * 2)
    tt = np.arange(n) / SR
    s = np.sin(2 * np.pi * f0 * tt * (1 + 0.6 * np.exp(-tt * 18))) * np.exp(-tt / dec * 3)
    s += lp(rng.standard_normal(n), 400) * noise * np.exp(-tt * 20)
    i0 = int(at * SR)
    m = max(0, min(n, N - i0))
    mix[i0:i0 + m] += s[:m] * amp


def shot(at, amp):
    """a distant rifle shot: a filtered crack with a short tail"""
    n = int(SR * 0.6)
    tt = np.arange(n) / SR
    s = bp(rng.standard_normal(n), 300, 2500) * np.exp(-tt * 14)
    i0 = int(at * SR)
    m = max(0, min(n, N - i0))
    mix[i0:i0 + m] += s[:m] * amp


def radio(a, b, amp):
    n = int((b - a) * SR)
    s = bp(rng.standard_normal(n), 1200, 3400) * (0.6 + 0.4 * (rng.random(n) > 0.997))
    s *= np.minimum(1, np.minimum(np.arange(n), n - np.arange(n)) / (0.08 * SR))
    i0 = int(a * SR)
    mix[i0:i0 + n] += s[:max(0, min(n, N - i0))] * amp


# cold open
mix += drone([36.7, 55.0], 0.30, 0.0, L(7) + 2, cut=380)
for k in range(10):
    shot(L(3) + 0.9 + k * 0.55 + rng.random() * 0.4, 0.10 + 0.08 * rng.random())
radio(L(4) + 0.2, L(4) + 1.2, 0.05)
radio(L(5) - 0.5, L(5), 0.05)

# title and childhood: sparse plucks
mix += drone([73.4, 110.0], 0.12, L(7), L(11) + 2, cut=900)
scale = [146.8, 174.6, 196.0, 220.0, 261.6, 293.7]
tt0 = L(11)
k = 0
while tt0 < L(27) - 2:
    pluck(scale[(k * 3 + (k // 4)) % len(scale)] * (0.5 if k % 5 == 0 else 1), tt0, 0.10)
    tt0 += 1.6 + 0.4 * ((k * 7) % 3)
    k += 1
mix += drone([73.4, 146.8], 0.06, L(11), L(27), cut=700)

# October 1947: the drone returns with a heartbeat
mix += drone([36.7, 55.0, 73.4], 0.22, L(27) - 1, L(50), cut=500)
beat, tb = 1.0, L(27)
while tb < L(50):
    rate = 1.0 if tb < L(39) else 0.78 if tb < L(46) else 0.62
    hit(tb, 0.20, 48, 0.35, 0.1)
    hit(tb + 0.24, 0.12, 48, 0.3, 0.1)
    tb += rate

# the attack
mix += drone([36.7, 43.65, 55.0], 0.26, L(50) - 0.5, L(63) - 0.4, cut=650, fi=0.6, fo=0.6)
bpm = 96
tb, k = L(50), 0
while tb < L(63) - 0.6:
    hit(tb, 0.32 if k % 4 == 0 else 0.18, 52 if k % 4 == 0 else 70, 0.45, 0.25)
    tb += 60 / bpm
    k += 1
for k in range(70):
    shot(L(50) + rng.random() * (L(63) - L(50) - 1), 0.05 + 0.07 * rng.random())
for k in range(12):
    hit(L(50) + 1 + rng.random() * (L(62) - L(50)), 0.28, 34, 0.9, 0.6)

# the message: one high drone, radio
mix += drone([293.7, 440.0], 0.06, L(63) - 0.3, L(69) + 2.2, cut=2400, fi=0.8, fo=0.05)
radio(L(63) + 0.4, L(63) + 1.4, 0.05)

# the shell: a deep boom, then wind only for 3 s
boom = L(69) + 2.2
hit(boom, 0.9, 30, 1.6, 1.2)
wind = lp(rng.standard_normal(N), 500) * (0.55 + 0.45 * np.sin(2 * np.pi * 0.13 * t))
mix += wind * 0.06 * env(boom + 0.2, L(72) + 4, 0.5, 3)

# aftermath and the medal: slow string chords
chords = [[73.4, 146.8, 174.6, 220.0], [58.3, 116.5, 146.8, 174.6], [87.3, 130.8, 174.6, 220.0], [65.4, 130.8, 164.8, 196.0]]
tc, k = L(72), 0
while tc < D - 4:
    dur = 7.5
    bright = 1.4 if tc > L(80) else 1.0
    mix += drone(chords[k % 4], 0.10 * bright, tc, tc + dur + 2, cut=1400 if tc > L(80) else 1000, fi=2.5, fo=3)
    tc += dur
    k += 1
mix *= env(0, D - 0.3, 0.5, 2.5)
mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.7
from scipy.io import wavfile
wavfile.write(out, SR, np.stack([mix, mix], 1).astype(np.float32))
print('wrote', out, round(D, 1), 's')
