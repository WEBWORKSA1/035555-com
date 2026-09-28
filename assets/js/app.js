/* 035555.com — app logic (vanilla JS, no dependencies) */
(function () {
  "use strict";
  var C = window.SITE_CONFIG || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
    sget: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    sset: function (k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }
  };
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function digitsOnly(s) { return String(s || "").replace(/\D/g, ""); }

  /* ---------- Theme ---------- */
  var savedTheme = store.get("theme");
  if (savedTheme) document.documentElement.setAttribute("data-theme", savedTheme);
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-theme-toggle]");
    if (!t) return;
    var cur = document.documentElement.getAttribute("data-theme") ||
      (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    var next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    store.set("theme", next);
  });

  /* ---------- Nav ---------- */
  var toggle = $(".menu-toggle"), menu = $(".menu");
  if (toggle && menu) toggle.addEventListener("click", function () {
    var open = menu.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });
  $$(".year").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Back to top / sticky CTA ---------- */
  var bt = $(".back-top"), sc = $(".sticky-cta");
  window.addEventListener("scroll", function () {
    var y = window.scrollY;
    if (bt) bt.classList.toggle("show", y > 700);
    if (sc) sc.classList.toggle("show", y > 500);
  }, { passive: true });
  if (bt) bt.addEventListener("click", function () { window.scrollTo({ top: 0 }); });

  /* ---------- Cookie notice ---------- */
  var ck = $(".cookie");
  if (ck && !store.get("cookieOk")) {
    ck.classList.add("show");
    $$("[data-cookie-ok]", ck).forEach(function (b) { b.addEventListener("click", function () { store.set("cookieOk", "1"); ck.classList.remove("show"); }); });
  }

  /* ---------- Analytics (optional) ---------- */
  if (C.ga4Id) {
    var g = document.createElement("script"); g.async = true;
    g.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(C.ga4Id);
    document.head.appendChild(g);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag("js", new Date()); gtag("config", C.ga4Id);
  }
  function track(name, params) { if (window.gtag) window.gtag("event", name, params || {}); }

  /* ---------- AdSense ---------- */
  var slots = $$("[data-ad]");
  if (C.adsenseClient) {
    var a = document.createElement("script"); a.async = true; a.crossOrigin = "anonymous";
    a.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + encodeURIComponent(C.adsenseClient);
    document.head.appendChild(a);
    slots.forEach(function (s) {
      var key = s.getAttribute("data-ad"), slotId = (C.adsenseSlots || {})[key];
      var ins = document.createElement("ins");
      ins.className = "adsbygoogle"; ins.style.display = "block";
      ins.setAttribute("data-ad-client", C.adsenseClient);
      if (slotId) ins.setAttribute("data-ad-slot", slotId);
      ins.setAttribute("data-ad-format", "auto"); ins.setAttribute("data-full-width-responsive", "true");
      var box = $(".ad-box", s); box.innerHTML = ""; box.style.border = "0"; box.appendChild(ins);
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  }

  /* ---------- Forms (FormSubmit AJAX; inbox never rendered) ---------- */
  function endpoint() {
    var id = C.formAlias;
    if (!id) { try { id = atob((C._k || []).join("")).split("").reverse().join(""); } catch (e) { id = ""; } }
    return "https://formsubmit.co/ajax/" + id;
  }
  function wireForm(form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = $(".form-msg", form);
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var fd = new FormData(form);
      if (fd.get("_honey")) return;
      var data = {};
      fd.forEach(function (v, k) {
        if (k === "_honey") return;
        data[k] = data[k] ? data[k] + ", " + v : v;
      });
      data._subject = "[035555.com] " + (form.getAttribute("data-subject") || "Website inquiry");
      data._template = "table"; data._captcha = "false";
      data["Page"] = location.href;
      var btn = $("button[type=submit]", form); if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = "Sending…"; }
      fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && String(res.j.success) !== "false") {
            form.reset();
            if (msg) { msg.className = "form-msg ok"; msg.textContent = form.getAttribute("data-ok") || "Thank you — we received your message and will reply shortly."; }
            track("generate_lead", { form: form.getAttribute("data-subject") || "form" });
            var steps = $$(".step", form); if (steps.length) goStep(form, 0);
          } else { throw new Error("fail"); }
        })
        .catch(function () {
          if (msg) { msg.className = "form-msg err"; msg.innerHTML = "Sorry, that didn't go through. Please try again, or use the <a href=\"" + esc(C.inquiryUrl) + "\" target=\"_blank\" rel=\"noopener\">contact page</a>."; }
        })
        .then(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; } });
    });
  }
  $$("form[data-form]").forEach(wireForm);

  /* Multi-step forms */
  function goStep(form, i) {
    var steps = $$(".step", form), bars = $$(".steps span", form);
    steps.forEach(function (s, k) { s.classList.toggle("on", k === i); });
    bars.forEach(function (b, k) { b.classList.toggle("on", k <= i); });
    form.dataset.step = i;
  }
  $$("form[data-steps]").forEach(function (form) {
    goStep(form, 0);
    form.addEventListener("click", function (e) {
      var n = e.target.closest("[data-next]"), p = e.target.closest("[data-prev]");
      var i = +form.dataset.step || 0;
      if (n) {
        var cur = $$(".step", form)[i], bad = $$("input,select,textarea", cur).filter(function (el) { return !el.checkValidity(); });
        if (bad.length) { bad[0].reportValidity(); return; }
        goStep(form, i + 1);
      }
      if (p) goStep(form, Math.max(0, i - 1));
    });
  });
  /* Prefill lead forms from URL (?need=domain&ref=...) */
  var params = new URLSearchParams(location.search);
  if (params.get("need")) $$("input[name='Need'][value='" + params.get("need").replace(/'/g, "") + "']").forEach(function (r) { r.checked = true; });
  if (params.get("ref")) $$("input[name='Reference number']").forEach(function (r) { r.value = params.get("ref"); });

  /* ---------- Exit-intent modal ---------- */
  var modal = $("#lead-modal");
  function openModal() { if (!modal || store.sget("modalShown")) return; modal.classList.add("open"); store.sset("modalShown", "1"); var f = $("input", modal); if (f) f.focus(); }
  if (modal) {
    document.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY < 8) openModal(); });
    setTimeout(openModal, 45000);
    modal.addEventListener("click", function (e) { if (e.target === modal || e.target.closest(".close")) modal.classList.remove("open"); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") modal.classList.remove("open"); });
  }

  /* ---------- Luck engine ---------- */
  var D = window.DIGITS || {};
  var GOOD = { "8888": 14, "888": 10, "88": 7, "666": 8, "66": 5, "999": 8, "99": 5, "168": 9, "1688": 10, "6688": 10, "518": 8, "516": 6, "1314": 7, "520": 6, "521": 5, "3399": 6, "3344": 5, "918": 4 };
  var BAD = { "4444": -18, "444": -14, "44": -10, "14": -8, "74": -8, "748": -8, "250": -8, "514": -8, "0748": -6, "0487": -6, "54": -3 };
  function luck(numStr) {
    var s = digitsOnly(numStr);
    if (!s) return null;
    var sum = 0; s.split("").forEach(function (d) { sum += (D[d] || { vibe: 0 }).vibe; });
    var score = 50 + (sum / s.length) * 10, hits = [];
    Object.keys(GOOD).forEach(function (k) { if (s.indexOf(k) > -1) { score += GOOD[k]; hits.push({ c: k, v: GOOD[k] }); } });
    Object.keys(BAD).forEach(function (k) { if (s.indexOf(k) > -1) { score += BAD[k]; hits.push({ c: k, v: BAD[k] }); } });
    var runs = s.match(/(\d)\1{2,}/g) || [];
    runs.forEach(function (r) { var v = r[0] === "4" ? -10 : Math.min(15, 3 * (r.length - 1)); score += v; hits.push({ c: r, v: v, run: true }); });
    var last = s[s.length - 1];
    if ("869".indexOf(last) > -1) { score += 5; hits.push({ c: "ends " + last, v: 5 }); }
    if (last === "4") { score -= 8; hits.push({ c: "ends 4", v: -8 }); }
    score = Math.max(1, Math.min(99, Math.round(score)));
    var verdict = score >= 85 ? "Exceptional — a number people pay a premium for." :
      score >= 70 ? "Very lucky — strong, positive associations." :
      score >= 55 ? "Good — balanced with a few positive notes." :
      score >= 40 ? "Neutral — no strong luck either way." : "Challenging — contains commonly avoided sounds.";
    return { s: s, score: score, hits: hits, verdict: verdict };
  }
  window.LUCK = luck;
  function slangHits(s) {
    var out = [], seen = {};
    (window.SLANG || []).forEach(function (e) {
      if (e[0].length >= 2 && /^\d+$/.test(e[0]) && s.indexOf(e[0]) > -1 && !seen[e[0] + e[4]]) { seen[e[0] + e[4]] = 1; out.push(e); }
    });
    return out.sort(function (a, b) { return b[0].length - a[0].length; });
  }
  function gauge(score) { return '<div class="gauge" style="--v:' + score + '" role="img" aria-label="Luck score ' + score + ' out of 100"><span>' + score + "</span></div>"; }
  function hitsHtml(h) {
    if (!h.length) return '<p class="muted small">No strong lucky or unlucky combinations found.</p>';
    return '<div class="chips">' + h.map(function (x) { return '<span class="tag ' + (x.v > 0 ? "luck" : "caution") + '">' + esc(x.c) + " " + (x.v > 0 ? "+" : "") + x.v + "</span>"; }).join("") + "</div>";
  }
  function areaHit(s) {
    var m = (window.AREA_CODES || []).filter(function (a) { return s.indexOf(a[0]) === 0; });
    return m.length ? m.sort(function (a, b) { return b[0].length - a[0].length; })[0] : null;
  }
  function share(title) {
    var url = location.href;
    if (navigator.share) navigator.share({ title: title, url: url }).catch(function () {});
    else if (navigator.clipboard) navigator.clipboard.writeText(url).then(function () { alert("Link copied!"); });
  }
  window.SHARE = share;

  /* ---------- Decoder ---------- */
  var dec = $("#decoder-form");
  if (dec) {
    var out = $("#decoder-out");
    var run = function (val) {
      var s = digitsOnly(val).slice(0, 24);
      if (!s) { out.innerHTML = '<p class="muted">Type a number made of digits 0–9.</p>'; return; }
      var L = luck(s), sl = slangHits(s), ar = areaHit(s);
      var rows = s.split("").map(function (d) {
        var x = D[d]; var cls = x.vibe > 0 ? "good" : x.vibe < 0 ? "bad" : "";
        return '<div class="digit-row"><div class="d ' + cls + '">' + d + "</div><div><b class='cn'>" + x.zh + "</b> <span class='muted'>" + x.py + "</span> — sounds like " + esc(x.sound) + '<div class="small muted">Chat code: ' + esc(x.slang) + "</div></div></div>";
      }).join("");
      var zh = s.split("").map(function (d) { return D[d].zh; }).join("");
      if (dec.hasAttribute("data-compact")) {
        out.innerHTML = '<div class="score">' + gauge(L.score) + '<div><h3>' + esc(s) + ' <span class="cn muted">' + zh + "</span></h3><p>" + L.verdict + "</p>" + hitsHtml(L.hits) + "</div></div>" +
          (sl.length ? '<p class="small" style="margin-top:12px"><b>Hidden codes:</b> ' + sl.slice(0, 3).map(function (e) { return e[0] + " " + esc(e[1]) + " (" + esc(e[3]) + ")"; }).join(" · ") + "</p>" : "") +
          '<a class="btn btn-primary btn-sm" href="decoder.html?n=' + s + '">Full breakdown →</a>';
        return;
      }
      out.innerHTML =
        '<div class="score">' + gauge(L.score) + '<div><h3>' + esc(s) + ' <span class="cn muted">' + zh + "</span></h3><p>" + L.verdict + "</p>" + hitsHtml(L.hits) + "</div></div>" +
        (sl.length ? '<h3 style="margin-top:20px">Hidden chat codes inside</h3><div class="grid g2">' + sl.slice(0, 8).map(function (e) { return '<div class="card"><span class="tag ' + e[4] + '">' + e[4] + '</span><h3>' + e[0] + ' <span class="cn">' + esc(e[1]) + '</span></h3><p class="small">' + esc(e[3]) + "</p></div>"; }).join("") + "</div>" : "") +
        (ar ? '<p class="note" style="margin-top:16px"><b>Area code match:</b> starts with ' + ar[0] + " — " + ar[1] + ", " + ar[2] + " (mainland China landline format).</p>" : "") +
        '<h3 style="margin-top:20px">Digit by digit</h3><div class="digit-rows">' + rows + "</div>" +
        '<div class="hero-cta" style="margin-top:18px"><a class="btn btn-primary" href="leads.html?need=number&ref=' + encodeURIComponent(s) + '">Find me a luckier number</a><button class="btn btn-ghost" type="button" onclick="SHARE(\'Number ' + s + '\')">Share result</button></div>';
      try { history.replaceState(null, "", "?n=" + s); } catch (e) {}
      track("decode_number", { length: s.length });
    };
    dec.addEventListener("submit", function (e) { e.preventDefault(); run($("input", dec).value); });
    $$("[data-try]").forEach(function (b) { b.addEventListener("click", function () { $("input", dec).value = b.getAttribute("data-try"); run(b.getAttribute("data-try")); }); });
    var n0 = params.get("n") || dec.getAttribute("data-default");
    if (n0) { $("input", dec).value = n0; run(n0); }
  }

  /* ---------- Luck checker ---------- */
  var lc = $("#luck-form");
  if (lc) {
    lc.addEventListener("submit", function (e) {
      e.preventDefault();
      var type = $("select", lc).value, raw = $("input", lc).value, L = luck(raw), o = $("#luck-out");
      if (!L) { o.innerHTML = '<p class="muted">Enter a number with at least one digit.</p>'; return; }
      var tips = {
        phone: "For phone numbers, the last 4 digits matter most — endings like 8888, 6688 or 1688 carry the highest premiums.",
        plate: "Plates are short and public: avoid 4 and 14/74 combos; repeated 8s or 6s signal status.",
        house: "Addresses with 4 are often discounted in Chinese-speaking markets; 8 and 6 are favored.",
        domain: "For numeric domains, shorter is stronger, patterns (AAAA, ABAB) beat random, and leading 0/4 lower demand.",
        date: "For dates, favor 6, 8, 9 and avoid 4 — many couples pick dates like the 8th, 18th or 28th.",
        business: "For business numbers, 168 (prosper all the way) and 518 (I will prosper) are classic choices."
      };
      o.innerHTML = '<div class="score">' + gauge(L.score) + "<div><h3>" + esc(L.s) + "</h3><p>" + L.verdict + "</p>" + hitsHtml(L.hits) + "</div></div>" +
        '<p class="note" style="margin-top:16px">' + tips[type] + "</p>" +
        '<div class="card" style="margin-top:16px"><h3>Want a ' + (L.score >= 80 ? "matching" : "90+") + " " + type + " number?</h3><p class='small muted'>Tell us your budget — we'll send a shortlist of available options.</p><a class='btn btn-primary' href='leads.html?need=" + type + "&ref=" + encodeURIComponent(L.s) + "'>Get my free shortlist</a></div>";
      track("luck_check", { type: type });
    });
  }

  /* ---------- Generator ---------- */
  var gen = $("#gen-form");
  if (gen) {
    function mulberry(a) { return function () { a |= 0; a = a + 0x6D2B79F5 | 0; var t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
    gen.addEventListener("submit", function (e) {
      e.preventDefault();
      var purpose = $("[name=purpose]", gen).value, len = Math.max(3, Math.min(11, +$("[name=len]", gen).value || 6)), bd = $("[name=bd]", gen).value;
      var pools = { wealth: "8886699135", love: "5201314952", career: "1686898132", health: "9966881235", balance: "1235678960" };
      var seeds = { wealth: ["168", "518", "88", "888", "6688"], love: ["520", "1314", "521", "3344", "9420"], career: ["168", "1688", "66", "918"], health: ["99", "999", "3399", "66"], balance: ["66", "88", "99", "168"] };
      var seed = bd ? +digitsOnly(bd) : Date.now(); var rnd = mulberry(seed + len * 7 + purpose.length);
      var pool = pools[purpose], cands = [];
      for (var i = 0; i < 400; i++) {
        var s = "";
        if (rnd() < 0.6) { var sd = seeds[purpose][Math.floor(rnd() * seeds[purpose].length)]; s = sd; }
        while (s.length < len) s += pool[Math.floor(rnd() * pool.length)];
        s = s.slice(0, len);
        if (rnd() < 0.5) s = s.split("").reverse().join("");
        if (s.indexOf("4") > -1) continue;
        cands.push(luck(s));
      }
      var uniq = {}, best = cands.filter(function (c) { if (uniq[c.s]) return false; uniq[c.s] = 1; return true; }).sort(function (a, b) { return b.score - a.score; }).slice(0, 9);
      $("#gen-out").innerHTML = '<div class="grid g3">' + best.map(function (b) {
        return '<div class="card"><div class="score" style="gap:12px"><div class="gauge" style="--v:' + b.score + ';width:64px;height:64px"><span style="width:48px;height:48px;font-size:1rem">' + b.score + '</span></div><div><h3 class="mono" style="margin:0">' + b.s + '</h3><a class="small" href="decoder.html?n=' + b.s + '">Decode →</a></div></div></div>';
      }).join("") + '</div><p class="note" style="margin-top:16px">Like one of these? We can check real-world availability as a phone number, plate or domain. <a href="leads.html?need=number">Request availability →</a></p>';
      track("generate_numbers", { purpose: purpose });
    });
  }

  /* ---------- Dictionary ---------- */
  var dict = $("#dict-list");
  if (dict) {
    var q = $("#dict-q"), cat = $("#dict-cat"), count = $("#dict-count");
    var render = function () {
      var term = (q.value || "").trim().toLowerCase(), c = cat.value;
      var list = (window.SLANG || []).filter(function (e) {
        return (!c || e[4] === c) && (!term || (e.join(" ").toLowerCase().indexOf(term) > -1));
      });
      count.textContent = list.length + " code" + (list.length === 1 ? "" : "s");
      dict.innerHTML = list.map(function (e) {
        return '<div class="card entry" id="code-' + esc(e[0]) + '"><div class="code">' + esc(e[0]) + '</div><div><div class="zh">' + esc(e[1]) + ' <span class="muted small">' + esc(e[2]) + '</span></div><p style="margin:.2em 0 .4em">' + esc(e[3]) + '</p><span class="tag ' + e[4] + '">' + e[4] + "</span>" + (/^\d+$/.test(e[0]) ? ' <a class="small" href="decoder.html?n=' + e[0] + '">Decode</a>' : "") + "</div></div>";
      }).join("") || '<p class="muted">No codes match. <a href="contact.html">Suggest one</a>.</p>';
    };
    q.addEventListener("input", render); cat.addEventListener("change", render);
    $$("[data-cat]").forEach(function (b) { b.addEventListener("click", function () { cat.value = b.getAttribute("data-cat"); $$("[data-cat]").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); }); render(); }); });
    if (params.get("q")) q.value = params.get("q");
    render();
  }

  /* ---------- Area codes ---------- */
  var at = $("#area-body");
  if (at) {
    var aq = $("#area-q");
    var ra = function () {
      var t = (aq.value || "").toLowerCase().trim();
      at.innerHTML = (window.AREA_CODES || []).filter(function (a) { return !t || a.join(" ").toLowerCase().indexOf(t) > -1; })
        .map(function (a) { return "<tr><td class='mono'><b>" + a[0] + "</b></td><td>" + esc(a[1]) + "</td><td>" + esc(a[2]) + "</td><td class='mono small'>+86 " + a[0].replace(/^0/, "") + "</td></tr>"; }).join("") ||
        "<tr><td colspan='4' class='muted'>No match.</td></tr>";
    };
    aq.addEventListener("input", ra); ra();
  }

  /* ---------- Numeric domain estimator ---------- */
  var de = $("#domain-form");
  if (de) {
    de.addEventListener("submit", function (e) {
      e.preventDefault();
      var raw = $("input", de).value.trim().toLowerCase().replace(/^https?:\/\//, "").replace(/^www\./, "");
      var parts = raw.split("."), label = parts[0] || "", tld = parts.slice(1).join(".") || "com", o = $("#domain-out");
      if (!/^\d{1,10}$/.test(label)) { o.innerHTML = '<p class="muted">Enter a numeric domain such as 035555.com or 1688.net.</p>'; return; }
      var pts = 0, why = [];
      var lenPts = { 1: 60, 2: 52, 3: 44, 4: 34, 5: 24, 6: 16, 7: 8, 8: 4 }[label.length] || 0;
      pts += lenPts; why.push(["Length " + label.length, lenPts]);
      var tldPts = tld === "com" ? 16 : ["cn", "net"].indexOf(tld) > -1 ? 8 : 2; pts += tldPts; why.push(["." + tld, tldPts]);
      if (label.indexOf("4") > -1) { pts -= 8; why.push(["Contains 4", -8]); }
      if (label[0] === "0") { pts -= 6; why.push(["Leading 0", -6]); }
      if (!/[04]/.test(label)) { pts += 6; why.push(["No 0 or 4 (“Chinese premium”)", 6]); }
      if (/^(\d)\1+$/.test(label)) { pts += 18; why.push(["All same digit", 18]); }
      else {
        var run = (label.match(/(\d)\1{2,}/g) || []).reduce(function (m, r) { return Math.max(m, r.length); }, 0);
        if (run >= 3) { var rp = 3 * run; pts += rp; why.push(["Run of " + run + " repeated digits", rp]); }
        if (/^(\d\d)\1+$/.test(label) || /^(\d{3})\1$/.test(label)) { pts += 8; why.push(["Repeating pattern (ABAB / ABCABC)", 8]); }
        if ("0123456789".indexOf(label) > -1 || "9876543210".indexOf(label) > -1) { pts += 8; why.push(["Sequential", 8]); }
      }
      if (/8$/.test(label)) { pts += 4; why.push(["Ends in 8", 4]); }
      var tiers = [[70, "Ultra-premium", "Top-tier scarcity. Seek a professional broker and escrow."], [52, "Premium", "Strong end-user and investor demand."], [38, "Strong", "Solid pattern with a real buyer pool."], [24, "Standard", "Liquid among numeric-domain investors; value depends on pattern."], [0, "Entry", "Speculative; best as a brandable or personal number."]];
      var tier = tiers.filter(function (t) { return pts >= t[0]; })[0];
      o.innerHTML = '<div class="card"><span class="badge">' + tier[1] + '</span><h3 style="margin-top:10px">' + esc(label + "." + tld) + " — pattern score " + Math.max(0, pts) + "</h3><p>" + tier[2] + "</p>" +
        '<div class="table-wrap"><table><thead><tr><th>Factor</th><th>Effect</th></tr></thead><tbody>' + why.map(function (w) { return "<tr><td>" + esc(w[0]) + "</td><td>" + (w[1] > 0 ? "+" : "") + w[1] + "</td></tr>"; }).join("") + "</tbody></table></div>" +
        '<p class="small muted" style="margin-top:12px">Pattern score is an educational heuristic, not an appraisal. Actual prices depend on comparable sales, traffic and buyer demand.</p>' +
        '<a class="btn btn-primary" href="leads.html?need=domain&ref=' + encodeURIComponent(label + "." + tld) + '">Get a free expert appraisal</a></div>';
      track("domain_estimate", { len: label.length });
    });
    if (params.get("d")) $("input", de).value = params.get("d");
    if ($("input", de).value) de.dispatchEvent(new Event("submit", { cancelable: true }));
  }

  /* ---------- Videos ---------- */
  var vg = $("#video-grid");
  if (vg) {
    var lim = +vg.getAttribute("data-limit") || 99;
    vg.innerHTML = (C.videos || []).slice(0, lim).map(function (v) {
      if (v.id) return '<figure style="margin:0"><div class="video" data-yt="' + esc(v.id) + '" role="button" tabindex="0" aria-label="Play: ' + esc(v.title) + '"><img loading="lazy" alt="" src="https://i.ytimg.com/vi/' + esc(v.id) + '/hqdefault.jpg"><div class="play"><span>▶</span></div></div><figcaption class="small" style="margin-top:8px;font-weight:600">' + esc(v.title) + "</figcaption></figure>";
      return '<figure style="margin:0"><a class="video-ph" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=' + encodeURIComponent(v.q || v.title) + '">▶ ' + esc(v.title) + '</a><figcaption class="small muted" style="margin-top:8px">Episode coming soon — watch related videos on YouTube</figcaption></figure>';
    }).join("");
    vg.addEventListener("click", play); vg.addEventListener("keydown", function (e) { if (e.key === "Enter") play(e); });
    function play(e) {
      var v = e.target.closest("[data-yt]"); if (!v) return;
      v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + v.getAttribute("data-yt") + '?autoplay=1" title="YouTube video" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
    }
  }
  $$("[data-yt-channel]").forEach(function (a) { if (C.youtubeChannel) a.href = C.youtubeChannel; });

  /* ---------- Donation links ---------- */
  var dl = $("#donate-links");
  if (dl) {
    var names = { paypal: "PayPal", stripe: "Card (Stripe)", buymeacoffee: "Buy Me a Coffee", kofi: "Ko-fi", githubSponsors: "GitHub Sponsors" };
    var html = Object.keys(names).filter(function (k) { return (C.donate || {})[k]; }).map(function (k) {
      return '<a class="btn btn-gold" target="_blank" rel="noopener" href="' + esc(C.donate[k]) + '">' + names[k] + "</a>";
    }).join("");
    dl.innerHTML = html || '<p class="small muted">Instant online payment links are being set up. Use the pledge form below — we\'ll reply with secure payment options within 24 hours.</p>';
  }
  $$("[data-amount]").forEach(function (b) {
    b.addEventListener("click", function () {
      var f = $("#pledge-amount"); if (f) { f.value = b.getAttribute("data-amount"); f.focus(); }
      $$("[data-amount]").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
    });
  });
})();
