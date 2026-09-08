# -*- coding: utf-8 -*-
"""Generator core for businessbrokerage.eu. Reference-book layout."""

import os, html

BASE = "https://businessbrokerage.eu"
NAME = "Business Brokerage Europe"
MAIL = "info@businessbrokerage.eu"

PLATFORM = "https://www.businessforsale.eu"

NAV = [
    ("/handbook/", "Handbook"),
    ("/methods/", "Valuation methods"),
    ("/markets/", "Markets"),
    ("/glossary/", "Glossary"),
]

PAGES = []


def esc(t):
    return html.escape(t, quote=False)


def ext(url, text=None):
    return '<a href="%s" rel="noopener">%s</a>' % (url, text or url)


CSS = r"""
:root{
  --page:#ffffff; --paper:#f7f5f0; --ink:#141c26; --muted:#5b6672;
  --rule:#d8d3c7; --navy:#1d3557; --brick:#8c3b2e; --gold:#b08b3f;
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
 font-family:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
 font-size:17.5px;line-height:1.62}
h1,h2,h3,h4{font-family:inherit;font-weight:600;line-height:1.2;letter-spacing:-.005em}
h1{font-size:clamp(1.9rem,1.4rem + 2vw,2.7rem);margin:.1em 0 .4em}
h2{font-size:1.42rem;margin:2rem 0 .6rem;border-bottom:1px solid var(--rule);padding-bottom:.3rem}
h3{font-size:1.13rem;margin:1.5rem 0 .4rem}
p{margin:0 0 1em}
a{color:var(--brick)}
a:hover{color:#6d2c22}
.wrap{max-width:1180px;margin:0 auto;padding:0 26px}

/* masthead */
.mast{background:var(--navy);color:#f3efe6}
.mast .wrap{display:flex;align-items:baseline;gap:26px;flex-wrap:wrap;padding-top:14px;padding-bottom:14px}
.mast a{color:#f3efe6;text-decoration:none}
.mast .name{font-size:1.28rem;letter-spacing:.02em}
.mast .name span{color:var(--gold)}
.mast nav{margin-left:auto;display:flex;gap:22px;flex-wrap:wrap;font-size:.95rem}
.mast nav a{border-bottom:1px solid transparent;padding-bottom:2px}
.mast nav a:hover,.mast nav a[aria-current]{border-color:var(--gold)}
.strap{background:var(--navy);color:#c9d4e2;border-top:1px solid rgba(255,255,255,.13)}
.strap .wrap{padding:7px 26px;font-size:.82rem;letter-spacing:.06em;text-transform:uppercase}

/* two column reading layout */
.sheet{display:grid;grid-template-columns:230px minmax(0,1fr);gap:46px;margin:34px 0 10px;align-items:start}
@media(max-width:880px){.sheet{grid-template-columns:1fr;gap:18px}}
.rail{position:sticky;top:22px;font-size:.9rem;border-right:1px solid var(--rule);padding-right:18px}
@media(max-width:880px){.rail{position:static;border-right:0;border-bottom:1px solid var(--rule);padding:0 0 14px}}
.rail b{display:block;font-size:.76rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}
.rail ol{list-style:none;margin:0;padding:0;counter-reset:c}
.rail li{margin:0 0 6px;counter-increment:c}
.rail li a{text-decoration:none;color:var(--ink)}
.rail li a:before{content:counter(c,decimal-leading-zero) "  ";color:var(--gold);font-variant-numeric:tabular-nums}
.rail li a:hover{color:var(--brick)}
.rail li a[aria-current]{color:var(--brick);font-weight:600}

.col{background:var(--page);border:1px solid var(--rule);padding:34px 40px 40px;box-shadow:0 1px 0 rgba(20,28,38,.04)}
@media(max-width:620px){.col{padding:22px 20px 26px}}
.chapno{font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.lede{font-size:1.12rem;color:#39424e}
.rule{border:0;border-top:1px solid var(--rule);margin:30px 0}

/* figures */
figure.fig{margin:24px 0;border:1px solid var(--rule);background:var(--paper);padding:18px}
figure.fig svg{display:block;width:100%;max-width:560px;height:auto;margin:0 auto}
figure.fig figcaption{font-size:.85rem;color:var(--muted);margin-top:10px;border-top:1px solid var(--rule);padding-top:8px}

/* marginal note */
.note{border-left:3px solid var(--gold);padding:2px 0 2px 16px;margin:22px 0;color:#39424e}
.note b{display:block;font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}

/* definition list */
dl.defs{margin:18px 0}
dl.defs dt{font-weight:600;margin-top:14px}
dl.defs dd{margin:2px 0 0;color:#39424e}

table{border-collapse:collapse;width:100%;margin:18px 0;font-size:.95rem}
th,td{border-bottom:1px solid var(--rule);padding:9px 10px;text-align:left;vertical-align:top}
th{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);border-bottom:2px solid var(--rule)}
.tablewrap{overflow-x:auto}

ul,ol{margin:0 0 1.05em;padding-left:1.2em}
li{margin:0 0 .4em}

/* index grid */
.index{list-style:none;margin:22px 0;padding:0;counter-reset:x}
.index li{counter-increment:x;border-top:1px solid var(--rule);padding:14px 0;display:grid;grid-template-columns:46px 1fr;gap:16px}
.index li:last-child{border-bottom:1px solid var(--rule)}
.index .n{color:var(--gold);font-variant-numeric:tabular-nums}
.index a{text-decoration:none;font-weight:600;color:var(--navy)}
.index a:hover{color:var(--brick)}
.index p{margin:.2em 0 0;font-size:.95rem;color:#4a545f}

.cta{background:var(--navy);color:#eef2f7;padding:22px 26px;margin:30px 0}
.cta h2{border:0;color:#fff;margin:0 0 .4rem;font-size:1.2rem}
.cta a{color:#f0c675}

.foot{background:#111923;color:#aebbc9;margin-top:52px;padding:30px 0 40px;font-size:.9rem}
.foot a{color:#dfe6ee;text-decoration:none}
.foot a:hover{color:#f0c675}
.foot .cols{display:grid;grid-template-columns:2fr 1fr 1fr;gap:26px}
@media(max-width:760px){.foot .cols{grid-template-columns:1fr}}
.foot h4{margin:0 0 .5rem;color:#fff;font-size:.98rem}
.foot ul{list-style:none;margin:0;padding:0}
.foot li{margin:0 0 5px}
.foot .end{margin-top:24px;padding-top:14px;border-top:1px solid #26303c;font-size:.82rem}
"""


