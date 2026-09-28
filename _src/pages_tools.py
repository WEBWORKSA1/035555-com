from layout import ad, lead_form, newsletter

PAGES = {}

# ---------------- HOME ----------------
def home(R):
    return f'''
<section class="hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow">Free number meaning tools · 数字含义</span>
    <h1>Every number says something. <span style="color:var(--brand)">Decode it.</span></h1>
    <p class="lead">Instantly read any phone number, licence plate, date, address or domain the way Chinese speakers hear it — lucky sounds, hidden chat codes like <b>520</b> (I love you) and <b>5555</b> (crying), and a 0–100 luck score.</p>
    <div class="digits" aria-label="0 3 5 5 5 5"><span class="digit">0</span><span class="digit">3</span><span class="digit hl">5</span><span class="digit hl">5</span><span class="digit hl">5</span><span class="digit hl">5</span></div>
    <div class="hero-cta"><a class="btn btn-primary" href="decoder.html">Decode a number</a><a class="btn btn-ghost" href="leads.html">Find me a lucky number</a></div>
    <div class="stats"><div><b>10</b><span>digits, 3 sound layers each</span></div><div><b>75+</b><span>number chat codes</span></div><div><b>60</b><span>China area codes</span></div><div><b>$0</b><span>free, no sign-up</span></div></div>
  </div>
  <div class="tool" aria-label="Quick decoder">
    <h2 style="font-size:1.35rem">Quick decode</h2>
    <form id="decoder-form" data-default="035555" data-compact><div class="tool-input"><label class="sr" for="qd">Number</label><input id="qd" inputmode="numeric" maxlength="24" placeholder="Try 035555, 520, 1688…"><button class="btn btn-primary" type="submit">Decode</button></div></form>
    <div class="chips" style="margin-top:10px"><button class="chip" data-try="520">520</button><button class="chip" data-try="5201314">5201314</button><button class="chip" data-try="168">168</button><button class="chip" data-try="666">666</button><button class="chip" data-try="748">748</button><button class="chip" data-try="88888888">88888888</button></div>
    <div id="decoder-out" class="result" aria-live="polite"></div>
  </div>
</div></section>
{ad("top", R)}
<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Tools</span><h2>Everything numbers, in one place</h2></div><p>Built for curious readers, couples, parents naming dates, car and phone buyers, domain investors and businesses entering Chinese-speaking markets.</p></div>
  <div class="grid g3">
    <a class="card" href="decoder.html"><div class="ico">解</div><h3>Number Decoder</h3><p class="muted">Digit-by-digit sounds, hidden chat codes and a luck score for any number.</p></a>
    <a class="card" href="lucky-number-checker.html"><div class="ico">吉</div><h3>Luck Checker</h3><p class="muted">Score a phone number, plate, house number, date or domain — with tips for each.</p></a>
    <a class="card" href="generator.html"><div class="ico">生</div><h3>Lucky Number Generator</h3><p class="muted">Get 4-free numbers tuned for wealth, love, career or health.</p></a>
    <a class="card" href="dictionary.html"><div class="ico">典</div><h3>Number Slang Dictionary</h3><p class="muted">520, 1314, 666, 233, 996, 748… searchable with Chinese, pinyin and English.</p></a>
    <a class="card" href="area-codes.html"><div class="ico">区</div><h3>China Area Codes</h3><p class="muted">Find which city a 0xx or 0xxx prefix belongs to — including every Shanxi 035x code.</p></a>
    <a class="card" href="numeric-domains.html"><div class="ico">域</div><h3>Numeric Domain Scorer</h3><p class="muted">See why some number domains trade at premiums, then get a free appraisal.</p></a>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap"><div class="lead-band">
  <div>
    <span class="eyebrow" style="color:var(--gold)">Lucky Number Concierge</span>
    <h2>Stop guessing. Get a shortlist of truly lucky numbers.</h2>
    <p>Tell us what you need and your budget. We send curated, available options — phone numbers, licence plates, numeric domains or auspicious dates — scored and explained.</p>
    <ul class="checks"><li>Free shortlist in 24–48 hours</li><li>Every option luck-scored and explained in plain English</li><li>Buyers and sellers of numeric domains welcome</li><li>No obligation, no spam</li></ul>
  </div>
  {lead_form(R, compact=True, fid="home-lf")}
</div></div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Trending codes</span><h2>What people are decoding</h2></div><a class="btn btn-ghost btn-sm" href="dictionary.html">Open the dictionary →</a></div>
  <div class="grid g4">
    <a class="card" href="dictionary.html?q=520"><span class="tag love">love</span><h3>520 <span class="cn">我爱你</span></h3><p class="small muted">“I love you” — May 20 is an unofficial Valentine's Day.</p></a>
    <a class="card" href="dictionary.html?q=5555"><span class="tag emotion">emotion</span><h3>5555 <span class="cn">呜呜呜呜</span></h3><p class="small muted">The sound of sobbing — dramatic or playful.</p></a>
    <a class="card" href="dictionary.html?q=666"><span class="tag slang">slang</span><h3>666 <span class="cn">溜溜溜</span></h3><p class="small muted">“Awesome!” — praise in games and livestreams.</p></a>
    <a class="card" href="dictionary.html?q=168"><span class="tag luck">luck</span><h3>168 <span class="cn">一路发</span></h3><p class="small muted">“Prosper all the way” — a favourite business number.</p></a>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Watch</span><h2>Number meanings on video</h2></div><a class="btn btn-ghost btn-sm" href="videos.html">All videos →</a></div>
  <div class="grid g3" id="video-grid" data-limit="3"></div>
</div></section>
{ad("inContent", R)}
<section><div class="wrap grid g2" style="align-items:start">
  <div>
    <span class="eyebrow">The name</span><h2>Why “035555”?</h2>
    <p>Read aloud in Mandarin, <b class="cn">零三五五五五</b> is <i>líng sān wǔ wǔ wǔ wǔ</i>. In chat-code logic 0 → 你 (you), 3 → 想 (miss) and 5 → 我 (me) or 呜 (sob) — so the string can be read playfully as <b>“you miss me-me-me-me”</b> or as a sigh followed by <b>5555</b>, crying. It also begins with <b>0355</b>, the landline code for Changzhi in Shanxi, and <b>035</b> is Bergamo's area code in Italy.</p>
    <p>One number, many readings — that's exactly what this site is about.</p>
    <a class="btn btn-ghost" href="guides/meaning-of-035555.html">Read the full breakdown →</a>
  </div>
  <div class="card">
    <h3>Get one number code a week</h3>
    <p class="muted small">A 2-minute email: one code, its story, and a luck tip. Join readers learning Chinese culture the fun way.</p>
    {newsletter(R, "Home")}
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap grid g3">
  <a class="card" href="contests.html"><span class="badge">Monthly</span><h3 style="margin-top:10px">Decode-a-Number Contest</h3><p class="muted small">Explain a number's hidden meaning in the most creative way. Sponsored prizes every month.</p></a>
  <a class="card" href="support.html"><span class="badge" style="background:var(--gold);color:#1c1714">Support</span><h3 style="margin-top:10px">Keep the tools free</h3><p class="muted small">Donations fund hosting, new tools, creators and contest prizes.</p></a>
  <a class="card" href="advertise.html"><span class="badge" style="background:var(--ink)">Partners</span><h3 style="margin-top:10px">Advertise & sponsor</h3><p class="muted small">Reach an audience actively shopping for lucky numbers, domains and dates.</p></a>
</div></section>

<section><div class="wrap article">
  <h2 class="center">Frequently asked questions</h2>
  <details><summary>Is the luck score scientific?</summary><p>No. It's a transparent heuristic based on widely shared Chinese sound associations (8 = prosper, 4 = death, 6 = smooth, 9 = lasting). It's for fun, learning and comparing options — not a prediction.</p></details>
  <details><summary>Why is 4 unlucky and 8 lucky?</summary><p>四 (sì, four) sounds like 死 (sǐ, death). 八 (bā, eight) sounds close to 发 (fā, to prosper). These sound-alikes shape prices of phone numbers, plates and apartments across Chinese-speaking markets.</p></details>
  <details><summary>Can you actually get me a lucky phone number or domain?</summary><p>Yes — use the <a href="leads.html">Lucky Number Concierge</a>. We research availability and send you a free shortlist. Pricing depends on the seller and market.</p></details>
  <details><summary>Is 035555.com a company or a trademark?</summary><p>No. It's a descriptive numeric domain. We claim no rights in the number itself and are not affiliated with anyone using the same digits. See <a href="disclosure.html">our disclosure</a>.</p></details>
</div></section>
'''

