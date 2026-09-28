from layout import ad, lead_form, newsletter, honey, INQ

PAGES = {}


def hero(crumb, h1, p):
    return f'''<section class="page-hero"><div class="wrap"><div class="breadcrumbs"><a href="index.html">Home</a> › {crumb}</div><h1>{h1}</h1><p>{p}</p></div></section>'''


def msg():
    return '<p class="form-msg" aria-live="polite"></p>'

# ---------------- LEADS ----------------
def leads(R):
    return hero("Lucky Number Concierge", "Lucky Number Concierge",
                "Get a free, personalised shortlist of lucky phone numbers, licence plates, numeric domains or auspicious dates — scored, explained and matched to your budget.") + f'''
<section style="padding-top:8px"><div class="wrap grid g2" style="align-items:start">
  {lead_form(R, fid="main-lf")}
  <div>
    <div class="card"><h3>How it works</h3>
      <ol><li><b>Tell us the goal</b> — what, budget, timeline. 60 seconds.</li>
      <li><b>We research</b> — availability across sellers and registries, scored with our luck engine.</li>
      <li><b>You get a shortlist</b> — 5–10 options with meanings in plain English.</li>
      <li><b>You decide</b> — buy direct, or ask us to help negotiate. No obligation.</li></ol></div>
    <div class="card" style="margin-top:18px"><h3>Who we help</h3>
      <div class="chips"><span class="tag luck">New business owners</span><span class="tag love">Couples picking dates</span><span class="tag slang">Car buyers</span><span class="tag emotion">Phone upgraders</span><span class="tag work">Domain investors</span><span class="tag luck">Brands entering Chinese markets</span></div></div>
    <div class="card" style="margin-top:18px"><h3>Selling a numeric domain or premium number?</h3><p class="small muted">List it with us. Choose “Buy / sell a numeric domain” and select “I'm selling” as budget.</p></div>
  </div>
</div></section>
<section><div class="wrap article">
  <h2 class="center">Concierge FAQ</h2>
  <details><summary>Is the shortlist really free?</summary><p>Yes. We earn from optional brokerage/partner fees only if you decide to proceed — always disclosed up front.</p></details>
  <details><summary>Which countries do you cover?</summary><p>Anywhere for domains. For phone numbers and plates, availability depends on local carriers and licensing authorities; we tell you honestly what's possible.</p></details>
  <details><summary>How fast will I hear back?</summary><p>Usually within 1 business day, and the shortlist within 24–48 hours.</p></details>
</div></section>'''

PAGES["leads.html"] = dict(title="Lucky Number Concierge — Get Lucky Phone Numbers, Plates & Numeric Domains | 035555.com",
    desc="Free shortlist of lucky phone numbers, licence plates, numeric domains and auspicious dates matched to your budget. Buyers and sellers welcome.",
    body=leads, current="")

