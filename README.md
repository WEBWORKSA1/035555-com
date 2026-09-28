# 035555.com — Number meanings, decoded

Free, interactive hub for Chinese number meanings: decoder, luck checker, lucky number generator, slang dictionary, China area codes, numeric domain scorer, guides, videos, contests — with lead generation, sponsorship, donations and AdSense built in.

**Stack:** static HTML + CSS + vanilla JS. Hosted free on GitHub Pages from the `gh-pages` branch. No build step needed to serve.

**Live:** https://webworksa1.github.io/035555-com/

## Go-live checklist
All settings live in `assets/js/config.js`:

1. **Forms** — submit any form once on the live site. FormSubmit sends an activation email to the owner inbox; click *Activate*. Then copy the random alias FormSubmit gives you into `formAlias` (removes even the encoded address from the source).
2. **AdSense** — after approval set `adsenseClient` (+ optional slot IDs) and update `ads.txt`.
3. **Analytics** — set `ga4Id`.
4. **Donations** — paste PayPal/Stripe/Buy Me a Coffee/Ko-fi/GitHub Sponsors links into `donate`.
5. **YouTube** — set `youtubeChannel` and add video IDs to `videos`.

## Custom domain (035555.com)
1. Add a file named `CNAME` containing `035555.com` to the root of the `gh-pages` branch.
2. DNS at the registrar: A records for `@` → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153; CNAME `www` → `webworksa1.github.io`.
3. Settings → Pages → Custom domain `035555.com` → Enforce HTTPS.

## Structure
- `index.html` + tool pages (`decoder`, `lucky-number-checker`, `generator`, `dictionary`, `area-codes`, `numeric-domains`), `guides/`, `videos`, `leads` (lead generation), `support` (donations), `contests`, `careers`, `advertise`, `contact`, `about`, `faq`, `privacy`, `terms`, `disclosure`, `404`.
- `assets/css/style.css` — design system (light/dark).
- `assets/js/config.js` — all IDs and links. `data.js` — digits, slang, area codes. `layout.js` — shared footer, sticky CTA, cookie notice, lead popup. `app.js` — tools, forms, ads, videos.
- `_src/` — optional Python page generator (`python3 _src/build.py` rewrites the HTML from templates).

## Docs
- `docs/RESEARCH.md` — meaning of 035555, concept, revenue model, 25-site benchmark, sources.
- `docs/BUILD-PROMPT.md` — phase-wise build prompt.

## Legal
“035555” is used descriptively; no trademark rights in the number are claimed. See `disclosure.html`.
