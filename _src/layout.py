"""Shared layout pieces for the 035555.com static build."""
import json

DOMAIN = "https://035555.com"
INQ = "https://web.works/contact"

NAV = [
    ("decoder.html", "Decoder"), ("lucky-number-checker.html", "Luck Checker"),
    ("dictionary.html", "Dictionary"), ("generator.html", "Generator"), ("numeric-domains.html", "Domains"),
    ("guides/index.html", "Guides"), ("videos.html", "Videos"),
]


def ad(slot, R):
    return (f'<div class="ad-slot" data-ad="{slot}"><div class="ad-label">Advertisement</div>'
            f'<div class="ad-box"><span>Your brand here — reach readers decoding numbers every day. '
            f'<a href="{R}advertise.html">Advertise with us</a></span></div></div>')


def honey():
    return '<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">'


def newsletter(R, source="Newsletter"):
    return f'''<form class="newsletter" data-form data-subject="Newsletter signup ({source})" data-ok="You're in! Watch your inbox for the weekly Number Code.">
  {honey()}<label class="sr" for="nl-{source}">Email</label>
  <input id="nl-{source}" type="email" name="Email" placeholder="you@email.com" required autocomplete="email">
  <input type="hidden" name="Source" value="{source}">
  <button class="btn btn-primary" type="submit">Get the weekly code</button>
  <p class="form-msg small" aria-live="polite" style="flex-basis:100%;margin:0"></p>
</form>'''


def lead_form(R, compact=False, fid="lf"):
    needs = [("number", "Lucky phone number"), ("plate", "Lucky licence plate"), ("domain", "Buy / sell a numeric domain"),
             ("business", "Business name & number consult"), ("date", "Auspicious date selection"), ("other", "Something else")]
    opts = "".join(f'<label class="opt"><input type="radio" name="Need" value="{v}" {"required" if i == 0 else ""}><span>{t}</span></label>'
                   for i, (v, t) in enumerate(needs))
    return f'''<form class="card" data-form data-steps data-subject="LEAD — Lucky number / domain request" data-ok="Request received! Expect your personalised shortlist within 24–48 hours." id="{fid}">
  {honey()}
  <div class="steps" aria-hidden="true"><span></span><span></span><span></span></div>
  <div class="step">
    <h3>What are you looking for?</h3>
    <div class="opt-grid" role="radiogroup" aria-label="Need">{opts}</div>
    <div class="field" style="margin-top:14px"><label for="{fid}-ref">Number, domain or idea you have in mind (optional)</label>
      <input id="{fid}-ref" name="Reference number" placeholder="e.g. 8888 ending, 1688.com, a date"></div>
    <button class="btn btn-primary btn-block" type="button" data-next>Continue →</button>
  </div>
  <div class="step">
    <h3>Budget & timing</h3>
    <div class="row2">
      <div class="field"><label for="{fid}-b">Budget (USD)</label><select id="{fid}-b" name="Budget" required>
        <option value="">Select…</option><option>Under $100</option><option>$100 – $500</option><option>$500 – $2,500</option><option>$2,500 – $10,000</option><option>$10,000 – $50,000</option><option>$50,000+</option><option>I'm selling</option></select></div>
      <div class="field"><label for="{fid}-t">Timeline</label><select id="{fid}-t" name="Timeline" required>
        <option value="">Select…</option><option>This week</option><option>This month</option><option>1–3 months</option><option>Just researching</option></select></div>
    </div>
    <div class="field"><label for="{fid}-c">Country / region</label><input id="{fid}-c" name="Country" placeholder="e.g. Canada, Hong Kong, Singapore" required></div>
    <div class="row2"><button class="btn btn-ghost" type="button" data-prev>← Back</button><button class="btn btn-primary" type="button" data-next>Continue →</button></div>
  </div>
  <div class="step">
    <h3>Where should we send your shortlist?</h3>
    <div class="row2">
      <div class="field"><label for="{fid}-n">Name</label><input id="{fid}-n" name="Name" required autocomplete="name"></div>
      <div class="field"><label for="{fid}-e">Email</label><input id="{fid}-e" type="email" name="Email" required autocomplete="email"></div>
    </div>
    <div class="field"><label for="{fid}-p">Phone / WhatsApp / WeChat (optional)</label><input id="{fid}-p" name="Phone or messenger" autocomplete="tel"></div>
    {"" if compact else f'<div class="field"><label for="{fid}-m">Anything else?</label><textarea id="{fid}-m" name="Details" rows="3" placeholder="Preferred digits, digits to avoid, purpose…"></textarea></div>'}
    <label class="small" style="font-weight:500"><input type="checkbox" name="Consent" value="Yes" required style="width:auto;margin-right:6px">I agree to be contacted about my request. See the <a href="{R}privacy.html">Privacy Policy</a>.</label>
    <div class="row2" style="margin-top:12px"><button class="btn btn-ghost" type="button" data-prev>← Back</button><button class="btn btn-primary" type="submit">Send my request</button></div>
  </div>
  <p class="form-msg" aria-live="polite"></p>
  <p class="small muted" style="margin:10px 0 0">Free, no obligation. We reply within 1 business day.</p>
</form>'''