# ---------------- SUPPORT / DONATE ----------------
def support(R):
    return hero("Support us", "Support 035555.com",
                "Every tool here is free. Your support pays for operations, promotion, new creators and contest prizes — and keeps ads light.") + f'''
<section style="padding-top:8px"><div class="wrap">
  <div class="grid g4">
    <div class="card"><div class="ico">运</div><h3>Operations</h3><p class="small muted">Hosting, domains, tools, research and data upkeep.</p></div>
    <div class="card"><div class="ico">推</div><h3>Promotion & marketing</h3><p class="small muted">Reaching learners and communities worldwide.</p></div>
    <div class="card"><div class="ico">才</div><h3>Hiring talent</h3><p class="small muted">Paying writers, translators, video creators and developers.</p></div>
    <div class="card"><div class="ico">奖</div><h3>Contests & prizes</h3><p class="small muted">Funding monthly challenges and prizes for the community.</p></div>
  </div>
</div></section>
<section style="padding-top:0"><div class="wrap grid g3">
  <div class="card tier"><h3>Supporter</h3><div class="price">$8</div><p class="muted small">≈ a lucky 8</p><ul><li>Name on supporters wall (optional)</li><li>Our thanks, forever</li></ul><button class="btn btn-ghost" data-amount="8">Choose $8</button></div>
  <div class="card tier featured"><span class="badge">Most popular</span><h3 style="margin-top:8px">Patron</h3><div class="price">$68</div><p class="muted small">六六大顺 — smooth sailing</p><ul><li>Everything in Supporter</li><li>Early access to new tools</li><li>Vote on the next contest theme</li></ul><button class="btn btn-primary" data-amount="68">Choose $68</button></div>
  <div class="card tier"><h3>Prize Sponsor</h3><div class="price">$888</div><p class="muted small">发发发 — triple prosperity</p><ul><li>Fund a monthly contest prize</li><li>Logo on contest page & video</li><li>Social shout-out</li></ul><button class="btn btn-ghost" data-amount="888">Choose $888</button></div>
</div></section>
<section style="padding-top:0"><div class="wrap grid g2" style="align-items:start">
  <div class="card"><h3>Give instantly</h3><div id="donate-links" class="hero-cta"></div>
    <p class="small muted" style="margin-top:12px">Recurring monthly support is available on platforms that offer it.</p></div>
  <form class="card" data-form data-subject="DONATION pledge" data-ok="Thank you! We'll email secure payment options and a receipt within 24 hours.">
    {honey()}<h3>Pledge form</h3>
    <div class="row2"><div class="field"><label for="pledge-amount">Amount (USD)</label><input id="pledge-amount" name="Amount" type="number" min="1" required></div>
    <div class="field"><label for="pf">Frequency</label><select id="pf" name="Frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
    <div class="field"><label for="pu">Direct my gift to</label><select id="pu" name="Designation"><option>Where it's needed most</option><option>Operations</option><option>Promotions & marketing</option><option>Hiring talent</option><option>Contests & prizes</option></select></div>
    <div class="row2"><div class="field"><label for="pn">Name</label><input id="pn" name="Name" required autocomplete="name"></div><div class="field"><label for="pe">Email</label><input id="pe" type="email" name="Email" required autocomplete="email"></div></div>
    <div class="field"><label for="pw">Show my name on the supporters wall?</label><select id="pw" name="Public credit"><option>Yes</option><option>No, keep me anonymous</option></select></div>
    <button class="btn btn-primary btn-block" type="submit">Send pledge</button>{msg()}
    <p class="small muted" style="margin:8px 0 0">035555.com is not a registered charity; contributions are not tax-deductible.</p>
  </form>
</div></section>'''

PAGES["support.html"] = dict(title="Support & Donate — Keep 035555.com Free | 035555.com",
    desc="Support free number-meaning tools. Donations fund operations, promotion, hiring creators, and monthly contest prizes.",
    body=support, current="")

# ---------------- CONTESTS ----------------
def contests(R):
    return hero("Contests", "Decode-a-Number Contests",
                "Monthly creative challenges with prizes. Explain a number, invent a clever code, or make a 30-second video — the community and judges pick winners.") + f'''
<section style="padding-top:8px"><div class="wrap grid g2" style="align-items:start">
  <div>
    <div class="card"><span class="badge">This month</span><h2 style="margin-top:10px">Challenge: “Tell the story of a number”</h2>
      <p>Pick any number (your birthday, phone ending, a price) and explain its meaning using Chinese sounds and slang — in a post, image or short video.</p>
      <div class="table-wrap"><table><tbody>
        <tr><th>1st prize</th><td>$88 gift card + featured video</td></tr>
        <tr><th>2nd prize</th><td>$66 gift card</td></tr>
        <tr><th>3rd prize</th><td>$18 gift card</td></tr>
        <tr><th>Community pick</th><td>Winner's number on the homepage for a month</td></tr>
      </tbody></table></div>
      <p class="small muted" style="margin-top:10px">Prizes funded by <a href="support.html">supporters</a> and <a href="advertise.html">sponsors</a>. Want to sponsor a prize? <a href="advertise.html">Talk to us</a>.</p></div>
    <div class="card" style="margin-top:18px"><h3>Official rules (summary)</h3>
      <ul class="small"><li>No purchase necessary. Open to entrants 18+ where contests are lawful; void where prohibited.</li><li>One entry per person per month. Entries must be original work.</li>
      <li>Judging: creativity 40%, accuracy 30%, clarity 30%. Judges' decisions are final.</li><li>Winners are notified by email and announced on this page within 14 days of the close.</li>
      <li>By entering you grant 035555.com a non-exclusive licence to display your entry with credit.</li><li>See the <a href="terms.html#contests">Terms</a> for full rules.</li></ul></div>
  </div>
  <form class="card" data-form data-subject="CONTEST entry" data-ok="Entry received — good luck! We'll confirm by email.">
    {honey()}<h3>Submit your entry</h3>
    <div class="row2"><div class="field"><label for="cn">Name / handle</label><input id="cn" name="Name" required></div><div class="field"><label for="ce">Email</label><input id="ce" type="email" name="Email" required></div></div>
    <div class="field"><label for="cnum">Your number</label><input id="cnum" name="Number" inputmode="numeric" required></div>
    <div class="field"><label for="cs">Your story / explanation</label><textarea id="cs" name="Entry" rows="6" required maxlength="3000"></textarea></div>
    <div class="field"><label for="cl">Link to image / video (optional)</label><input id="cl" name="Link" type="url" placeholder="https://"></div>
    <div class="field"><label for="cc">Country</label><input id="cc" name="Country" required></div>
    <label class="small" style="font-weight:500"><input type="checkbox" name="Rules accepted" value="Yes" required style="width:auto;margin-right:6px">I'm 18+ and accept the contest rules.</label>
    <button class="btn btn-primary btn-block" type="submit" style="margin-top:12px">Enter contest</button>{msg()}
  </form>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="card center"><h2>Winners</h2><p class="muted">Winners of each monthly challenge will be announced here. Enter now to be among the first.</p></div></div></section>'''