PAGES["index.html"] = dict(
    title="035555.com — Chinese Number Meanings, Lucky Number Checker & Decoder",
    desc="Decode any number: Chinese digit meanings, number slang like 520 and 5555, lucky phone & plate checker, lucky number generator and numeric domain scorer. Free.",
    body=home, current="index.html",
    jsonld={"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "Why is 4 unlucky and 8 lucky in Chinese?", "acceptedAnswer": {"@type": "Answer", "text": "Four (si) sounds like the word for death; eight (ba) sounds close to fa, to prosper."}},
        {"@type": "Question", "name": "What does 5555 mean in Chinese?", "acceptedAnswer": {"@type": "Answer", "text": "5 is pronounced wu, echoing the sobbing sound 呜呜, so 5555 means crying."}}]})

# ---------------- DECODER ----------------
def decoder(R):
    return f'''
<section class="page-hero"><div class="wrap">
  <div class="breadcrumbs"><a href="index.html">Home</a> › Decoder</div>
  <h1>Number Decoder</h1>
  <p>Enter any number — a phone number, plate, birthday, price or domain. See how each digit sounds in Mandarin, which chat codes hide inside, and how lucky it reads.</p>
</div></section>
<section style="padding-top:8px"><div class="wrap grid" style="grid-template-columns:minmax(0,1fr)">
  <div class="tool">
    <form id="decoder-form" data-default="035555"><div class="tool-input"><label class="sr" for="dn">Number</label><input id="dn" inputmode="numeric" maxlength="24" placeholder="Enter up to 24 digits"><button class="btn btn-primary" type="submit">Decode</button></div></form>
    <div class="chips" style="margin-top:10px"><span class="small muted">Try:</span><button class="chip" data-try="035555">035555</button><button class="chip" data-try="5201314">5201314</button><button class="chip" data-try="1688">1688</button><button class="chip" data-try="7456">7456</button><button class="chip" data-try="13888888888">13888888888</button></div>
    <div id="decoder-out" class="result" aria-live="polite"></div>
  </div>
</div></section>
{ad("inContent", R)}
<section><div class="wrap article">
  <h2>How the decoder reads a number</h2>
  <ol><li><b>Sound layer</b> — each digit's Mandarin pronunciation and the words it echoes (八 bā → 发 fā, prosper).</li>
  <li><b>Chat-code layer</b> — sequences used in texting, like 520 (我爱你) or 886 (bye).</li>
  <li><b>Luck layer</b> — a transparent 1–99 score: average digit “vibe”, plus lucky combos (168, 888), minus avoided ones (14, 74, 250), plus repetition and ending bonuses.</li>
  <li><b>Location layer</b> — if the number starts with a known mainland China area code, we show the city.</li></ol>
  <p class="note">Meanings are cultural associations and internet slang, shared for learning and fun. Different regions (Mandarin vs. Cantonese) sometimes read digits differently.</p>
</div></section>'''

