"""plan.py: the single source of timing for the film.
usage: python tools/plan.py
Reads panels/boxes.json and the beat list below. Writes proj/beats.js (used by proj/index.html)
and storyboard.json (the shot table). Times are in seconds.

Reading time per panel: 1.2 s + 1 s per 5 words of lettering, held between 2.2 s and 7.5 s."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCALE = 4            # panels were upscaled 4x, so world pixels = page pixels x 4
GAP = 640            # world pixels of paper between two spreads
PAGE_SIZE = {'1': (1400, 862), '2': (1372, 891), '3': (1402, 840), '4': (1378, 868), '5': (1406, 840)}

# words of lettering in each panel (captions + balloons), counted by hand from the pages
WORDS = {
    'p1_01': 52, 'p1_02': 52, 'p1_03': 36, 'p1_04': 22, 'p1_05': 22, 'p1_06': 8, 'p1_07': 18,
    'p2_01': 32, 'p2_02': 9, 'p2_03': 21, 'p2_04': 24, 'p2_05': 26, 'p2_06': 36, 'p2_07': 29,
    'p2_08': 67, 'p2_09': 49, 'p2_10': 29,
    'p3_01': 37, 'p3_02': 47, 'p3_03': 29, 'p3_04': 23, 'p3_05': 22, 'p3_06': 6, 'p3_07': 23,
    'p3_08': 36, 'p3_09': 17, 'p3_10': 14,
    'p4_01': 17, 'p4_02': 29, 'p4_03': 29, 'p4_04': 27, 'p4_05': 0, 'p4_06': 18, 'p4_07': 15,
    'p5_01': 17, 'p5_02': 14, 'p5_03': 9, 'p5_04': 12, 'p5_05': 22, 'p5_06': 16, 'p5_07': 17,
    'p5_08': 38,
}
# what each panel shows, for the storyboard table
WHAT = {
    'p1_01': 'Little Som tells his father he wants to join the army', 'p1_02': 'Father: study for the I.C.S.; Som: the army',
    'p1_03': 'Waiting to meet Maj Gen Bruce Hey, Lucknow', 'p1_04': 'Inducted into the military college at ten',
    'p1_05': 'Commissioned from I.M.A. in 1942, aged 19', 'p1_06': 'Burma campaign: an explosion, a man down',
    'p1_07': 'Somnath refuses to leave Bahadur behind', 'p2_01': 'Ordered to drop the wounded man; he refuses',
    'p2_02': 'Somnath runs back to camp carrying him', 'p2_03': 'Bahadur survives', 'p2_04': '31 Oct 1947: arm in plaster, going anyway',
    'p2_05': 'His mother worries', 'p2_06': '"The bullet with my name on it..."', 'p2_07': '4 Kumaon, Delta Company commander',
    'p2_08': 'Raiders invade Kashmir; the Maharaja signs the accession', 'p2_09': '4 Kumaon ordered to the Srinagar airstrip',
    'p2_10': '"My men know the way I function. I must go."', 'p3_01': 'Arrival at the Srinagar airstrip',
    'p3_02': '2 Nov: reports of raiders in the hills', 'p3_03': '3 Nov: companies sent to survey Badgam',
    'p3_04': 'Only refugees in the nala, it seems', 'p3_05': '14:30: the "refugees" start leaving',
    'p3_06': 'Ambush', 'p3_07': '70 men against about 1,000 raiders', 'p3_08': 'Surrounded on three sides; holding',
    'p3_09': 'Chalk markings for the air force', 'p3_10': 'Spitfires arrive', 'p4_01': 'Keep fighting',
    'p4_02': '"We\'ll fight to the last man and last round."', 'p4_03': 'He mans a machine gun himself',
    'p4_04': 'A shell lands on the ammunition', 'p4_05': 'The blast', 'p4_06': 'He lies among the dead, aged 24',
    'p4_07': 'Sepoy Dewan Singh charges: "For Somi Sa\'ab!"', 'p5_01': 'The men fight on', 'p5_02': 'Dewan Singh falls',
    'p5_03': 'The intruders retreat', 'p5_04': 'Enough time won for reinforcements', 'p5_05': 'The cost: 20 dead, 26 wounded',
    'p5_06': 'The enemy withdraws from the airfield', 'p5_07': '"The airfield is now secure."', 'p5_08': 'Param Vir Chakra, the first',
}
# chapter cards: (shown before this panel, big line, small line)
CARDS = {
    'p1_01': None,
    'p1_06': ('BURMA', 'World War II'),
    'p2_04': ('OCTOBER 1947', 'A call to Kashmir'),
    'p3_01': ('SRINAGAR', '31 October 1947'),
    'p3_03': ('BADGAM', '3 November 1947'),
}
TITLE = ('MAJOR SOMNATH SHARMA', 'The first Param Vir Chakra', '1923 – 1947')
END = ('PARAM VIR CHAKRA', 'The first. 1947.', 'Major Somnath Sharma, 4 Kumaon')

MOVE = 0.9          # camera move between panels on one spread
MOVE_SPREAD = 1.6   # camera move from one spread to the next
CARD_IN, CARD_OUT = 0.7, 0.5
TITLE_HOLD, CARD_HOLD, END_HOLD = 4.2, 2.4, 5.0


def hold(pid):
    return round(min(7.5, max(2.2, 1.2 + WORDS[pid] / 5)), 2)


boxes = json.load(open(os.path.join(ROOT, 'panels', 'boxes.json')))
spreads, panels, x = [], [], 0
for page in sorted(k for k in boxes if not k.startswith('_')):
    w, h = PAGE_SIZE[page]
    spreads.append({'page': page, 'x': x, 'w': w * SCALE, 'h': h * SCALE, 'src': f'media/spread{page}.jpg'})
    for k, (x0, y0, x1, y1) in enumerate(boxes[page], 1):
        panels.append({'id': f'p{page}_{k:02d}', 'page': page,
                       'box': [x + x0 * SCALE, y0 * SCALE, x + x1 * SCALE, y1 * SCALE]})
    x += w * SCALE + GAP

# walk the beats and give every one a time
t = 0.0
cards = [{'kind': 'title', 'lines': TITLE, 'in': -1, 'out': TITLE_HOLD}]
t = TITLE_HOLD + CARD_OUT
shots = [{'time': f'0.0-{t:.1f}', 'graphic': 'Title card: ' + ' / '.join(TITLE), 'asset': {'kind': 'code'}}]
for i, p in enumerate(panels):
    card = CARDS.get(p['id'])
    if card:
        c = {'kind': 'chapter', 'lines': card, 'in': t, 'out': t + CARD_IN + CARD_HOLD}
        cards.append(c)
        shots.append({'time': f'{t:.1f}-{c["out"] + CARD_OUT:.1f}', 'graphic': 'Chapter card: ' + ' / '.join(card),
                      'asset': {'kind': 'code'}})
        t = c['out'] + CARD_OUT
    p['arrive'] = round(t, 3)
    p['leave'] = round(t + hold(p['id']), 3)
    shots.append({'time': f'{t:.1f}-{p["leave"]:.1f}', 'graphic': f'{p["id"]}: {WHAT[p["id"]]}',
                  'asset': {'kind': 'user_photo', 'path': f'panels/hd/{p["id"]}.jpg'}})
    t = p['leave']
    nxt = panels[i + 1] if i + 1 < len(panels) else None
    if nxt and not CARDS.get(nxt['id']):
        p['move'] = MOVE_SPREAD if nxt['page'] != p['page'] else MOVE
        t += p['move']
    else:
        p['move'] = 0  # a card covers the change, or it is the last panel
end_in = t
cards.append({'kind': 'end', 'lines': END, 'in': end_in, 'out': 1e9})
D = round(end_in + CARD_IN + END_HOLD, 1)
shots.append({'time': f'{end_in:.1f}-{D:.1f}', 'graphic': 'End card: ' + ' / '.join(END), 'asset': {'kind': 'code'}})

beats = {'D': D, 'CARD_IN': CARD_IN, 'CARD_OUT': CARD_OUT, 'spreads': spreads, 'panels': panels, 'cards': cards}
with open(os.path.join(ROOT, 'proj', 'beats.js'), 'w') as f:
    f.write('// written by tools/plan.py. Do not edit by hand: change the plan and run it again.\n')
    f.write('window.BEATS = ' + json.dumps(beats, indent=1) + ';\n')
json.dump({'title': 'Major Somnath Sharma: the first Param Vir Chakra', 'format': '16:9', 'seconds': D,
           'shots': shots}, open(os.path.join(ROOT, 'storyboard.json'), 'w'), indent=1)
# keep the composition's length in step with the plan
html = os.path.join(ROOT, 'proj', 'index.html')
src = open(html).read()
open(html, 'w').write(re.sub(r'data-duration="[0-9.]+"', f'data-duration="{D}"', src, count=1))
print(f'{len(panels)} panels, {len(cards)} cards, {D} s ({int(D // 60)}:{D % 60:04.1f})')
