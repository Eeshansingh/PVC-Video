"""crop_panels.py: cut each panel out of the page spreads using panels/boxes.json.
usage: python tools/crop_panels.py source/pages panels/boxes.json panels/crop"""
import cv2, json, os, sys

src, bj, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
boxes = json.load(open(bj))
n = 0
for page, lst in boxes.items():
    if page.startswith('_'):
        continue
    img = cv2.imread(os.path.join(src, f'page{page}.webp'))
    H, W = img.shape[:2]
    for k, (x0, y0, x1, y1) in enumerate(lst, 1):
        crop = img[max(0, y0 - 2):min(H, y1 + 3), max(0, x0 - 2):min(W, x1 + 3)]
        cv2.imwrite(os.path.join(out, f'p{page}_{k:02d}.png'), crop)
        n += 1
print(n, 'panels')