PAGES["contests.html"] = dict(title="Contests & Prizes — Decode-a-Number Challenge | 035555.com",
    desc="Monthly Decode-a-Number contest: explain a number's hidden meaning and win prizes. Free to enter.", body=contests, current="contests.html")

# ---------------- CAREERS ----------------
def careers(R):
    roles = [("Chinese–English Content Writer", "Remote · Freelance", "Write accurate, fun explainers on number meanings and culture. Native or near-native Mandarin."),
             ("YouTube / Shorts Creator & Editor", "Remote · Per video", "Script, shoot or edit 30–120s explainers. Paid per episode + revenue share on sponsored episodes."),
             ("SEO & Growth Specialist", "Remote · Part-time", "Keyword research, internal linking, programmatic pages for thousands of number codes."),
             ("Sponsorship & Ad Sales", "Remote · Commission", "Sell sponsorships to language apps, telecoms, travel and domain brands."),
             ("Community & Contest Moderator", "Remote · Part-time", "Run monthly contests, moderate entries, engage our social channels."),
             ("Front-end Developer (Contract)", "Remote · Project", "Build new interactive tools in vanilla JS; accessibility and performance first.")]
    cards = "".join(f'<div class="card"><h3>{t}</h3><p class="small"><span class="tag">{m}</span></p><p class="small muted">{d}</p><a class="btn btn-ghost btn-sm" href="#apply" onclick="document.getElementById(\'ar\').value=\'{t}\'">Apply</a></div>' for t, m, d in roles)
    return hero("Careers", "Careers & Creators", "We're a small, remote-first team building the web's friendliest guide to number meanings. Join as a freelancer, creator or partner.") + f'''
<section style="padding-top:8px"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
<section id="apply" style="padding-top:0"><div class="wrap article">
  <form class="card" data-form data-subject="CAREERS application" data-ok="Application received — thank you! We review every application and reply within a week.">
    {honey()}<h2>Apply</h2>
    <div class="field"><label for="ar">Role</label><select id="ar" name="Role" required><option value="">Select…</option>{"".join(f"<option>{t}</option>" for t, _, _ in roles)}<option>Open application</option></select></div>
    <div class="row2"><div class="field"><label for="an">Full name</label><input id="an" name="Name" required autocomplete="name"></div><div class="field"><label for="ae">Email</label><input id="ae" type="email" name="Email" required autocomplete="email"></div></div>
    <div class="row2"><div class="field"><label for="al">Portfolio / LinkedIn / CV link</label><input id="al" name="Portfolio" type="url" placeholder="https://" required></div><div class="field"><label for="ak">Languages</label><input id="ak" name="Languages" placeholder="e.g. English, Mandarin"></div></div>
    <div class="row2"><div class="field"><label for="av">Availability</label><select id="av" name="Availability"><option>Under 10 h/week</option><option>10–20 h/week</option><option>20+ h/week</option></select></div><div class="field"><label for="ag">Location / time zone</label><input id="ag" name="Location"></div></div>
    <div class="field"><label for="am">Why you? (short)</label><textarea id="am" name="Message" rows="4" required></textarea></div>
    <button class="btn btn-primary btn-block" type="submit">Submit application</button>{msg()}
  </form>
</div></section>'''

