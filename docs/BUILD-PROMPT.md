# 035555.com — Phase-wise Build Prompt

Paste each phase into an AI coding assistant in order. Each phase is self-contained and ends with acceptance checks. This repo already implements Phases 1–7; Phases 8–10 are growth steps.

---

## Global rules (include with every phase)

```
You are building 035555.com — "Number meanings, decoded": a free, interactive hub for Chinese number
meanings (decoder, luck checker, lucky number generator, slang dictionary, China area codes, numeric
domain scorer, guides, videos, contests) monetized by Google AdSense, YouTube, lead generation,
sponsorships and donations.

Hard constraints:
- Static HTML/CSS/vanilla JS only. Must run on GitHub Pages free plan (no server, no build step required
  at runtime). All internal links RELATIVE so the site works at /035555-com/ and at a custom domain root.
- Mobile-first, responsive (no horizontal scroll at 360px), WCAG AA contrast, keyboard accessible,
  light + dark themes, prefers-reduced-motion respected.
- EVERY page top: a full-width bar reading "Contact, if you are interested in this website / domain name /
  Sponsorship / Advertisement / Partnership" linking to https://web.works/contact (new tab).
- ONE contact inbox for all forms (the owner's private Gmail, supplied separately). It must NEVER
  appear on the page or in plain text in source. Deliver forms via FormSubmit AJAX with the address
  assembled at runtime from an encoded config value (and later replaced by FormSubmit's random alias).
- No trademark claim in "035555". Include a Trademark & Copyright Disclosure page and footer notice.
  No fake testimonials, fake winners or fabricated statistics.
- All monetization IDs (AdSense client + slots, GA4, donation links, YouTube IDs) live in ONE file:
  assets/js/config.js. Site must look finished with those empty (placeholders become "Advertise here").
```

## Phase 1 — Foundation & design system
```
Create: assets/css/style.css with CSS tokens on :root (bg, surface, ink, muted, line, brand red #c8102e,
gold #c99a2e), dark-mode overrides under prefers-color-scheme and [data-theme="dark"], Inter + Noto Serif SC
fonts, components: buttons, cards, tags (love/luck/emotion/slang/work/caution), grid helpers, forms, tables,
FAQ <details>, ad slots, lead band, gauge (conic-gradient), sticky mobile CTA, modal, cookie notice, footer.
Create a Python build (_src/build.py + layout.py) that renders every page from one layout: skip link,
inquiry bar, sticky header (logo "03" mark, nav, "Get a lucky number" CTA, theme toggle, hamburger),
shared footer/lead-modal/cookie notice (emitted once as assets/js/layout.js), newsletter.
SEO per page: title, meta description, canonical, Open Graph/Twitter, JSON-LD (WebSite+SearchAction,
FAQPage, Article). Generate sitemap.xml, robots.txt, ads.txt placeholder, manifest, favicon, og image, .nojekyll.
Accept: all pages share header/footer; Lighthouse a11y >= 95; no layout overflow at 360/768/1366px.
```

## Phase 2 — Data layer
```
assets/js/data.js: DIGITS 0–9 (hanzi, pinyin, homophones, chat-code use, vibe −3..+3, cultural note);
SLANG >= 75 entries [code, hanzi, pinyin, English, category] incl. 520, 521, 1314, 5201314, 530, 035,
666, 88, 886, 233, 555, 5555, 7456, 687, 918, 995, 996, 007, 1024, 250, 748, 38 (flag insults as
"caution"); AREA_CODES for major China cities + every Shanxi 035x code (0355 = Changzhi).
Accept: every meaning cross-checked against >= 2 sources.
```

## Phase 3 — Interactive tools (assets/js/app.js)
```
1. Luck engine: score 1–99 = 50 + avg digit vibe×10 + lucky combos (8888, 888, 168, 1688, 518, 1314…)
   − avoided combos (4444, 44, 14, 74, 250, 514, 748) + repeat runs + ending bonus (8/6/9) − ending 4.
   Return hits so the UI explains the score.
2. Decoder (decoder.html + compact version in homepage hero): gauge, verdict, hidden chat codes, area code
   match, digit-by-digit rows, shareable ?n= URL, Share button, CTA to leads with ?need=&ref= prefilled.
3. Luck Checker: type (phone/plate/house/date/domain/business) + number → score, type-specific tip,
   "Get my free shortlist" lead CTA.
4. Generator: goal (wealth/love/career/health/balance), length, optional birthday seed (repeatable PRNG);
   never output 4; show top 9 by score.
5. Dictionary: live search across all fields, category chips/select, count, ?q= deep link, "Decode" links.
6. Area-code finder: filterable table with +86 format.
7. Numeric domain scorer: length, TLD, 0/4 rules, leading 0, repeats, ABAB/ABCABC, sequential, ends-in-8 →
   tier (Entry…Ultra-premium) with factor table and "Get a free expert appraisal" lead CTA. ?d= deep link.
Accept: zero console errors; each tool works with keyboard only.
```

