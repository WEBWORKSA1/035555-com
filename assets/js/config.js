/* ============================================================
   035555.com — SITE CONFIG (edit this file only to go live)
   ============================================================ */
window.SITE_CONFIG = {
  siteName: "035555.com",
  inquiryUrl: "https://web.works/contact",

  /* FORMS — all submissions are delivered via FormSubmit.co (free).
     The destination inbox is never printed on the page. After the first
     submission, FormSubmit emails an activation link to the owner inbox.
     Once activated, FormSubmit also shows a random alias string —
     paste it into formAlias below so the inbox is no longer derivable at all. */
  formAlias: "",            // e.g. "a1b2c3d4e5f6..." from FormSubmit dashboard
  _k: ["bW9jLmxp", "YW1nQDFh", "c2tyb3di", "ZXc="],

  /* MONETIZATION */
  adsenseClient: "",        // e.g. "ca-pub-1234567890123456" (also update /ads.txt)
  adsenseSlots: { top: "", inContent: "", sidebar: "", footer: "" },
  ga4Id: "",                // e.g. "G-XXXXXXX"

  /* DONATIONS — paste hosted payment links (no email needed in links). */
  donate: {
    paypal: "",             // PayPal hosted donate button link
    stripe: "",             // Stripe Payment Link
    buymeacoffee: "",       // https://buymeacoffee.com/yourname
    kofi: "",               // https://ko-fi.com/yourname
    githubSponsors: ""      // https://github.com/sponsors/yourname
  },

  /* YOUTUBE — add video IDs (the part after v=) to show embeds. */
  youtubeChannel: "",       // e.g. "https://www.youtube.com/@yourchannel"
  videos: [
    { id: "", title: "What does 035555 mean? Reading a number like a native speaker", q: "chinese number meanings explained" },
    { id: "", title: "520, 1314, 5201314 — Chinese love codes decoded", q: "520 1314 chinese number love meaning" },
    { id: "", title: "Why 8 is lucky and 4 is avoided", q: "why 8 lucky 4 unlucky china" },
    { id: "", title: "555 and 666 — crying vs. awesome in Chinese chat", q: "555 666 chinese internet slang" },
    { id: "", title: "How lucky phone numbers are priced", q: "lucky phone number china price" },
    { id: "", title: "Numeric domain names and why China buys them", q: "chinese numeric domain names" }
  ]
};