PAGES["careers.html"] = dict(title="Careers & Creators — Write, Film & Grow With Us | 035555.com",
    desc="Remote freelance roles: Chinese-English writers, video creators, SEO, ad sales, community moderators and developers.", body=careers, current="")

# ---------------- ADVERTISE ----------------
def advertise(R):
    return hero("Advertise", "Advertise, Sponsor & Partner",
                "Reach people actively researching lucky numbers, Chinese culture, phone numbers, plates and domains — a high-intent audience.") + f'''
<section style="padding-top:8px"><div class="wrap">
  <div class="grid g3">
    <div class="card tier"><h3>Tool Sponsor</h3><p class="muted small">Your brand on one tool page (e.g. Luck Checker).</p><ul><li>“Powered by” placement</li><li>Result-card CTA</li><li>Monthly performance report</li></ul><a class="btn btn-ghost" href="#adform">Enquire</a></div>
    <div class="card tier featured"><span class="badge">Best value</span><h3 style="margin-top:8px">Site-wide Partner</h3><p class="muted small">Premium placements across all pages.</p><ul><li>Header & in-content units</li><li>Newsletter feature</li><li>Contest prize co-branding</li></ul><a class="btn btn-primary" href="#adform">Enquire</a></div>
    <div class="card tier"><h3>Video & Social</h3><p class="muted small">Sponsored explainers and mentions.</p><ul><li>Dedicated or integrated video</li><li>Pinned links & description</li><li>Shorts cut-downs</li></ul><a class="btn btn-ghost" href="#adform">Enquire</a></div>
  </div>
  <div class="grid g2" style="margin-top:28px;align-items:start">
    <div class="card"><h3>Ideal partners</h3><div class="chips"><span class="tag">Language-learning apps</span><span class="tag">Telecom & eSIM</span><span class="tag">Domain registrars & marketplaces</span><span class="tag">Travel to Asia</span><span class="tag">Wedding & events</span><span class="tag">Feng shui & lifestyle</span><span class="tag">Car dealers</span><span class="tag">Real estate</span></div>
      <p class="small muted" style="margin-top:12px">Interested in acquiring this website or domain name outright, or a strategic partnership? <a href="{INQ}" target="_blank" rel="noopener">Contact the owner</a>.</p></div>
    <form class="card" id="adform" data-form data-subject="ADVERTISING / SPONSORSHIP inquiry" data-ok="Thanks! Our media kit and rates are on their way.">
      {honey()}<h3>Request media kit & rates</h3>
      <div class="row2"><div class="field"><label for="dn2">Name</label><input id="dn2" name="Name" required></div><div class="field"><label for="dc">Company</label><input id="dc" name="Company" required></div></div>
      <div class="row2"><div class="field"><label for="de2">Work email</label><input id="de2" type="email" name="Email" required></div><div class="field"><label for="dw">Website</label><input id="dw" name="Website" type="url" placeholder="https://"></div></div>
      <div class="row2"><div class="field"><label for="di">Interest</label><select id="di" name="Interest"><option>Site-wide Partner</option><option>Tool Sponsor</option><option>Video & Social</option><option>Contest prize sponsor</option><option>Buy website / domain</option><option>Partnership</option></select></div>
      <div class="field"><label for="db">Monthly budget</label><select id="db" name="Budget"><option>Under $500</option><option>$500 – $2,000</option><option>$2,000 – $10,000</option><option>$10,000+</option></select></div></div>
      <div class="field"><label for="dm2">Goals</label><textarea id="dm2" name="Message" rows="3"></textarea></div>
      <button class="btn btn-primary btn-block" type="submit">Send inquiry</button>{msg()}
    </form>
  </div>
</div></section>'''

PAGES["advertise.html"] = dict(title="Advertise & Sponsor — Reach a High-Intent Audience | 035555.com",
    desc="Sponsorships, site-wide ad placements, video integrations and contest co-branding on 035555.com.", body=advertise, current="")

