"""build_spreads.py: rebuild each page spread at 4x, with the upscaled panels pasted in place.
usage: python tools/build_spreads.py source/pages panels/boxes.json panels/hd proj/media
Gutters, titles and footnotes come from a plain 4x resize; panels that are not upscaled yet fall back to it too."""
import cv2, json, os, sys
import numpy as np

src, bj, hd, out = sys.argv[1:5]
os.makedirs(out, exist_ok=True)
boxes = json.load(open(bj))
for page, lst in boxes.items():
    if page.startswith('_'):
        continue
    img = cv2.imread(os.path.join(src, f'page{page}.webp'))
    big = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)
    # tint the page outside the panels (margins, gutters, footnotes) to the film's paper colour (#EFE6D2)
    # with a multiply, so white margins never flash during camera moves and the lettering stays black
    paper = (big.astype('float32') * [210 / 255, 230 / 255, 239 / 255]).astype('uint8')
    big = paper
    done = 0
    for k, (x0, y0, x1, y1) in enumerate(lst, 1):
        f = os.path.join(hd, f'p{page}_{k:02d}.jpg')
        if not os.path.exists(f):
            continue
        up = cv2.imread(f)
        # the page white around the panel (and around balloons that spill past its border) gets the paper tint too:
        # flood from the corners through near-white pixels; balloon outlines stop the fill
        mask = np.zeros((up.shape[0] + 2, up.shape[1] + 2), np.uint8)
        light = (cv2.cvtColor(up, cv2.COLOR_BGR2GRAY) > 225).astype(np.uint8) * 255
        for cx, cy in [(0, 0), (up.shape[1] - 1, 0), (0, up.shape[0] - 1), (up.shape[1] - 1, up.shape[0] - 1)]:
            if light[cy, cx]:
                cv2.floodFill(light, mask, (cx, cy), 128)
        out_px = light == 128
        up[out_px] = (up[out_px].astype('float32') * [210 / 255, 230 / 255, 239 / 255]).astype('uint8')
        X, Y = max(0, x0 - 2) * 4, max(0, y0 - 2) * 4
        h, w = min(up.shape[0], big.shape[0] - Y), min(up.shape[1], big.shape[1] - X)
        big[Y:Y + h, X:X + w] = up[:h, :w]
        done += 1
    if page == '5':   # his portrait from the last panel, for the title and end cards
        cv2.imwrite(os.path.join(out, 'portrait.jpg'), big[516 * 4:786 * 4, 925 * 4:1085 * 4], [cv2.IMWRITE_JPEG_QUALITY, 92])
    cv2.imwrite(os.path.join(out, f'spread{page}.jpg'), big, [cv2.IMWRITE_JPEG_QUALITY, 88])
    print(f'spread{page}: {big.shape[1]} x {big.shape[0]}, {done}/{len(lst)} panels upscaled')
