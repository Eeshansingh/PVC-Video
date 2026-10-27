"""build_spreads.py: rebuild each page spread at 4x, with the upscaled panels pasted in place.
usage: python tools/build_spreads.py source/pages panels/boxes.json panels/hd proj/media
Gutters, titles and footnotes come from a plain 4x resize; panels that are not upscaled yet fall back to it too."""
import cv2, json, os, sys

src, bj, hd, out = sys.argv[1:5]
os.makedirs(out, exist_ok=True)
boxes = json.load(open(bj))
for page, lst in boxes.items():
    if page.startswith('_'):
        continue
    img = cv2.imread(os.path.join(src, f'page{page}.webp'))
    big = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)
    done = 0
    for k, (x0, y0, x1, y1) in enumerate(lst, 1):
        f = os.path.join(hd, f'p{page}_{k:02d}.jpg')
        if not os.path.exists(f):
            continue
        up = cv2.imread(f)
        X, Y = max(0, x0 - 2) * 4, max(0, y0 - 2) * 4
        h, w = min(up.shape[0], big.shape[0] - Y), min(up.shape[1], big.shape[1] - X)
        big[Y:Y + h, X:X + w] = up[:h, :w]
        done += 1
    if page == '5':   # his portrait from the last panel, for the title and end cards
        cv2.imwrite(os.path.join(out, 'portrait.jpg'), big[516 * 4:786 * 4, 925 * 4:1085 * 4], [cv2.IMWRITE_JPEG_QUALITY, 92])
    cv2.imwrite(os.path.join(out, f'spread{page}.jpg'), big, [cv2.IMWRITE_JPEG_QUALITY, 88])
    print(f'spread{page}: {big.shape[1]} x {big.shape[0]}, {done}/{len(lst)} panels upscaled')