def header(R, current):
    cur = ' aria-current="page"'
    items = "".join(
        f'<li><a href="{R}{href}"{cur if href == current else ""}>{label}</a></li>' for href, label in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="inquiry-bar" role="note"><a href="{INQ}" target="_blank" rel="noopener">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership →</a></div>
<header class="site-header"><div class="wrap nav">
  <a class="logo" href="{R}index.html" aria-label="035555.com home"><span class="logo-mark">03</span><span>035555.com<small>Number meanings, decoded</small></span></a>
  <ul class="menu" id="menu">{items}</ul>
  <div class="nav-actions">
    <a class="btn btn-primary btn-sm" href="{R}leads.html">Get a lucky number</a>
    <button class="icon-btn" type="button" data-theme-toggle aria-label="Toggle dark mode">◐</button>
    <button class="icon-btn menu-toggle" type="button" aria-controls="menu" aria-expanded="false" aria-label="Menu">☰</button>
  </div>
</div></header>'''


def footer(R):
    return f'''<footer class="site-footer"><div class="wrap">
  <div class="foot-grid">
    <div>
      <a class="logo" href="{R}index.html"><span class="logo-mark">03</span><span>035555.com<small>Number meanings, decoded</small></span></a>
      <p class="muted small" style="margin-top:12px">Free tools and guides to the meanings of numbers in Chinese language and culture — lucky digits, chat codes, phone & plate luck, and numeric domains.</p>
      {newsletter(R, "Footer")}
    </div>
    <div><h4>Tools</h4><ul>
      <li><a href="{R}decoder.html">Number Decoder</a></li><li><a href="{R}lucky-number-checker.html">Luck Checker</a></li>
      <li><a href="{R}generator.html">Lucky Number Generator</a></li><li><a href="{R}dictionary.html">Number Slang Dictionary</a></li>
      <li><a href="{R}area-codes.html">China Area Codes</a></li><li><a href="{R}numeric-domains.html">Numeric Domain Scorer</a></li></ul></div>
    <div><h4>Learn</h4><ul>
      <li><a href="{R}guides/meaning-of-035555.html">What 035555 means</a></li><li><a href="{R}guides/chinese-digit-meanings.html">Digit meanings 0–9</a></li>
      <li><a href="{R}guides/chinese-number-slang.html">Number slang guide</a></li><li><a href="{R}guides/numeric-domains-guide.html">Numeric domains guide</a></li>
      <li><a href="{R}videos.html">Videos</a></li><li><a href="{R}faq.html">FAQ</a></li></ul></div>
    <div><h4>Get involved</h4><ul>
      <li><a href="{R}leads.html">Lucky Number Concierge</a></li><li><a href="{R}support.html">Support us / Donate</a></li>
      <li><a href="{R}contests.html">Contests & prizes</a></li><li><a href="{R}careers.html">Careers & creators</a></li>
      <li><a href="{R}advertise.html">Advertise & sponsor</a></li><li><a href="{R}contact.html">Contact</a></li></ul></div>
    <div><h4>Company</h4><ul>
      <li><a href="{R}about.html">About</a></li><li><a href="{R}privacy.html">Privacy Policy</a></li>
      <li><a href="{R}terms.html">Terms of Use</a></li><li><a href="{R}disclosure.html">Trademark & Copyright</a></li>
      <li><a href="{R}sitemap.xml">Sitemap</a></li><li><a href="{INQ}" target="_blank" rel="noopener">Buy / partner on this domain</a></li></ul></div>
  </div>
  <div class="legal">
    <p>© <span class="year">2026</span> 035555.com. Original content and tools © their authors. “035555” is used here as a descriptive numeric string and domain name; no trademark rights in the number are claimed, and this site is not affiliated with any company, phone subscriber or organisation that uses the same digits. Cultural meanings are folk and internet-slang associations provided for education and entertainment only. <a href="{R}disclosure.html">Full disclosure</a>.</p>
  </div>
</div></footer>
<div class="sticky-cta"><a class="btn btn-primary" href="{R}leads.html">Get a lucky number</a><a class="btn btn-gold" href="{R}decoder.html">Decode</a></div>
<button class="icon-btn back-top" type="button" aria-label="Back to top">↑</button>
<div class="cookie card small" role="dialog" aria-label="Cookie notice"><p>We use cookies for analytics and, where enabled, advertising (Google AdSense). See our <a href="{R}privacy.html">Privacy Policy</a>.</p><button class="btn btn-primary btn-sm" data-cookie-ok>OK</button></div>'''


def modal(R):
    return f'''<div class="modal" id="lead-modal" role="dialog" aria-modal="true" aria-labelledby="lm-title"><div class="card">
  <button class="icon-btn close" type="button" aria-label="Close">✕</button>
  <span class="eyebrow">Free shortlist</span><h3 id="lm-title">Want a number that scores 90+?</h3>
  <p class="small muted">Tell us what you need — phone, plate, domain or date — and we'll send options that fit your budget.</p>
  <form data-form data-subject="LEAD — Exit-intent popup" data-ok="Got it! We'll be in touch within 24 hours.">
    {honey()}
    <div class="field"><label for="lm-need">I'm looking for</label><select id="lm-need" name="Need" required><option value="">Select…</option><option>Lucky phone number</option><option>Lucky licence plate</option><option>Numeric domain</option><option>Selling a numeric domain</option><option>Advertising / sponsorship</option></select></div>
    <div class="field"><label for="lm-email">Email</label><input id="lm-email" type="email" name="Email" required autocomplete="email"></div>
    <button class="btn btn-primary btn-block" type="submit">Send me options</button>
    <p class="form-msg small" aria-live="polite"></p>
  </form>
</div></div>'''


def page(R, current, title, desc, body, path, jsonld=None, lead_modal=True, og_type="website"):
    url = DOMAIN + "/" + (path if path != "index.html" else "")
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": "035555.com", "url": DOMAIN + "/",
           "potentialAction": {"@type": "SearchAction", "target": DOMAIN + "/dictionary.html?q={q}", "query-input": "required name=q"}}]
    if jsonld:
        ld += jsonld if isinstance(jsonld, list) else [jsonld]
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#c8102e">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="035555.com">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{DOMAIN}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{R}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{R}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}assets/css/style.css">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{ld_html}
</head>
<body data-root="{R}">
{header(R, current)}
<main id="main">
{body}
</main>
<script src="{R}assets/js/config.js"></script>
<script src="{R}assets/js/data.js"></script>
<script src="{R}assets/js/layout.js"></script>
<script src="{R}assets/js/app.js"></script>
</body>
</html>
'''