PAGES["decoder.html"] = dict(title="Number Decoder — What Does This Number Mean in Chinese? | 035555.com",
    desc="Free Chinese number decoder: digit-by-digit sounds, hidden number slang, area code detection and a luck score for any phone number, plate or date.",
    body=decoder, current="decoder.html")

# ---------------- LUCK CHECKER ----------------
def checker(R):
    return f'''
<section class="page-hero"><div class="wrap">
  <div class="breadcrumbs"><a href="index.html">Home</a> › Luck Checker</div>
  <h1>Lucky Number Checker</h1>
  <p>Is your phone number, licence plate, address, wedding date or domain lucky? Get a score, the reasons behind it, and tips for choosing better.</p>
</div></section>
<section style="padding-top:8px"><div class="wrap grid g2" style="align-items:start">
  <div class="tool">
    <form id="luck-form">
      <div class="field"><label for="lt">What are you checking?</label><select id="lt"><option value="phone">Phone number</option><option value="plate">Licence plate</option><option value="house">House / unit number</option><option value="date">Date (e.g. 20260808)</option><option value="domain">Numeric domain</option><option value="business">Business / price number</option></select></div>
      <div class="field"><label for="ln">Number</label><input id="ln" inputmode="numeric" placeholder="e.g. 138 8888 1688" required></div>
      <button class="btn btn-primary btn-block" type="submit">Check my luck</button>
    </form>
    <div id="luck-out" class="result" aria-live="polite"></div>
  </div>
  <div>
    <div class="card"><h3>Quick rules of thumb</h3>
      <div class="table-wrap"><table><thead><tr><th>Favoured</th><th>Avoided</th></tr></thead><tbody>
      <tr><td><b>8</b> 发 prosper</td><td><b>4</b> 死 death</td></tr>
      <tr><td><b>6</b> 顺/溜 smooth</td><td><b>14</b> 要死 “will die”</td></tr>
      <tr><td><b>9</b> 久 lasting</td><td><b>74</b> 去死 “go die”</td></tr>
      <tr><td><b>168</b> 一路发</td><td><b>250</b> fool</td></tr>
      <tr><td><b>518</b> 我要发</td><td><b>748</b> go to hell</td></tr></tbody></table></div>
    </div>
    {ad("sidebar", R)}
  </div>
</div></section>'''

