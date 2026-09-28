from layout import ad, newsletter

PAGES = {}

def art(R, crumb, h1, dek, body, related=True):
    rel = f'''<div class="card" style="margin-top:32px"><h3>Try it yourself</h3><p class="small muted">Decode any number instantly, or get a free shortlist of lucky options.</p><div class="hero-cta"><a class="btn btn-primary" href="{R}decoder.html">Open the decoder</a><a class="btn btn-ghost" href="{R}leads.html">Get a lucky number</a></div></div>
<div class="card" style="margin-top:18px"><h3>Get one number code a week</h3>{newsletter(R, "Guide")}</div>''' if related else ""
    return f'''<section class="page-hero"><div class="wrap article"><div class="breadcrumbs"><a href="{R}index.html">Home</a> › <a href="{R}guides/index.html">Guides</a> › {crumb}</div><h1>{h1}</h1><p>{dek}</p><p class="small muted">Updated September 2026 · 035555.com editorial</p></div></section>
<section style="padding-top:8px"><div class="wrap article">{body}{rel}</div></section>{ad("footer", R)}'''


def meaning(R):
    return art(R, "Meaning of 035555", "What does 035555 mean?", "One six-digit number, five different readings: sound, slang, numerology, geography and the domain market.", f'''
<div class="toc"><b>Contents</b><ol><li><a href="#sound">The sound reading</a></li><li><a href="#slang">The chat-code reading</a></li><li><a href="#five">The meaning of five</a></li><li><a href="#geo">Where 035 and 0355 point</a></li><li><a href="#domain">As a numeric domain</a></li><li><a href="#score">Luck score</a></li></ol></div>
<h2 id="sound">1. The sound reading</h2>
<p>In Mandarin, 035555 is read digit by digit: <b class="cn">零三五五五五</b> — <i>líng sān wǔ wǔ wǔ wǔ</i>. Chinese number meanings mostly come from <em>homophones</em>, words that sound alike:</p>
<ul><li><b>0 零 líng</b> — echoes 灵 (spirit, cleverness); in chat codes 0 often stands for 你 (nǐ, “you”).</li>
<li><b>3 三 sān</b> — echoes 生 (shēng, life/birth); in chat codes often 想 (xiǎng, “miss / think of”). It can also echo 散 (sàn, “scatter”).</li>
<li><b>5 五 wǔ</b> — echoes 我 (wǒ, “I/me”), 无 (wú, “nothing”) and the sob 呜 (wū).</li></ul>
<h2 id="slang">2. The chat-code reading</h2>
<p>Chinese internet users build sentences from digits — 520 is 我爱你 (“I love you”), 530 is 我想你 (“I miss you”). Applying the same logic:</p>
<ul><li><b>035</b> → 你想我 — “you miss me”.</li><li><b>5555</b> → 呜呜呜呜 — heavy (often playful) crying, a well-known chat expression.</li></ul>
<p>So <b>035555</b> can be read as a teasing <em>“you miss me… me-me-me”</em>, or as “you miss me — boo-hoo”. It's a light, emotional, very internet-native string.</p>
<h2 id="five">3. The meaning of five</h2>
<p>Beyond the sound, five is a structural number in Chinese thought: the <b>五行 Five Elements</b> (wood, fire, earth, metal, water), the <b>五福 Five Blessings</b> (longevity, wealth, health, virtue and a peaceful end), the five tones and five directions. A run of four 5s places heavy emphasis on that “five-fold completeness”. Three is similarly symbolic: 三才, the triad of Heaven, Earth and Humanity.</p>
<h2 id="geo">4. Where 035 and 0355 point</h2>
<p>In mainland China, landline area codes begin with 0. Every Shanxi province city code starts with <b>035</b> (plus Shuozhou 0349): Taiyuan 0351, Datong 0352 … and <b>0355 is Changzhi</b>. A number written 0355-55xxxxx would be a Changzhi landline. In Italy, <b>035</b> is the area code of Bergamo. See the <a href="{R}area-codes.html">area code finder</a>.</p>
<h2 id="domain">5. As a numeric domain</h2>
<p>Six-digit .com domains (“6N”) are a recognised asset class, largely driven by Chinese-speaking buyers who find numbers easier than romanised words. The market commonly treats names <em>without</em> 0 or 4 as a premium tier and discounts names that start with 0. 035555 starts with 0 — but its quadruple 5 (AAAA pattern) and memorable rhythm are genuine strengths. Try the <a href="{R}numeric-domains.html?d=035555.com">numeric domain scorer</a>.</p>
<h2 id="score">6. Luck score</h2>
<p>Our transparent engine rates 035555 around the low 60s — <b>“Good: balanced with a few positive notes.”</b> No avoided 4s, a strong repetition bonus, a positive 3, and neutral 0 and 5s. <a href="{R}decoder.html?n=035555">See the full breakdown →</a></p>
<p class="note">Meanings here are folk associations and internet slang, offered for education and entertainment. 035555.com claims no trademark in the number — see our <a href="{R}disclosure.html">disclosure</a>.</p>''')

