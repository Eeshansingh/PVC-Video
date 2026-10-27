# PVC Video: Major Somnath Sharma

A 4 min 58 s motion comic of Major Somnath Sharma, the first Param Vir Chakra, built from five comic
spreads (`source/pages/`) with the [Claude Video 2.0](https://github.com/ItsssssJack/claude-video-2) skill:
HTML + GSAP, rendered to MP4 with HyperFrames.

## How it was made
1. **Panels.** All 42 panels were boxed by hand (`panels/boxes.json`). `tools/crop_panels.py` cuts them out,
   and `tools/upscale_panels.py` upscales each one 4x with OpenCV's EDSR model. The source pages are only
   about 1400 px wide, so each panel was 250 to 550 px before upscaling.
2. **Spreads.** `tools/build_spreads.py` rebuilds each spread at 4x (5600 px wide) with the sharp panels
   pasted back in place. It also cuts his portrait for the title and end cards.
3. **Plan.** `tools/plan.py` times everything: reading time per panel from its word count, camera moves,
   and chapter cards. It writes `proj/beats.js` and `storyboard.json`.
4. **Film.** `proj/index.html` is one camera moving over the spreads. A paper veil covers every panel
   except the one being read, a slow push runs during each hold, and stencil chapter cards cover each
   jump in time.

Read `BRIEF.md` for the numbers and `STYLE.md` for the look.

## Rebuild
`bash build.sh draft` or `bash build.sh high`. The comments at the top of `build.sh` list what it needs.

## Story beats
Title → childhood (early 1930s) → BURMA (WWII, saving Bahadur) → OCTOBER 1947 (going to Kashmir with a
broken arm) → SRINAGAR (31 Oct) → BADGAM (3 Nov: the ambush, the last stand, Dewan Singh) → the airfield
held → Param Vir Chakra.
