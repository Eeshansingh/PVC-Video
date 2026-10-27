"""upscale_panels.py: 4x upscale every cropped panel with OpenCV's EDSR model, then a light sharpen.
usage: python tools/upscale_panels.py panels/crop panels/hd /path/to/EDSR_x4.pb
Skips panels that are already done, so it can be re-run safely."""
import cv2, os, sys, time

src, out, model = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel(model)
sr.setModel('edsr', 4)
for name in sorted(os.listdir(src)):
    dst = os.path.join(out, os.path.splitext(name)[0] + '.jpg')
    if os.path.exists(dst):
        continue
    t = time.time()
    up = sr.upsample(cv2.imread(os.path.join(src, name)))
    blur = cv2.GaussianBlur(up, (0, 0), 1.2)
    up = cv2.addWeighted(up, 1.25, blur, -0.25, 0)
    cv2.imwrite(dst, up, [cv2.IMWRITE_JPEG_QUALITY, 92])
    print(name, up.shape[1], 'x', up.shape[0], round(time.time() - t), 's', flush=True)