# ---------------- CONTACT ----------------
def contact(R):
    return hero("Contact", "Contact us", "Questions, corrections, code suggestions, partnerships or press — send a message and we'll reply within 1–2 business days.") + f'''
<section style="padding-top:8px"><div class="wrap grid g2" style="align-items:start">
  <form class="card" data-form data-subject="CONTACT form">
    {honey()}
    <div class="row2"><div class="field"><label for="kn">Name</label><input id="kn" name="Name" required autocomplete="name"></div><div class="field"><label for="ke">Email</label><input id="ke" type="email" name="Email" required autocomplete="email"></div></div>
    <div class="field"><label for="kt">Topic</label><select id="kt" name="Topic"><option>General question</option><option>Suggest a number code</option><option>Correction</option><option>Lucky number request</option><option>Advertising / sponsorship</option><option>Buy this website / domain</option><option>Partnership</option><option>Press</option></select></div>
    <div class="field"><label for="km">Message</label><textarea id="km" name="Message" rows="6" required></textarea></div>
    <button class="btn btn-primary btn-block" type="submit">Send message</button>{msg()}
  </form>
  <div>
    <div class="card"><h3>Interested in this website or domain?</h3><p class="muted small">For acquisition of 035555.com, sponsorship, advertising or partnership, contact the owner directly.</p><a class="btn btn-gold" href="{INQ}" target="_blank" rel="noopener">Contact the owner →</a></div>
    <div class="card" style="margin-top:18px"><h3>Quick links</h3><ul><li><a href="leads.html">Get a lucky number shortlist</a></li><li><a href="advertise.html">Advertise with us</a></li><li><a href="careers.html">Work with us</a></li><li><a href="support.html">Support / donate</a></li></ul></div>
  </div>
</div></section>'''

PAGES["contact.html"] = dict(title="Contact — 035555.com", desc="Contact 035555.com for questions, code suggestions, partnerships, advertising or acquisition inquiries.", body=contact, current="")

# ---------------- ABOUT ----------------
def about(R):
    return hero("About", "About 035555.com", "A free, independent guide to what numbers mean — built for curious people everywhere.") + '''
<section style="padding-top:8px"><div class="wrap article">
  <p>Numbers carry meaning in every culture, but few places treat them as richly as the Chinese-speaking world, where a digit's <em>sound</em> can make a phone number, plate or apartment worth far more — or far less. 035555.com turns that knowledge into simple, honest tools.</p>
  <h2>What we believe</h2>
  <ul><li><b>Transparent over mystical.</b> Our luck score shows exactly why a number scores what it does.</li><li><b>Culture with respect.</b> We explain meanings in context and flag insults and sensitive codes.</li><li><b>Free at the core.</b> Tools stay free, supported by light advertising, sponsors and donors.</li></ul>
  <h2>How we make money</h2>
  <p>Display advertising (Google AdSense), sponsorships, optional concierge/brokerage fees disclosed up front, and voluntary donations. Sponsored content is always labelled.</p>
  <h2>Editorial standards</h2>
  <p>Entries are checked against multiple published sources and native speakers. Found an error? <a href="contact.html">Tell us</a> — corrections are made promptly.</p>
</div></section>'''

PAGES["about.html"] = dict(title="About — 035555.com", desc="About 035555.com: a free, transparent guide to number meanings in Chinese language and culture.", body=about, current="")

