# 035555.com — Number meanings, decoded

Free, interactive hub for Chinese number meanings: decoder, luck checker, lucky number generator, slang dictionary, China area codes, numeric domain scorer, guides, videos, contests — with lead generation, sponsorship, donations and AdSense built in.

**Stack:** static HTML + CSS + vanilla JS. Hosted free on GitHub Pages. No build step needed to serve.

## How publishing works
Page sources live in `_src/` (Python 3, no dependencies). On every push to `main`, the GitHub Actions workflow `.github/workflows/build.yml` runs `python3 _src/build.py`, commits the generated HTML to the repo root, and mirrors it to the `gh-pages` branch that GitHub Pages serves.

To build locally: `python3 _src/build.py` (writes HTML into the repo root).

## Go-live checklist
All settings live in `assets/js/config.js`:

1. **Forms** — submit any form once on the live site. FormSubmit sends an activation email to the owner inbox; click *Activate*. Then copy the random alias FormSubmit gives you into `formAlias` (removes even the encoded address from the source).
2. **AdSense** — after approval set `adsenseClient` (+ optional slot IDs) and update `ads.txt`.
3. **Analytics** — set `ga4Id`.
4. **Donations** — paste PayPal/Stripe/Buy Me a Coffee/Ko-fi/GitHub Sponsors links into `donate`.
5. **YouTube** — set `youtubeChannel` and add video IDs to `videos`.

## Custom domain
1. Add a file named `CNAME` containing `035555.com` to the repo root.
2. DNS at the registrar: A records for `@` → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153; CNAME `www` → `webworksa1.github.io`.
3. Settings → Pages → Custom domain `035555.com` → Enforce HTTPS.

## Editing pages
Edit copy in `_src/pages_*.py`, shared header/footer in `_src/layout.py`, styles in `assets/css/style.css`, tool logic in `assets/js/app.js`, data in `assets/js/data.js`.

## Docs
- `docs/RESEARCH.md` — meaning of 035555, concept, revenue model, 25-site benchmark, sources.
- `docs/BUILD-PROMPT.md` — phase-wise build prompt.

## Legal
“035555” is used descriptively; no trademark rights in the number are claimed. See `disclosure.html`.