PAGES["lucky-number-checker.html"] = dict(title="Lucky Number Checker — Phone, Plate, Date & Address Luck Score | 035555.com",
    desc="Check whether a phone number, licence plate, house number, date or domain is lucky in Chinese culture. Free score with explanations.",
    body=checker, current="lucky-number-checker.html")

# ---------------- GENERATOR ----------------
def generator(R):
    return f'''
<section class="page-hero"><div class="wrap">
  <div class="breadcrumbs"><a href="index.html">Home</a> › Generator</div>
  <h1>Lucky Number Generator</h1>
  <p>Generate 4-free numbers tuned to a goal. Add a birthday to get a repeatable personal set.</p>
</div></section>
<section style="padding-top:8px"><div class="wrap">
  <div class="tool">
    <form id="gen-form" class="grid g4" style="align-items:end">
      <div class="field" style="margin:0"><label for="gp">Goal</label><select id="gp" name="purpose"><option value="wealth">Wealth & business</option><option value="love">Love & relationships</option><option value="career">Career & success</option><option value="health">Health & longevity</option><option value="balance">Balance</option></select></div>
      <div class="field" style="margin:0"><label for="gl">Digits</label><input id="gl" name="len" type="number" min="3" max="11" value="6"></div>
      <div class="field" style="margin:0"><label for="gb">Birthday (optional)</label><input id="gb" name="bd" type="date"></div>
      <button class="btn btn-primary" type="submit">Generate</button>
    </form>
    <div id="gen-out" class="result" aria-live="polite"></div>
  </div>
</div></section>
{ad("inContent", R)}'''

PAGES["generator.html"] = dict(title="Lucky Number Generator — Chinese Lucky Numbers for Wealth, Love & Career | 035555.com",
    desc="Generate lucky numbers without 4, tuned for wealth, love, career or health using Chinese number meanings. Free and instant.",
    body=generator, current="generator.html")

# ---------------- DICTIONARY ----------------
def dictionary(R):
    return f'''
<section class="page-hero"><div class="wrap">
  <div class="breadcrumbs"><a href="index.html">Home</a> › Dictionary</div>
  <h1>Chinese Number Slang Dictionary</h1>
  <p>The number codes Chinese speakers use in texts, livestreams and social media — with characters, pinyin and plain-English meaning.</p>
</div></section>
<section style="padding-top:8px"><div class="wrap">
  <div class="dict-controls"><label class="sr" for="dict-q">Search</label><input id="dict-q" type="search" placeholder="Search a code, word or meaning (e.g. 520, love, bye)">
    <label class="sr" for="dict-cat">Category</label><select id="dict-cat"><option value="">All categories</option><option value="love">Love</option><option value="luck">Luck</option><option value="emotion">Emotion</option><option value="slang">Slang</option><option value="work">Work</option><option value="caution">Caution / insults</option></select></div>
  <div class="chips" style="margin-bottom:14px"><button class="chip" data-cat="" aria-pressed="true">All</button><button class="chip" data-cat="love">Love</button><button class="chip" data-cat="luck">Luck</button><button class="chip" data-cat="emotion">Emotion</button><button class="chip" data-cat="slang">Slang</button><button class="chip" data-cat="work">Work</button><button class="chip" data-cat="caution">Caution</button> <span id="dict-count" class="small muted" style="align-self:center"></span></div>
  <div id="dict-list" class="grid g2"></div>
  <p class="small muted" style="margin-top:16px">Missing a code? <a href="contact.html">Suggest it</a> — accepted entries are credited in our monthly contest.</p>
</div></section>
{ad("footer", R)}'''

PAGES["dictionary.html"] = dict(title="Chinese Number Slang Dictionary — 520, 1314, 666, 5555 & More | 035555.com",
    desc="Searchable dictionary of Chinese number slang: 520 I love you, 1314 forever, 666 awesome, 5555 crying, 88 bye, 996 and more with characters and pinyin.",
    body=dictionary, current="dictionary.html")