# ---------------- FAQ ----------------
def faq(R):
    qa = [("What does 035555 mean?", "It has no single fixed meaning. Read by sound it is líng-sān-wǔ-wǔ-wǔ-wǔ; in chat-code logic it can read playfully as “you miss me-me-me-me” or as a sigh followed by 5555 (crying). It also starts with 0355, the landline code for Changzhi, Shanxi. See <a href='guides/meaning-of-035555.html'>the full guide</a>."),
          ("What is the luckiest number in Chinese culture?", "8, because 八 (bā) sounds like 发 (fā), to prosper. 6 (smooth) and 9 (long-lasting) are also favoured."),
          ("What is the unluckiest number?", "4, because 四 (sì) sounds like 死 (sǐ), death. Combos like 14 and 74 are also avoided."),
          ("What does 520 mean?", "我爱你 — “I love you”. 5-2-0 (wǔ-èr-líng) loosely echoes wǒ-ài-nǐ."),
          ("What does 666 mean?", "“Awesome” or “smooth skills” — widely used in gaming and livestream chats."),
          ("What does 88 mean?", "“Bye-bye” (拜拜, bāi-bāi) in chat; also double prosperity."),
          ("Is the luck score accurate?", "It's a transparent heuristic for fun and comparison, not a prediction."),
          ("Can you help me buy a lucky number?", "Yes — the <a href='leads.html'>Lucky Number Concierge</a> sends a free shortlist."),
          ("How do I advertise?", "See <a href='advertise.html'>Advertise</a> for packages and the media-kit form.")]
    body = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qa)
    return hero("FAQ", "Frequently asked questions", "Quick answers about number meanings, our tools and services.") + f'<section style="padding-top:8px"><div class="wrap article">{body}</div></section>'

PAGES["faq.html"] = dict(title="FAQ — Chinese Number Meanings | 035555.com", desc="Answers to common questions about Chinese number meanings, lucky numbers, 520, 666, 88 and our tools.", body=faq, current="",
    jsonld={"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "What is the luckiest number in Chinese culture?", "acceptedAnswer": {"@type": "Answer", "text": "8, because it sounds like fa, to prosper."}},
        {"@type": "Question", "name": "What does 520 mean?", "acceptedAnswer": {"@type": "Answer", "text": "I love you (wo ai ni)."}}]})

# ---------------- LEGAL ----------------
def privacy(R):
    return hero("Privacy", "Privacy Policy", "Last updated: September 2026") + '''
<section style="padding-top:8px"><div class="wrap article">
  <h2>What we collect</h2><p>Information you submit in forms (such as name, email, and your message), and anonymous usage data if analytics is enabled. Tools like the decoder run in your browser; the numbers you type are not sent to us unless you submit a form.</p>
  <h2>How forms are processed</h2><p>Form submissions are delivered by a third-party form-processing service (FormSubmit) to our private inbox. We use your details only to respond to your request.</p>
  <h2>Advertising & cookies</h2><p>We may use Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You can opt out of personalised advertising at <a href="https://www.google.com/settings/ads" rel="noopener" target="_blank">Google Ads Settings</a> or <a href="https://www.aboutads.info" rel="noopener" target="_blank">aboutads.info</a>. We may also use Google Analytics to understand traffic.</p>
  <h2>Embedded content</h2><p>Videos are embedded via YouTube's privacy-enhanced mode and load only when you click play.</p>
  <h2>Your rights</h2><p>You may request access to, correction of, or deletion of your personal data via our <a href="contact.html">contact form</a>. Where GDPR, PIPEDA, CCPA or similar laws apply, we honour those rights.</p>
  <h2>Retention</h2><p>We keep form messages only as long as needed to respond and for legitimate record-keeping.</p>
  <h2>Children</h2><p>This site is not directed at children under 13, and contests are for adults 18+.</p>
  <h2>Contact</h2><p>Questions about this policy: use the <a href="contact.html">contact form</a>.</p>
</div></section>'''

PAGES["privacy.html"] = dict(title="Privacy Policy — 035555.com", desc="How 035555.com collects, uses and protects information, including cookies and Google AdSense.", body=privacy, current="")


def terms(R):
    return hero("Terms", "Terms of Use", "Last updated: September 2026") + '''
<section style="padding-top:8px"><div class="wrap article">
  <h2>Use of the site</h2><p>Content and tools are provided “as is” for education and entertainment. Cultural meanings and luck scores are not predictions, and no outcome is guaranteed. Do not rely on them for financial, legal or medical decisions.</p>
  <h2>Concierge & brokerage</h2><p>Shortlists are free and non-binding. Any transaction is between you and the seller; any fee we charge is disclosed and agreed in writing before you proceed. Numeric domain “pattern scores” are heuristics, not appraisals.</p>
  <h2 id="contests">Contests</h2><p>No purchase necessary. Open to individuals 18+ where lawful; void where prohibited. One entry per person per contest. Entries must be original and must not infringe others' rights. Winners are selected by judges on creativity, accuracy and clarity. Prizes are non-transferable; we may substitute a prize of equal or greater value. Winners may need to confirm eligibility. By entering, you grant us a non-exclusive, royalty-free licence to display your entry with credit.</p>
  <h2>Donations</h2><p>Donations are voluntary, support site operations, and are non-refundable except where required by law. 035555.com is not a registered charity; donations are not tax-deductible.</p>
  <h2>User submissions</h2><p>You're responsible for what you submit. We may edit or remove submissions at our discretion.</p>
  <h2>Intellectual property</h2><p>Site design, text, tools and code are protected by copyright. See our <a href="disclosure.html">Trademark & Copyright Disclosure</a>.</p>
  <h2>Limitation of liability</h2><p>To the fullest extent permitted by law, we are not liable for indirect or consequential damages arising from use of the site.</p>
  <h2>Changes</h2><p>We may update these terms; continued use means acceptance.</p>
</div></section>'''

