# Brief: Major Somnath Sharma, a motion comic

- Format: 1920 x 1080, 30 fps, 297.7 s (4:58), does not loop, silent (music and voice belong in the edit).
- Source: the 5 comic spreads in `source/pages/` (about 1400 x 860 px each), in story order.
- Media: 42 panels cut by hand (`panels/boxes.json`), upscaled 4x with OpenCV EDSR, pasted back into 4x spreads.
- Style: `STYLE.md` (comic dossier). Ground #EFE6D2, ink #1C1A17, accent #D9772B. Stardos Stencil + Special Elite.
- Words added on screen (everything else is the comic's own lettering):
  - Title: MAJOR / SOMNATH SHARMA. "The first Param Vir Chakra". "1923 – 1947".
  - Chapters: BURMA (World War II) · OCTOBER 1947 (A call to Kashmir) · SRINAGAR (31 October 1947) · BADGAM (3 November 1947)
  - End: PARAM VIR CHAKRA. "The first. 1947." "Major Somnath Sharma, 4 Kumaon".
- Timing: `tools/plan.py` is the single source. Reading time per panel = 1.2 s + words / 5, clamped 2.2 to 7.5 s.
  Camera moves 0.9 s (same spread) or 1.6 s (next spread). Cards: 0.7 s in, 2.4 s hold, 0.5 s out.
- Ban list: no glow, no gradients, no linear easing on what the eye follows, one accent, no text over faces,
  no Math.random/Date.now.
- Deliberate exceptions to the skill's defaults:
  - Panels are centred (the panel is the frame).
  - Reading holds run up to 7.5 s with only a slow push, so the pacing check's 1 s dead-gap rule is expected to flag them.