# ---------------- AREA CODES ----------------
def areas(R):
    return f'''
<section class="page-hero"><div class="wrap">
  <div class="breadcrumbs"><a href="index.html">Home</a> › China Area Codes</div>
  <h1>China Area Code Finder</h1>
  <p>Mainland China landline numbers start with a 3- or 4-digit area code beginning with 0. Search by code, city or province. The country code is +86 (drop the leading 0 when dialling from abroad).</p>
</div></section>
<section style="padding-top:8px"><div class="wrap">
  <div class="dict-controls"><label class="sr" for="area-q">Search</label><input id="area-q" type="search" placeholder="Search e.g. 0355, Shanxi, Shenzhen"></div>
  <div class="table-wrap"><table><thead><tr><th>Area code</th><th>City</th><th>Province</th><th>From abroad</th></tr></thead><tbody id="area-body"></tbody></table></div>
  <p class="note" style="margin-top:16px"><b>Did you know?</b> All Shanxi province codes start with 035 (plus Shuozhou 0349). <b>0355</b> is Changzhi — so a local Changzhi landline could look like 0355-55xxxxx.</p>
</div></section>
{ad("footer", R)}'''

PAGES["area-codes.html"] = dict(title="China Area Codes — Find the City for 010, 021, 0355 & More | 035555.com",
    desc="Search China telephone area codes by code, city or province, including all Shanxi 035x codes such as 0351 Taiyuan and 0355 Changzhi.",
    body=areas, current="")

# ---------------- NUMERIC DOMAINS ----------------
def domains(R):
    return f'''
<section class="page-hero"><div class="wrap">
  <div class="breadcrumbs"><a href="index.html">Home</a> › Numeric Domains</div>
  <h1>Numeric Domain Scorer</h1>
  <p>Numbers are easier to type and remember than romanised Chinese, so numeric domains have long been prized by Chinese-speaking businesses and investors. Score any number domain's pattern strength in seconds.</p>
</div></section>
<section style="padding-top:8px"><div class="wrap grid g2" style="align-items:start">
  <div class="tool">
    <form id="domain-form"><label for="dm">Numeric domain</label><div class="tool-input"><input id="dm" placeholder="e.g. 035555.com" value="035555.com"><button class="btn btn-primary" type="submit">Score it</button></div></form>
    <div id="domain-out" class="result" aria-live="polite"></div>
  </div>
  <div class="card">
    <h3>What moves value</h3>
    <ul><li><b>Length:</b> only 100 two-digit and 1,000 three-digit .com names exist.</li>
    <li><b>Digits:</b> the market often treats names without 0 or 4 as a premium class; a leading 0 usually lowers demand.</li>
    <li><b>Pattern:</b> repeats (AAAA), mirrors (ABBA), pairs (AABB) and endings in 8 outperform random strings.</li>
    <li><b>Extension:</b> .com leads; .cn and .net follow for Chinese buyers.</li></ul>
    <p class="small muted">Buying or selling? Our concierge connects serious parties and can arrange escrow referrals.</p>
    <a class="btn btn-gold" href="leads.html?need=domain">Buy / sell a numeric domain</a>
  </div>
</div></section>
{ad("inContent", R)}'''

PAGES["numeric-domains.html"] = dict(title="Numeric Domain Scorer — Chinese Number Domain Value Factors | 035555.com",
    desc="Score a numeric domain's pattern strength: length, lucky digits, repeats and extension. Learn why Chinese buyers value number domains, and get a free appraisal.",
    body=domains, current="numeric-domains.html")

# ---------------- VIDEOS ----------------
def videos(R):
    return f'''
<section class="page-hero"><div class="wrap">
  <div class="breadcrumbs"><a href="index.html">Home</a> › Videos</div>
  <h1>Videos</h1>
  <p>Short explainers on number meanings, lucky numbers and Chinese internet culture. Subscribe to get new episodes.</p>
  <div class="hero-cta"><a class="btn btn-primary" data-yt-channel href="https://www.youtube.com/results?search_query=chinese+number+meanings" target="_blank" rel="noopener">▶ Subscribe on YouTube</a><a class="btn btn-ghost" href="careers.html">Become a creator</a></div>
</div></section>
<section style="padding-top:8px"><div class="wrap"><div class="grid g3" id="video-grid"></div></div></section>
{ad("footer", R)}
<section><div class="wrap"><div class="card center"><h2>Sponsor an episode</h2><p class="muted">Pre-roll mentions, pinned links and dedicated explainers. Great for language apps, travel, telecom and domain brands.</p><a class="btn btn-primary" href="advertise.html">See sponsorship options</a></div></div></section>'''

PAGES["videos.html"] = dict(title="Videos — Chinese Number Meanings Explained | 035555.com",
    desc="Watch short explainers on Chinese number meanings, lucky numbers and number slang like 520, 666 and 5555.",
    body=videos, current="videos.html")