PAGES["terms.html"] = dict(title="Terms of Use — 035555.com", desc="Terms of use for 035555.com, including contest rules, donations and concierge terms.", body=terms, current="")


def disclosure(R):
    return hero("Trademark & Copyright", "Trademark & Copyright Disclosure", "Please read — this explains how we use the number “035555” and third-party names.") + f'''
<section style="padding-top:8px"><div class="wrap article">
  <h2>1. The number “035555”</h2>
  <p>“035555” is a numeric string. We use it descriptively as our domain name (035555.com) and as an example of how numbers are read. <b>We do not claim any trademark, service mark or exclusive right in the number 035555</b>, in any Chinese reading of it, or in any other number or number code on this site.</p>
  <p>This site is <b>not affiliated with, endorsed by, or sponsored by</b> any company, brand, telephone subscriber, carrier, government body, or organisation that uses the digits 035555 or any similar sequence — including any telephone number in the 0355 (Changzhi, Shanxi, China) area code or the 035 (Bergamo, Italy) area code. Any resemblance to a real phone number, product code or registration number is coincidental.</p>
  <h2>2. Third-party trademarks</h2>
  <p>Google, AdSense, YouTube, PayPal, Stripe, Ko-fi, Buy Me a Coffee, GitHub and other names mentioned are trademarks of their respective owners, used only to identify their services. No endorsement is implied.</p>
  <h2>3. Number slang and cultural meanings</h2>
  <p>Chinese number meanings and slang (e.g. 520, 1314, 666, 5555) are part of shared language and culture and are not owned by anyone. Our explanations, selection, arrangement, scoring method and code are original works.</p>
  <h2>4. Our copyright</h2>
  <p>© 2026 035555.com. The site's original text, design, graphics and software are protected by copyright. You may quote short excerpts with a link back. Do not republish full pages or tools without permission.</p>
  <h2>5. Videos</h2>
  <p>Embedded YouTube videos remain the property of their creators and are shown via YouTube's standard embed player under YouTube's Terms of Service.</p>
  <h2>6. Takedown / infringement notices</h2>
  <p>If you believe content here infringes your rights, send a notice via our <a href="contact.html">contact form</a> with: your contact details, the work or mark concerned, the URL of the material, a good-faith statement, and a statement that the information is accurate and that you are authorised to act. We respond promptly and remove material where appropriate.</p>
  <h2>7. Domain inquiries</h2>
  <p>Inquiries about the website, the domain name, sponsorship, advertising or partnership: <a href="{INQ}" target="_blank" rel="noopener">contact the owner</a>.</p>
</div></section>'''

PAGES["disclosure.html"] = dict(title="Trademark & Copyright Disclosure — 035555.com", desc="035555.com claims no trademark in the number 035555 and is not affiliated with any organisation using these digits. Copyright and takedown information.", body=disclosure, current="")


def notfound(R):
    return f'''<section class="page-hero center"><div class="wrap"><h1>404 <span class="cn muted">呜呜呜呜</span></h1><p style="margin:0 auto 20px">This page is crying — it doesn't exist. (5555 means “sobbing” in Chinese chat.)</p><a class="btn btn-primary" href="{R}index.html">Go home</a> <a class="btn btn-ghost" href="{R}decoder.html">Decode a number</a></div></section>'''

PAGES["404.html"] = dict(title="Page not found — 035555.com", desc="Page not found.", body=notfound, current="", abs_root=True)
