# Visuals, Animation Styles and Free Tools for Narrated Indian Military History Videos (PVC hero stories)

Research date: 2026-11-09. Note: many tool and pricing facts come from secondary blogs and aggregators, because official pages (support.google.com, lilys.ai) could not be fetched from this session. Confidence is flagged throughout. Items marked "(background knowledge, not verified this session)" come from the researcher's prior knowledge, not a source fetched here. The report writer should treat them as lower confidence or check them.

## 1. Which visual styles do successful narrated history channels use, and how often should visuals change?

### Takeaway
Top war-history channels (Kings and Generals, Epic History TV, History Marsh) are built on illustrated animated maps with unit arrows, plus illustrated stills. Secondhand evidence says they use Photoshop and After Effects, sometimes with hired map designers. No rigorous published shot-length norm exists for YouTube documentaries. Creator guidance points to a visual change (cut, zoom, overlay or map move) about every 3-8 s in long-form narration and every 2-3 s in Shorts. Visuals that are relevant to the narration matter more than the cut rate.

### Cited Findings
- A breakdown of how history animators make maps groups Kings and Generals, History Marsh and Epic History TV together because their map styles are similar. It says the workflow was confirmed for only one channel and assumed for the others. The stated workflow is Photoshop + After Effects for battle maps, with a hired professional map designer for unique maps. Some other creators use Blender or Unreal Engine for 3D. This is secondhand and not a statement from K&G. — [Lilys.ai summary of "How History Animators Make Their Maps" (Jan 2026)](https://lilys.ai/en/notes/map-animation-20260119/history-animators-maps)
- Freelancers selling "Kings and Generals / Vox / Johnny Harris style" map animations say they mainly use Adobe After Effects. — [Fiverr listing](https://fiverr.com/orhan0051/create-epic-historical-map-animations-like-vox-johnny-harris)
- Guidance on pacing varies a lot. One guide says to change visuals every 15-25 s and another says every 20-30 s. For narration-heavy videos, one guide says to change the main visual roughly every 3-5 s, "not forcing a hard cut every four seconds". — [Overseeros: how often should visuals change](https://www.overseeros.com/blog/how-often-should-visuals-change-youtube-video); [AIR Media-Tech retention editing](https://air.io/en/youtube-hacks/advanced-retention-editing-cutting-patterns-that-keep-viewers-past-minute-8)
- A controlled B-roll test (OpusClip blog) suggests B-roll clips of 3-8 s, cut on speech pauses. Watch-time gains appeared only when the B-roll directly illustrated what was being said. — [Opus.pro: Does B-roll increase watch time?](https://www.opus.pro/blog/does-b-roll-increase-watch-time)
- A faceless-Shorts analysis claims about 82% retention with a scene change every 2-3 s, versus 58% at 6+ s. The methodology is not disclosed, so the numbers are unverified. — [Fluxnote: faceless shorts retention tips 2026](https://fluxnote.io/guides/faceless-shorts-retention-tips-2026)
- YouTube's "inauthentic content" rule (renamed from "repetitious content" on 15 Jul 2025) names "narrated stories with only minor variations" and "slideshows with identical narration across multiple videos" as examples. It can demonetize a whole channel. YouTube says using AI does not by itself disqualify content. — [Social Media Today](https://www.socialmediatoday.com/news/youtube-clarifies-monetization-update-inauthentic-repeated-content/752892/); [Gulf News](https://gulfnews.com/technology/youtube-updates-monetisation-policies-ai-and-repetitive-content-ban-begins-july-15-1.500192660); [ppc.land](https://ppc.land/youtube-clarifies-inauthentic-content-policy-changes/)

### Inferences
- Style comparison for a solo creator. These are the researcher's judgements, built from the findings above and genre conventions:
  - **Animated maps** (K&G, Epic History TV, Armchair Historian) carry the "where and how" of a battle. They are essential for PVC stories: Zoji La, Shelatang, Naushera, Tithwal, Srinagar airfield. They are the most effort per minute but can be reused across videos.
  - **Archival photo + Ken Burns / 2.5D parallax** gives authenticity. The real hero's portrait matters for trust and for the inauthentic-content rule. Parallax (DepthFlow) turns a flat photo into a pseudo-3D shot cheaply.
  - **AI-illustrated frames (painterly or graphic-novel style)** fill the gap where no photos exist, which applies to almost all 1947-48 action moments. A stylised illustration avoids realistic gore and avoids implying that a "fake photo" is real.
  - **2D character animation** (Simple History style) is very high effort. It is not recommended for a solo creator except as small loops.
  - **Kinetic type / motion graphics** (dates, unit names, quotes, citation text) are cheap. They are especially good in Shorts and for the PVC citation.
  - **Stock footage** of modern Indian Army is generic and risks being historically wrong (1947 vs today's gear). Use it sparingly.
- Recommended mix for long-form, per 60 s: about 2-3 map beats, 3-5 illustrated or parallax stills, 1-2 archival photos, plus text overlays. Make a visual change every 3-6 s using zooms and parallax within shots, not only hard cuts.
- To stay clear of "inauthentic content", each video needs original scripting, distinct visuals and real research. Do not reuse the same template or narration structure with only the names swapped.

### Gaps
- No primary-source interviews from Kings and Generals, Simple History, Armchair Historian or Epic History TV about their tools were retrieved. lilys.ai was not reachable, so only the search snippet was available.
- No reliable measured average-shot-length data for YouTube history documentaries was found.

## 2. Free tools and pipelines (editing, animation, maps, parallax, AI images and video)

### Takeaway
A fully free, commercially safe stack exists. It is built on a core of DaVinci Resolve free (edit and Fusion), maps built from QGIS + Natural Earth (or Google Earth Studio, which requires approval) and animated in Resolve/Fusion or Blender, DepthFlow for parallax, FLUX.1 [schnell] (Apache 2.0) or SDXL locally for images, and Wan 2.2 (Apache 2.0) locally for image-to-video. Hosted free tiers (Kling, Gemini, Ideogram) carry watermarks, public-visibility or licence caveats. CapCut is reportedly banned in India.

### Cited Findings
- **DepthFlow** (2.5D parallax from a single image with an AI depth map) is dual-licensed: AGPL-3.0, or a commercial (MIT) licence. Using it to render video for YouTube does not distribute the software, so AGPL obligations should not apply to the output videos (inference). — [PyPI depthflow](https://pypi.org/project/depthflow); [GitTrend](https://gittrend.io/repo/BrokenSource/DepthFlow); [HF Space README](https://huggingface.co/spaces/BrokenSource/DepthFlow/blob/main/README.md?code=true)
- **Google Earth Studio**: free, runs only in desktop Chrome (WebAssembly), and requires an access request that Google approves by email. Its historical terms allowed free use for news, research, education and public interest work. It was still listed as available in 2026, but no official 2026 announcement was found. — [Google Earth Studio FAQ (hi)](https://www.google.com/intl/hi/earth/studio/faq/); [Earth Studio (hi)](https://www.google.com/intl/hi/earth/studio/); [creatoreconomytools 2026 listing](https://creatoreconomytools.com/tool/google-earth-studio); [ppc.land](https://ppc.land/google-earth-studio-now-available-for-newsrooms-and-for-free/)
- **FLUX.1 [schnell]** is Apache 2.0, so commercial use is allowed. **FLUX.1 [dev]** weights are under a non-commercial licence. The model card says outputs may be used commercially, but forum readings conflict. The safest route is schnell, or dev only through the BFL API or a commercial licence. — [HF FLUX.1-schnell discussion](https://huggingface.co/black-forest-labs/FLUX.1-schnell/discussions/55); [HF FLUX.1-dev discussion](https://huggingface.co/black-forest-labs/FLUX.1-dev/discussions/7); [PromptZone FLUX licence guide](https://www.promptzone.com/zuzanna_choi/flux-ai-license-key-insights-2g8d); [localaimaster licence comparison](https://localaimaster.com/blog/local-image-model-licenses-commercial-use)
- **Wan 2.2** (Alibaba) is open source under Apache 2.0, with text-to-video and image-to-video models. The 5B TI2V model runs on about 8 GB VRAM (one guide gives ~6 GB at 480p and ~10 GB at 720p) and takes ~6 min per clip on an RTX 4090. Reported VRAM needs for the 14B models are inconsistent: 8 GB with offload in one source, 80 GB in the README per another. — [Stable Diffusion Art: Wan 2.2 I2V](https://stable-diffusion-art.com/wan-2-2-image-to-video/); [computingforgeeks](https://computingforgeeks.com/run-wan-video-generation-locally/); [MindStudio](https://www.mindstudio.ai/blog/what-is-wan-2-2-video-open-source); [aifilms 8GB GGUF workflow](https://studio.aifilms.ai/blog/wan-2-2-gguf-8gb-vram-open-source-video-workflow)
- **Kling free tier**: through most of 2026, guides reported 66 daily credits with no rollover, enough for only a few short clips, with a watermark and 720p output. A 4 Nov 2026 report says daily credits now go only to subscribers and free accounts get a monthly login credit pack valid for 31 days. Only one source confirms this, so it is unconfirmed. — [aireiter Kling free tier 2026](https://aireiter.com/blog/kling-ai-free-tier-2026); [eesel Kling pricing](https://eesel.ai/blog/kling-ai-pricing); [LaoZhang blog, 4 Nov 2026](https://blog.laozhang.ai/en/posts/kling-daily-free-credits)
- **Gemini image generation (Nano Banana)**: secondary sources say outputs may be used commercially on free or paid plans. Images carry a visible Gemini sparkle watermark (Nano Banana Pro) plus an invisible SynthID watermark that survived stripping tools in a test. Google's own terms were not retrieved. — [Workalizer](https://workalizer.com/insights/gemini/navigating-geminis-commercial-use-synthid-watermarks-essential-insights-and-gemini-alerts-for-workspace-users); [The Register, Nov 2025](https://www.theregister.com/2025/11/20/google_ai_image_detector/); [DeepMind SynthID](https://deepmind.google/technologies/synthid/)
- **Ideogram free plan**: Ideogram's official FAQ says free-plan images are public. Secondary sources conflict on whether free-tier images may be used commercially. One 2026 guide says the free plan gives about 10 images a day. — [Ideogram FAQ](https://docs.ideogram.ai/using-ideogram/frequently-asked-questions); [Fluxnote Ideogram pricing 2026](https://fluxnote.io/guides/ideogram-pricing-guide-2026); [ConductAtlas ToS summary](https://conductatlas.com/platform/ideogram/ideogram-terms-of-service/tiered-ip-ownership-by-subscription-level/)
- **CapCut free (2026)**: exports up to 1080p with no watermark on standard edits. Some AI templates and effects add a watermark. Auto captions are capped at about 10 min per video or project, and other AI tools are credit-limited. Pro pricing is quoted anywhere from $7.99 to $19.99/mo. One source notes CapCut has been banned in India since June 2020. — [Dupple: Is CapCut free 2026](https://dupple.com/learn/is-capcut-free); [vidpros CapCut Pro vs Free](https://vidpros.com/capcut-pro-vs-free/); [Fluxnote CapCut Q&A (Jun 2026)](https://fluxnote.io/guides/capcut-questions-answered); [costbench](https://costbench.com/software/video-editing/capcut/free-plan/)

### Inferences
- (Background knowledge, not verified this session.) The following are free and allow commercial use of what you make with them: DaVinci Resolve free (edit, Fusion node compositing, Fairlight audio, keyframed Ken Burns; capped at UHD 60p in the free version), Blender (GPL, with Grease Pencil 2D animation and camera moves on 3D terrain), Kdenlive (GPL), Natron (open-source compositor, development largely stalled), Cavalry (free tier for procedural motion graphics), Motion Canvas (MIT, TypeScript), QGIS (GPL), MapLibre GL (BSD) and Natural Earth data (public domain). Remotion's licence requires a paid company licence for companies above a small headcount but is free for individuals. HyperFrames: not researched, status unknown.
- Recommended map pipeline: build base maps (Kashmir/J&K terrain, rivers, passes, 1947 line positions) in QGIS from Natural Earth plus SRTM hillshade. Export high-resolution PNG/SVG layers. Animate the arrows, front lines and labels in Resolve Fusion (or Blender Grease Pencil) with "write-on" strokes. Use Google Earth Studio fly-ins to Zoji La or Srinagar for 3D establishing shots if access is approved. Google Earth imagery needs its attribution shown on screen.
- Recommended visual pipeline: write the script with shot list → generate illustrated frames locally (FLUX.1 schnell or SDXL in ComfyUI, with a consistent style LoRA) → apply parallax with DepthFlow to archival photos and AI frames → use Wan 2.2 5B image-to-video for occasional 3-5 s motion hero shots (flags, smoke, snow) → build maps → edit in Resolve and add captions → make a Shorts cut.
- A free Kling or Hailuo tier is only useful for a few hero shots, and its watermark makes it unsuitable for final output without paying. Local Wan 2.2 needs a GPU with 8 GB or more.

### Gaps
- Current official Hailuo (MiniMax) free-tier limits were not researched.
- The official Gemini, Leonardo and Bing Image Creator licence pages were not fetched.
- Remotion, HyperFrames and Cavalry free-tier terms were not verified this session.
- Google Earth Studio's 2026 terms of service for monetized YouTube are not confirmed.

## 3. Sourcing real images: 1947-48 Kashmir war and Indian Army archival photos, and copyright rules

### Takeaway
Wikimedia Commons has a small category for the 1947 war, with about 15 files. Indian photographs are public domain in India 60 years after publication, so 1947-48 photos are generally PD in India. Commons also requires US PD status, so check each file's tag. In May 2025 the government declared PIB, Doordarshan and AIR content free for creators to use on YouTube if it is not misrepresented. IWM material is under a non-commercial licence, so a monetized video likely needs a paid licence.

### Cited Findings
- The Commons category "Indo-Pakistani War of 1947" lists about 15 files. Some are tagged PD as coming from the Pakistan Army war image gallery, and some are CC0 with an unknown author. — [Commons category](https://commons.wikimedia.org/wiki/Category:Indo-Pakistani_War_of_1947)
- Under India's Copyright Act 1957, photographs are protected for 60 years from the start of the year after publication. Commons requires works from India to be PD (or freely licensed) in both India and the US. — [Commons: Copyright rules by territory/India (mirror)](https://download.osmand.net/wiki/Commons:Copyright_rules_by_territory/India/ru)
- GODL-India: Commons accepts many central-government photos under the Government Open Data License. Over 15,000 files are awaiting review, and editors dispute whether individual department photos were ever explicitly released under GODL. They also argue that government works carry 60-year copyright under s.17(d). — [Commons deletion request on GODL](https://download.osmand.net/wiki/Commons:Deletion_requests/Media_in_Category:Unreviewed_photos_of_GODL-India); [Template:GODL-India](https://www.wikipedia.org/wiki/Template:GODL-India-text)
- May 2025: amid the ANI copyright dispute, the government opened Doordarshan, AIR and PIB content to creators. Reports say the PIB release allows use on YouTube, podcasts and blogs provided it is not misrepresented or used unlawfully. — [India Observers](https://indiaobservers.com/doordarshan-air-pib-ani-copyright-issue); [Channel IAM, 31 May 2025](https://en.channeliam.com/2025/05/31/indian-public-broadcasters-offer-free-media-content); [The Bridge Chronicle](https://www.thebridgechronicle.com/amp/story/news/indian-government-media-agencies-free-access-archives)
- IWM: embedding or using items is under the "IWM Non-Commercial Licence", for example non-commercial educational use. Commercial use or high-resolution copies require contacting IWM's Image and Film Licensing Team, at a cost. — [IWM collection item page](https://www.iwm.org.uk/collections/item/object/1060042869)

### Inferences
- (Inference.) 1947-48 photos published then fell into PD in India around 2008-09. Under US URAA restoration, Indian works not PD in India on 1 Jan 1996 may still be under US copyright until about 2042-43. So Commons tags vary, and a creator targeting Indian audiences is mainly exposed to Indian law. Content ID claims come mostly from agencies such as Getty, Alamy and AP, not from PD archives.
- Practical sourcing order:
  1. Commons, keeping only files with explicit PD-India, GODL or CC tags, and recording the source URL and licence.
  2. PIB photo archive and ADGPI (Indian Army) official posts, which are covered by the 2025 PIB free-use statement. ADGPI social posts are not explicitly covered, so credit them and avoid misrepresenting them.
  3. IWM only with a paid licence for monetized use.
  4. Never use Getty or Alamy watermarked images.
- Always put credits in the description and an on-screen source tag for archival photos.

### Gaps
- No explicit ADGPI or Indian Army reuse policy was found.
- The PIB release text was not read directly; only news reports were seen.
- The National Archives of India (Abhilekh Patal) reuse terms were not researched.
- No authoritative legal source on whether YouTube ad revenue counts as "commercial" under the IWM licence was found.

## 4. Style consistency for AI images, and depicting war within YouTube's violence and advertiser-friendly policies

### Takeaway
For consistency, use local models with a fixed style LoRA, fixed seed and prompt template, and reference-image conditioning (IP-Adapter or FLUX Kontext-type editing) to keep heroes recognisable. Base each hero's look on his real portrait. On policy: YouTube allows violent content in educational or documentary (EDSA) context only when that context is in the video itself. Ads are restricted when blood or injury is the focal point. Show courage, maps, aftermath and symbols rather than gore, and keep thumbnails non-graphic.

### Cited Findings
- EDSA exception: YouTube may allow violent or graphic material in educational, documentary, scientific or artistic videos. The context must be in the images or audio, not only in the title or description. Graphic war footage may be age-restricted. — [YouTube Violent or graphic content policies](https://support.google.com/youtube/answer/2802008?hl=en); [How YouTube evaluates EDSA content](https://support.google.com/youtube/answer/6345162?hl=en); [YouTube blog on EDSA](https://blog.youtube/inside-youtube/look-how-we-treat-educational-documentary-scientific-and-artistic-content-youtube/)
- Advertiser-friendly guidelines: content where "blood, violence, or injury" is the focal point without other context is not suitable for ads. Educational or historical content with non-graphic depictions of dead bodies, and blurred or obscured violence, is treated more leniently. These categories still carry a higher risk of limited ads (the yellow icon). Automated decisions can be appealed for human review. — [YouTube Advertiser-friendly content guidelines](https://support.google.com/youtube/answer/6162278?hl=en); [Subscribr ad-friendly checklist](https://subscribr.ai/youtube-strategy/youtube-ad-friendly-content-checklist)
- Enforcement can misfire on legitimate documentaries, for example Anand Patwardhan's film being removed. — [The Wire](https://thewire.in/film/anand-patwardhans-award-winning-film-father-son-and-holy-war-removed-from-youtube)
- Wan 2.2 supports LoRA fine-tunes for style and character consistency in video. — [MindStudio](https://www.mindstudio.ai/blog/what-is-wan-2-2-video-open-source)

### Inferences
- Visual rules for PVC stories:
  - Show firing, charges, explosions and smoke at a distance or in silhouette.
  - Do not show close-up wounds or blood. Show a soldier's death through symbolism: a fallen helmet, a flag, a fade to his portrait, the citation text.
  - Keep enemies non-dehumanising and avoid communal framing, which is a hate-speech risk.
  - The narration should carry educational context, for example dates, units and the citation.
- Character consistency workflow:
  1. Collect the hero's real photo.
  2. Train a small character LoRA (10-20 images generated with face reference), or use IP-Adapter/InstantID-style face conditioning in ComfyUI.
  3. Lock one style LoRA or prompt suffix per channel, for example "muted ink-and-watercolour graphic novel, 1940s Indian Army uniforms".
  4. Keep a uniform and kit reference sheet for 1947-48: khaki drill, Brodie or Mk II helmets, Lee-Enfield No.1 Mk III, woollens and greatcoats for Zoji La.
  5. Check for anachronisms such as modern camouflage and INSAS rifles.
- Disclose realistic synthetic content using YouTube's altered/synthetic content label where AI creates realistic-looking scenes (background knowledge, not verified this session). Stylised illustration is less likely to be mistaken for real archival imagery.

### Gaps
- The full text of the YouTube pages could not be fetched (support.google.com blocked), so wording comes from search snippets.
- The current YouTube altered/synthetic disclosure requirements and Instagram's "AI info" labelling rules were not verified this session.

## 5. Captions for Shorts and Reels (Hindi/Hinglish, Devanagari fonts) and free auto-caption tools

### Takeaway
Whisper large-v3 (open source) via free front-ends like Vibe gives Devanagari transcripts at roughly 5-10% WER on clean standard Hindi. Hinglish is weaker: English words get transliterated, unless you use a Hinglish fine-tune such as Tara. CapCut's free tier captions Hindi but caps auto-captions at about 10 min and is reportedly banned in India. Burn captions in with Resolve or another subtitle tool after proofreading.

### Cited Findings
- Whisper-based tools reportedly reach about 8-10% WER on standard Hindi and about 90-92% accuracy, dropping to 75-85% for Bhojpuri and Rajasthani. Vibe's Large model claims about 4-6% WER on clean speech. large-v3-turbo shows about 7-15% WER. These are all vendor or comparison claims. — [VexaScribe comparison (Aug 2026)](https://vexascribe.com/compare/best-transcription-software-for-hindi-audio); [Vibe Hindi page](https://vibe-transcribe.pages.dev/vibe-translate-hindi/); [free.ai Hindi](https://free.ai/transcribe/hindi/?lang=de)
- Vibe is open source, works offline, needs no account and outputs native Devanagari. With mixed Hindi-English audio, Whisper tends to transliterate English words into Devanagari. The Tara Hinglish fine-tune of large-v3 can output English words in Latin script. — [Vibe](https://vibe-transcribe.pages.dev/vibe-translate-hindi/); [Tara Hindi+Hinglish transcriber](https://trelis-tara-hindi-transcriber.hf.space/)
- An evaluation thread on Whisper with Indian-context audio (Hinglish, names) exists on the Whisper GitHub discussions. — [openai/whisper discussion #2761](https://github.blesdmm.dns-dynamic.net/openai/whisper/discussions/2761)
- Indic Subtitler is an open-source project for Indic-language subtitles. — [GitHub kurianbenoy/Indic-Subtitler](https://github.com/kurianbenoy/Indic-Subtitler)
- CapCut free tier: auto-captions limited to about 10 min, Hindi supported, Hindi accuracy about 85-89% per one unverified table. — [Fluxnote CapCut AI free vs paid](https://fluxnote.io/guides/capcut-ai-features-free-vs-paid-2026); [Dupple](https://dupple.com/learn/is-capcut-free)

### Inferences
- Caption design, from background knowledge and not verified this session:
  - Use bold sans Devanagari fonts from Google Fonts under the OFL: Mukta, Hind, Baloo 2, Poppins (Latin + Devanagari), Noto Sans Devanagari, Tiro Devanagari Hindi for a "historical" serif look, and Rozha One for titles.
  - Show 1-4 words per caption with active-word highlight in saffron or yellow, a thick black stroke or shadow, and placement in the lower-middle third, clear of the Shorts/Reels UI.
  - Hindi matras get clipped by tight line-height, so use about 1.3-1.5x leading.
  - Hinglish audiences often read Roman Hindi. Consider Devanagari for emotional lines and Roman text for names, units and dates, or test both.
  - Since the narration is scripted, align the script text to the audio (Whisper with forced alignment, for example WhisperX) instead of trusting raw ASR. This gives near-perfect captions.
- DaVinci Resolve free can import SRT and style subtitles. Animated word-highlight captions are easier in CapCut (not available in India), Kdenlive or Remotion. An alternative is to generate ASS subtitles from WhisperX word timestamps and burn them in with ffmpeg (inference).

### Gaps
- No independent benchmark of Whisper large-v3 on Hinglish narration was found.
- Instagram's native Hindi auto-caption support was not checked.
- Data on Devanagari versus Roman caption retention was not found.

## 6. Thumbnail design for this genre and free tools

### Takeaway
Little genre-specific evidence was retrieved. Base the thumbnail on the hero's real face (portrait or restored and colourised photo) with a strong emotion or determination, one bold 2-4 word Hindi or English text hook, the PVC medal or tricolour motif, and a terrain or snow backdrop, with no gore. Free tools are Canva free, Photopea and GIMP.

### Cited Findings
- Advertiser-friendly guidelines apply to thumbnails as well as video. Graphic violence as the focal point is a reason for limited ads. — [YouTube Advertiser-friendly guidelines](https://support.google.com/youtube/answer/6162278?hl=en)

### Inferences
- (Background knowledge, not verified this session.)
  - Canva free allows commercial use of free elements with some restrictions. Photopea is a free browser Photoshop clone with ads. GIMP is GPL. Use OFL Devanagari fonts in each.
  - AI upscaling and colourisation of archival portraits help faces read at small sizes, but label the result as "colourised" in the video to stay honest.
  - Hindi versus English thumbnail text: no data was found. A/B test with YouTube's built-in "Test & Compare" thumbnail feature.

### Gaps
- No creator data or case study on Hindi versus English thumbnail text CTR for Indian military history was found.
- No breakdown of thumbnails from successful Indian defence-history channels was done. Analysing a channel's top videos with vidIQ or YouTube search could fill this.
