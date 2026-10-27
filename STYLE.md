# Comic dossier

id: comic-dossier (made for this film, from the comic pages in `source/pages/`)
Best for: motion comics, illustrated biographies, history told panel by panel.
Mood: an old service file on the desk. The comic does the talking; the film only points the reader's eye.
Reference piece: proj/index.html (297.7 s, does not loop)

## Palette (hex)
- ground (file paper): #EFE6D2
- ink: #1C1A17
- ink soft (small type): #5B554B
- veil (paper over the panels not being read): #EFE6D2 at 86%
- accent: #D9772B saffron. The ONE accent: only the rule above each card title.

## Type
- Display: Stardos Stencil 700, tracking 0.01em, line height 1.0. 112 px on title/end cards, 170 px on chapter cards.
- Labels: Special Elite 400, 50 px (subtitle) and 34 px (dates, credits) in ink soft.
- Font link (all free):
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Special+Elite&family=Stardos+Stencil:wght@400;700&display=swap">

## Easing (numbers)
- camera, panel to panel: power3.inOut, 0.9 s
- camera, spread to spread: power3.inOut, 1.6 s, pulling back (scale x e^-0.6 at the midpoint)
- push-in while a panel is read: sine.inOut, +5% over the whole hold
- card in: power3.inOut, 0.7 s (slides up). Card out: power3.in, 0.5 s (slides up and away)
- card type: masked rise, expo.out 0.65 s, 0.1 s stagger, starting 0.35 s after the card starts

## Motion rules
- One panel at a time. The camera frames it inside a 1680 x 920 safe area; everything else sits under the paper veil.
- Holds are reading time: 1.2 s + 1 s per 5 words of lettering, between 2.2 s and 7.5 s.
- The camera never stops: every hold is a slow push-in.
- Crossing to the next spread, the reading window closes to a point and opens on the new panel.
- A chapter card covers every jump in time or place; the camera moves while it is covered.

## Signature moves
- The paper veil that follows the reader's eye.
- Stencil chapter cards with one saffron rule.
- His portrait from the last panel, on the right of the title and end cards.

## Composition
- Cards: type hangs off a 144 px left margin; portrait strip is 480 px wide, flush right, behind an 8 px ink edge.
- Panels: centred by the camera (this style allows it: the panel is the frame).

## With media
- The media IS the comic: page spreads rebuilt at 4x with EDSR-upscaled panels.

## Ban list
- added text over the art (the comic is already lettered)
- covering any face with type or veil
- a second accent colour, glow, gradients
- Math.random or Date.now