PAGES["guides/meaning-of-035555.html"] = dict(title="What Does 035555 Mean? Chinese Number Meaning Explained | 035555.com",
    desc="035555 explained: Mandarin sound reading, chat-code meaning (你想我 + 5555 crying), the symbolism of five, the 0355 Changzhi area code and numeric-domain value.",
    body=meaning, article=True)


def digits(R):
    rows = [("0", "零", "líng", "灵 spirit · chat: 你 you", "Wholeness, a fresh start"), ("1", "一", "yī", "一 unity · 要 want", "Leadership, firsts"), ("2", "二", "èr", "爱 love (chat) · 易 easy", "Good things come in pairs"),
            ("3", "三", "sān", "生 life · 想 miss (chat)", "Growth, Heaven–Earth–Humanity"), ("4", "四", "sì", "死 death", "Most avoided digit"), ("5", "五", "wǔ", "我 me · 无 none · 呜 sob", "Five Elements, Five Blessings"),
            ("6", "六", "liù", "溜/顺 smooth", "Everything goes smoothly"), ("7", "七", "qī", "起 rise · 妻 wife · 气 anger", "Mixed; 7th month = Ghost Month"), ("8", "八", "bā", "发 prosper", "The luckiest digit"), ("9", "九", "jiǔ", "久 long-lasting", "Longevity, eternity")]
    t = "".join(f"<tr><td><b style='font-size:1.3rem'>{a}</b></td><td class='cn'>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in rows)
    return art(R, "Digit meanings 0–9", "Chinese number meanings: 0 to 9", "Why 8 is lucky, 4 is avoided and 5 can mean “me” or “crying” — every digit explained.", f'''
<div class="table-wrap"><table><thead><tr><th>Digit</th><th>Hanzi</th><th>Pinyin</th><th>Sounds like</th><th>Association</th></tr></thead><tbody>{t}</tbody></table></div>
<h2>Why sound matters</h2><p>Mandarin has many homophones, so a number is often “heard” as the word it resembles. That is why 8 (bā) evokes 发 (fā, to prosper) and 4 (sì) evokes 死 (sǐ, death). The effect is strong enough to shape real prices: phone numbers and licence plates full of 8s trade at premiums, and many buildings skip the 4th, 14th and 24th floors.</p>
<h2>Famous examples</h2><ul><li>The Beijing 2008 Olympics opened on 08/08/08 at 8:08 pm.</li><li>May 20 (5/20) has become an unofficial love day because 520 sounds like 我爱你.</li><li>Businesses love 168 (一路发, “prosper all the way”) and 518 (我要发, “I will prosper”).</li></ul>
<h2>Cantonese differences</h2><p>In Cantonese, 3 (saam) can echo 生 (life), 6 (luk) echoes 禄 (fortune), and 5 (ng) echoes 唔 (not) — so 5 can flip a phrase negative (e.g. 58 heard as “won't prosper”). Always consider the audience's dialect.</p>''')

PAGES["guides/chinese-digit-meanings.html"] = dict(title="Chinese Number Meanings 0–9: Lucky & Unlucky Digits Explained | 035555.com",
    desc="Every Chinese digit 0–9 explained: pronunciation, homophones, lucky and unlucky associations, Cantonese differences and famous examples.", body=digits, article=True)


def slang(R):
    return art(R, "Number slang guide", "Chinese number slang: the complete beginner's guide", "How 520, 1314, 666, 233, 88 and 5555 became part of everyday Chinese texting.", f'''
<p>Chinese texters turn digits into words because typing numbers is fast and the tones don't have to match exactly — only the rough sound. Here are the families you'll see most.</p>
<h2>Love codes</h2><ul><li><b>520</b> 我爱你 — I love you. <b>521</b> — I'm willing / I love you (reply).</li><li><b>1314</b> 一生一世 — for a lifetime; combined as <b>5201314</b>.</li><li><b>530</b> 我想你 — I miss you. <b>9420</b> 就是爱你 — it's you I love.</li></ul>
<h2>Feelings</h2><ul><li><b>555 / 5555</b> 呜呜 — crying. <b>7456</b> 气死我了 — I'm furious. <b>687</b> 对不起 — sorry.</li></ul>
<h2>Everyday chat</h2><ul><li><b>88 / 886</b> — bye-bye. <b>233</b> — LOL. <b>666</b> — awesome. <b>94</b> 就是 — exactly. <b>918</b> 加油吧 — go for it.</li></ul>
<h2>Work culture</h2><ul><li><b>996</b> — 9am–9pm, 6 days a week. <b>007</b> — always on. <b>1024</b> — Programmers' Day.</li></ul>
<h2>Handle with care</h2><ul><li><b>250</b> — fool. <b>748</b> — go to hell. <b>38</b> — a derogatory term for a gossipy woman. Avoid these in names, prices or gifts.</li></ul>
<p>Browse all entries in the <a href="{R}dictionary.html">Number Slang Dictionary</a>.</p>''')

PAGES["guides/chinese-number-slang.html"] = dict(title="Chinese Number Slang Guide: 520, 1314, 666, 233, 88 & 5555 | 035555.com",
    desc="Beginner's guide to Chinese number slang — love codes, feelings, everyday chat, work culture and codes to avoid.", body=slang, article=True)


def domains(R):
    return art(R, "Numeric domains guide", "Numeric domains: why Chinese buyers value number .coms", "Scarcity, easy typing and lucky sounds — the economics behind number domain names.", f'''
<h2>Why numbers?</h2><p>For Chinese speakers, numbers avoid the friction of romanising Chinese words, are universally readable, and can carry lucky meanings. That combination has made numeric domains a distinct, liquid market for over a decade.</p>
<h2>Scarcity drives price</h2><ul><li>There are only 100 two-digit (NN) and 1,000 three-digit (NNN) .com domains — all long registered.</li><li>Historical headline sales include 55.com (reported at about $2.3M in 2011) and 114.com (reported at about $2.1M in 2013).</li></ul>
<h2>What investors look for</h2><ul><li><b>Shorter is stronger</b> — every extra digit multiplies supply by ten.</li><li><b>“Chinese premium”</b> — names without 0 or 4 are commonly treated as a higher tier.</li><li><b>Patterns</b> — AAAA, ABAB, AABB and endings in 8 command more than random strings.</li><li><b>Extension</b> — .com first; .cn and .net follow.</li></ul>
<h2>Using a numeric domain</h2><p>The best numeric sites turn the number into a memorable brand and a useful product — a tool, a directory or a community — rather than a parked page. That's the approach this website takes.</p>
<p><a class="btn btn-primary" href="{R}numeric-domains.html">Score a numeric domain</a> <a class="btn btn-ghost" href="{R}leads.html?need=domain">Buy / sell one</a></p>
<p class="small muted">Sale figures are as publicly reported by industry sources; they are historical and not indicative of any current valuation.</p>''')

PAGES["guides/numeric-domains-guide.html"] = dict(title="Numeric Domains Guide: Why Chinese Buyers Value Number .COMs | 035555.com",
    desc="Why numeric domains are valued in China: scarcity of NN and NNN .coms, the 0/4 'Chinese premium', patterns and historical sales.", body=domains, article=True)


def index(R):
    items = [("meaning-of-035555.html", "What does 035555 mean?", "Sound, slang, numerology, geography and domain value."),
             ("chinese-digit-meanings.html", "Chinese number meanings 0–9", "Lucky and unlucky digits explained."),
             ("chinese-number-slang.html", "Chinese number slang guide", "520, 1314, 666, 233, 88, 5555 and more."),
             ("numeric-domains-guide.html", "Numeric domains guide", "Why number .coms are valued by Chinese buyers.")]
    cards = "".join(f'<a class="card" href="{h}"><h3>{t}</h3><p class="muted small">{d}</p><span class="small">Read →</span></a>' for h, t, d in items)
    return f'''<section class="page-hero"><div class="wrap"><div class="breadcrumbs"><a href="{R}index.html">Home</a> › Guides</div><h1>Guides</h1><p>In-depth, sourced explainers on numbers in Chinese language and culture.</p></div></section>
<section style="padding-top:8px"><div class="wrap"><div class="grid g2">{cards}</div></div></section>{ad("footer", R)}'''

PAGES["guides/index.html"] = dict(title="Guides — Chinese Number Meanings & Culture | 035555.com", desc="Guides to Chinese number meanings, number slang, lucky digits and numeric domains.", body=index, current="guides/index.html")