def page(path, title, meta, body, prio="0.6", rail=None, breadcrumb=None):
    nav = "".join('<a href="%s"%s>%s</a>' % (u, ' aria-current="page"' if path.startswith(u) else "", esc(n))
                  for u, n in NAV)
    railhtml = ""
    if rail:
        label, items, current = rail
        lis = "".join('<li><a href="%s"%s>%s</a></li>' % (u, ' aria-current="true"' if u == current else "", esc(t))
                      for u, t in items)
        railhtml = '<aside class="rail"><b>%s</b><ol>%s</ol></aside>' % (esc(label), lis)
    else:
        railhtml = '<aside class="rail"><b>Sections</b><ol>%s</ol></aside>' % "".join(
            '<li><a href="%s">%s</a></li>' % (u, esc(n)) for u, n in NAV)
    doc = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(meta)s">
<link rel="canonical" href="%(canon)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(meta)s">
<meta property="og:type" content="article">
<meta property="og:url" content="%(canon)s">
<meta property="og:site_name" content="%(name)s">
<meta name="theme-color" content="#1d3557">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="mast"><div class="wrap">
<a class="name" href="/">Business <span>Brokerage</span> Europe</a>
<nav>%(nav)s</nav>
</div></header>
<div class="strap"><div class="wrap">A reference on how online business sales are handled in Europe</div></div>
<div class="wrap"><div class="sheet">
%(rail)s
<main class="col">
%(body)s
</main>
</div></div>
<footer class="foot"><div class="wrap">
<div class="cols">
<div><h4>Business Brokerage Europe</h4>
<p>A reference work on the practice of brokering online businesses: mandates, valuation methods, deal structures and the steps between a first conversation and a signed transfer.</p></div>
<div><h4>Sections</h4><ul>
<li><a href="/handbook/">The handbook</a></li>
<li><a href="/methods/">Valuation methods</a></li>
<li><a href="/markets/">European markets</a></li>
<li><a href="/glossary/">Glossary</a></li>
</ul></div>
<div><h4>This site</h4><ul>
<li><a href="/about/">About</a></li>
<li><a href="/contact/">Contact</a></li>
<li><a href="/privacy/">Privacy statement</a></li>
<li><a href="/cookies/">Cookie statement</a></li>
</ul></div>
</div>
<div class="end">2026 &middot; businessbrokerage.eu</div>
</div></footer>
</body>
</html>
""" % dict(title=esc(title), meta=esc(meta), canon=BASE + path, name=NAME, nav=nav, rail=railhtml, body=body)
    PAGES.append((path, title, meta, doc, prio))
    return doc


def write(dist):
    for path, t, m, doc, prio in PAGES:
        d = os.path.join(dist, path.strip("/"))
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(doc)
    urls = "".join('<url><loc>%s%s</loc><priority>%s</priority></url>\n' % (BASE, p, pr)
                   for p, t, m, d, pr in PAGES if p != "/404/")
    open(os.path.join(dist, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    open(os.path.join(dist, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE)
    open(os.path.join(dist, "style.css"), "w", encoding="utf-8").write(CSS)