## Phase 4 — Lead generation (highest priority revenue)
```
leads.html "Lucky Number Concierge": 3-step form with progress bar — (1) need: phone / plate / numeric
domain buy-sell / business consult / auspicious date / other + reference number; (2) budget bands incl.
"I'm selling", timeline, country; (3) name, email, phone/WeChat/WhatsApp, details, consent checkbox.
Per-step validation, URL prefill, honeypot, success/error messages, GA4 generate_lead event.
Also: compact version on homepage in a dark "lead band", exit-intent + 45s modal (once per session),
sticky mobile CTA, lead CTAs inside every tool result, FAQ below form.
Accept: submission reaches the inbox via FormSubmit; inbox not visible anywhere.
```

## Phase 5 — Monetization surfaces
```
AdSense: [data-ad="top|inContent|sidebar|footer"] slots; when adsenseClient is set, inject the script and
<ins class="adsbygoogle"> responsive units; otherwise render "Your brand here — Advertise with us".
YouTube: videos.html + homepage strip rendered from config (click-to-load youtube-nocookie facade; if no ID,
a branded card linking to a YouTube search). Channel subscribe CTA.
advertise.html: 3 sponsor tiers, ideal-partner chips, media-kit request form (company, budget, interest incl.
"Buy website / domain" and "Partnership").
support.html: fund-use cards (operations, promotion & marketing, hiring talent, contests & prizes), tiers
$8 / $68 / $888, instant links from config (PayPal/Stripe/BMC/Ko-fi/GitHub Sponsors) and a pledge form
(amount, frequency, designation, public credit). Note "not a registered charity".
```

## Phase 6 — Community & talent
```
contests.html: current challenge, prize table, rules summary (no purchase necessary, 18+, void where
prohibited, judging criteria, licence), entry form, "Winners announced here" block (no fake winners).
careers.html: 6 role cards (writer, video creator, SEO, ad sales, moderator, front-end dev) with Apply
buttons that preselect the role in an application form (portfolio URL, languages, availability).
contact.html: topic-routed form + owner inquiry card linking to web.works/contact.
```

## Phase 7 — Content, legal, QA, deploy
```
Guides: meaning-of-035555, chinese-digit-meanings, chinese-number-slang, numeric-domains-guide, guides
index; FAQ page; about; privacy (AdSense/cookie wording, opt-out links), terms (contest, donation,
concierge clauses), disclosure (no trademark claim in 035555, non-affiliation incl. 0355 Changzhi and
035 Bergamo numbers, third-party marks, takedown procedure), 404 (works at nested paths via <base>).
QA with Playwright: every page 200, no broken internal links, no console errors, no horizontal overflow at
390px, inbox string absent from rendered HTML, lead form advances through all steps.
Deploy: push to github.com/webworksa1/035555-com, publish with GitHub Pages from the gh-pages branch.
Custom domain: add CNAME file "035555.com", DNS A records 185.199.108.153/109/110/111 + CNAME www →
webworksa1.github.io, then enable "Enforce HTTPS".
```

## Phase 8 — Growth (next 90 days)
```
Programmatic SEO: generate one static page per slang code (/code/520.html …) and per area code, each with
unique copy, FAQ schema and tool embed. Add Simplified-Chinese (/zh/) versions with hreflang.
Publish 2 guides/week; repurpose each as a YouTube Short linking back.
```

## Phase 9 — Conversion optimisation
```
A/B test hero CTA copy and lead-form first step; add a "number of the day" widget; add downloadable
"Lucky Numbers Cheat Sheet" PDF as an email lead magnet; add WhatsApp/WeChat click-to-chat after lead
submission.
```

## Phase 10 — Scale revenue
```
Apply for AdSense once 25+ substantial pages exist; add affiliate links (domain registrars, language apps,
eSIM); launch paid "Personal Number Report" (Stripe Payment Link); partner with numeric-domain brokers for
revenue share on concierge leads.
```
