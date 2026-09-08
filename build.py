# -*- coding: utf-8 -*-
"""Builds businessbrokerage.eu into dist/."""
import os, shutil
import core, art
from core import page, PLATFORM, esc
from content_handbook import CHAPTERS
from content_methods import METHODS
from content_markets import MARKETS
from content_glossary import TERMS

HANDBOOK_RAIL = ("Handbook", [("/handbook/%s/" % c["slug"], c["title"].split(":")[0]) for c in CHAPTERS], None)
METHOD_RAIL = ("Methods", [("/methods/%s/" % m["slug"], m["title"]) for m in METHODS], None)
MARKET_RAIL = ("Markets", [("/markets/%s/" % m["slug"], m["name"]) for m in MARKETS], None)


def plink(text, path):
    url = PLATFORM + path
    return '%s (<a href="%s" rel="noopener">%s</a>)' % (text, url, url)


def sections_html(sections):
    out = []
    for head, blocks in sections:
        out.append("<h2>%s</h2>" % esc(head))
        for b in blocks:
            out.append(b if b.strip().startswith("<") else "<p>%s</p>" % b)
    return "".join(out)


def links_block(links):
    if not links:
        return ""
    items = "".join("<li>%s</li>" % plink(t, p) for t, p in links)
    return '<div class="note"><b>Further reading on the platform</b><ul>%s</ul></div>' % items


def home():
    idx = "".join(
        '<li><span class="n">%02d</span><div><a href="/handbook/%s/">%s</a><p>%s</p></div></li>'
        % (i + 1, c["slug"], esc(c["title"]), esc(c["lede"])) for i, c in enumerate(CHAPTERS))
    body = f"""
<p class="chapno">A reference for sellers, buyers and advisers</p>
<h1>How online businesses change hands in Europe</h1>
<p class="lede">This site sets out the practice of business brokerage as it is applied to online companies: the mandate, the preparation, the search for candidates, the negotiation and the transfer. It is written as a reference rather than as a sales document.</p>
{art.fig("process", "The seven stages of a mandated sale process. Most of the elapsed time sits in preparation and in the investigation phase.")}
<h2>The handbook</h2>
<p>Twelve chapters, in the order a transaction actually runs.</p>
<ul class="index">{idx}</ul>
<h2>Three other sections</h2>
<dl class="defs">
<dt><a href="/methods/">Valuation methods</a></dt><dd>Five approaches, what each measures and where each stops being useful.</dd>
<dt><a href="/markets/">European markets</a></dt><dd>Country notes on channels, structures and buyer profiles across eight markets.</dd>
<dt><a href="/glossary/">Glossary</a></dt><dd>Forty-six terms that appear in transaction documents, defined in plain language.</dd>
</dl>
<div class="cta">
<h2>Where transactions are published</h2>
<p>Listings of European online businesses offered for sale, and the buyers currently searching, are published on {plink("the marketplace operated by Businessforsale.eu", "/online-business-for-sale")}.</p>
</div>
"""
    page("/", "Business brokerage in Europe: a working reference",
         "A reference on brokering online businesses in Europe: mandates, preparation, valuation methods, negotiation, due diligence and transfer, in twelve chapters.",
         body, "1.0")


def handbook():
    idx = "".join(
        '<li><span class="n">%02d</span><div><a href="/handbook/%s/">%s</a><p>%s</p></div></li>'
        % (i + 1, c["slug"], esc(c["title"]), esc(c["lede"])) for i, c in enumerate(CHAPTERS))
    body = f"""
<p class="chapno">Section one</p>
<h1>The handbook</h1>
<p class="lede">Twelve chapters covering a mandated sale from the engagement letter to the last item on the handover list. Each chapter stands on its own, and the order follows the sequence of a real process.</p>
{art.fig("timeline", "An indicative schedule. Individual processes run faster or slower, but the order of the steps rarely changes.")}
<ul class="index">{idx}</ul>
"""
    page("/handbook/", "The brokerage handbook: twelve chapters",
         "Twelve chapters on brokering the sale of an online business, from the mandate and preparation through negotiation and due diligence to the handover.",
         body, "0.9", rail=HANDBOOK_RAIL)

    for i, c in enumerate(CHAPTERS):
        figure = art.fig(*c["fig"]) if c.get("fig") else ""
        prev_next = []
        if i > 0:
            prev_next.append('<a href="/handbook/%s/">Previous chapter</a>' % CHAPTERS[i - 1]["slug"])
        if i < len(CHAPTERS) - 1:
            prev_next.append('<a href="/handbook/%s/">Next chapter</a>' % CHAPTERS[i + 1]["slug"])
        body = f"""
<p class="chapno">Chapter {i+1:02d}</p>
<h1>{c["title"]}</h1>
<p class="lede">{c["lede"]}</p>
{figure}
{sections_html(c["sections"])}
{links_block(c.get("links"))}
<hr class="rule">
<p>{' &middot; '.join(prev_next)} &middot; <a href="/handbook/">All chapters</a></p>
"""
        rail = ("Handbook", HANDBOOK_RAIL[1], "/handbook/%s/" % c["slug"])
        page("/handbook/%s/" % c["slug"], c["title"], c["meta"], body, "0.7", rail=rail)


def methods():
    idx = "".join(
        '<li><span class="n">%02d</span><div><a href="/methods/%s/">%s</a><p>%s</p></div></li>'
        % (i + 1, m["slug"], esc(m["title"]), esc(m["lede"])) for i, m in enumerate(METHODS))
    body = f"""
<p class="chapno">Section two</p>
<h1>Valuation methods</h1>
<p class="lede">No single method settles what a business is worth. Each measures something different, and a defensible valuation usually applies two and explains the gap between them.</p>
{art.fig("multiples", "Where a business sits within the observed range matters more than the method used to place it there.")}
<ul class="index">{idx}</ul>
<div class="note"><b>In practice</b><p>A valuation prepared for a transaction is a range with reasoning attached, not a certificate. {plink("A structured valuation of an online business", "/services/business-valuation")} is one of the services offered by the platform behind this reference.</p></div>
"""
    page("/methods/", "Valuation methods for online businesses",
         "Five valuation methods for online businesses: earnings multiples, discounted cash flow, discretionary earnings, asset based valuation and comparable transactions.",
         body, "0.9", rail=METHOD_RAIL)
    for m in METHODS:
        figure = art.fig(*m["fig"]) if m.get("fig") else ""
        body = f"""
<p class="chapno">Valuation method</p>
<h1>{m["title"]}</h1>
<p class="lede">{m["lede"]}</p>
{figure}
{sections_html(m["sections"])}
{links_block(m.get("links"))}
<hr class="rule">
<p><a href="/methods/">All valuation methods</a></p>
"""
        rail = ("Methods", METHOD_RAIL[1], "/methods/%s/" % m["slug"])
        page("/methods/%s/" % m["slug"], m["title"], m["meta"], body, "0.7", rail=rail)


def markets():
    rows = "".join('<li><span class="n">%02d</span><div><a href="/markets/%s/">%s</a><p>%s</p></div></li>'
                   % (i + 1, m["slug"], esc(m["name"]), esc(m["lede"])) for i, m in enumerate(MARKETS))
    body = f"""
<p class="chapno">Section three</p>
<h1>European markets</h1>
<p class="lede">Eight notes on how online business transactions run in different parts of Europe. The differences that matter are rarely legal; they sit in channel mix, buyer depth and the expectations placed on documentation.</p>
{art.fig("map", "The markets covered in this section.")}
<ul class="index">{rows}</ul>
"""
    page("/markets/", "Selling an online business across European markets",
         "Country notes on selling online businesses in eight European markets: channels, transaction structures, buyer profiles and practical points per country.",
         body, "0.9", rail=MARKET_RAIL)
    for m in MARKETS:
        pts = "".join("<h2>%s</h2><p>%s</p>" % (esc(h), t) for h, t in m["points"])
        others = "".join('<li><a href="/markets/%s/">%s</a></li>' % (o["slug"], esc(o["name"]))
                         for o in MARKETS if o["slug"] != m["slug"])
        body = f"""
<p class="chapno">Market note</p>
<h1>Selling an online business in {esc(m["name"])}</h1>
<p class="lede">{m["lede"]}</p>
{pts}
<div class="note"><b>Listings</b><p>Businesses currently offered across Europe are published at {plink("the European marketplace", "/online-business-for-sale")}.</p></div>
<hr class="rule">
<h2>Other markets</h2>
<ul>{others}</ul>
"""
        rail = ("Markets", MARKET_RAIL[1], "/markets/%s/" % m["slug"])
        page("/markets/%s/" % m["slug"], "Selling an online business in %s" % m["name"], m["meta"], body, "0.6", rail=rail)


def glossary():
    letters = sorted({t[0][0].upper() for t in TERMS})
    nav = " ".join('<a href="#%s">%s</a>' % (l, l) for l in letters)
    out = []
    current = None
    for term, desc in sorted(TERMS, key=lambda x: x[0].lower()):
        first = term[0].upper()
        if first != current:
            if current:
                out.append("</dl>")
            out.append('<h2 id="%s">%s</h2><dl class="defs">' % (first, first))
            current = first
        out.append("<dt>%s</dt><dd>%s</dd>" % (esc(term), esc(desc)))
    out.append("</dl>")
    body = f"""
<p class="chapno">Section four</p>
<h1>Glossary</h1>
<p class="lede">Forty-six terms that appear in mandates, memoranda and purchase agreements, defined as they are used in transactions involving online businesses.</p>
<p>{nav}</p>
{''.join(out)}
"""
    page("/glossary/", "Glossary of business brokerage terms",
         "Forty-six terms from business brokerage defined in plain language, from add-back and earn-out to locked box, participation exemption and working capital adjustment.",
         body, "0.8")


def statics():
    body = f"""
<h1>About this reference</h1>
<p class="lede">Business Brokerage Europe collects, in one place, the working practice behind the sale of an online business: what is agreed at the start, what is prepared, how candidates are found and what happens between an accepted offer and a completed transfer.</p>
<h2>Why it exists</h2>
<p>Most material on this subject is written either for large corporate transactions or as marketing for a single adviser. Neither is much use to the owner of a webshop turning over a few hundred thousand a year, or to the buyer looking at one. This reference sits in between: specific enough to be usable, general enough to apply across European markets.</p>
<h2>How it is organised</h2>
<p>Four sections. The <a href="/handbook/">handbook</a> follows a transaction from mandate to handover. The <a href="/methods/">methods</a> section explains how value is calculated. The <a href="/markets/">market notes</a> describe how practice differs by country. The <a href="/glossary/">glossary</a> defines the vocabulary.</p>
<h2>Where the transactions happen</h2>
<p>Listings, buyer registrations and the services described here are handled by {plink("Businessforsale.eu, a European marketplace for online companies", "/")}. Its knowledge base carries detailed articles on individual subjects, and several chapters here point to it.</p>
<h2>Accuracy</h2>
<p>Tax treatment, employment rules and platform policies differ per country and change over time. Nothing here replaces advice on a specific transaction. Corrections are welcome by e-mail.</p>
"""
    page("/about/", "About Business Brokerage Europe", "What this reference on business brokerage covers, how it is organised and where the underlying transactions take place.", body, "0.4")

    body = """
<h1>Contact</h1>
<p class="lede">This reference is maintained by e-mail. Corrections, additions and questions about a chapter are welcome.</p>
<p>E-mail: <a href="mailto:info@businessbrokerage.eu">info@businessbrokerage.eu</a></p>
<h2>What this site does not do</h2>
<p>No businesses are listed, valued or brokered here. The site describes practice; it does not take mandates and does not act for buyers or sellers.</p>
<h2>Corrections</h2>
<p>Where a chapter no longer matches practice in a particular country, a short note with the relevant detail is enough for the page to be updated.</p>
"""
    page("/contact/", "Contact", "How to reach the editors of this reference on business brokerage, and what the site does and does not do.", body, "0.3")

    body = """
<h1>Privacy statement</h1>
<p>This site is informational. It has no accounts, no shop and no forms, and it does not collect personal data through the pages themselves.</p>
<h2>Server logs</h2>
<p>The hosting provider keeps technical logs, including IP addresses, to detect faults and abuse. Those logs are not used to build profiles of visitors and are not shared for any other purpose.</p>
<h2>E-mail</h2>
<p>A message sent to the address on the contact page contains an e-mail address and whatever the sender chooses to include. It is used to reply and for nothing else, and it is not passed on to third parties.</p>
<h2>Links to other sites</h2>
<p>Several pages link to other websites. Once a visitor follows such a link, the privacy terms of that site apply.</p>
<h2>Requests</h2>
<p>A request to see or delete correspondence can be sent to the address on the contact page.</p>
"""
    page("/privacy/", "Privacy statement", "How this site handles visitor data: server logs, e-mail correspondence and links to other websites.", body, "0.2")

    body = """
<h1>Cookie statement</h1>
<p>This site sets no cookies of its own. There is no analytics package, no advertising network and no tracking script on any page.</p>
<h2>What that means in practice</h2>
<p>Nothing is stored in the browser between visits, and no consent banner is needed because there is nothing to consent to.</p>
<h2>Other sites</h2>
<p>Cookies set by other websites can be removed through the browser settings, under privacy and security in Chrome, Firefox, Safari and Edge.</p>
"""
    page("/cookies/", "Cookie statement", "This site sets no cookies, uses no analytics and carries no advertising scripts. What that means for visitors.", body, "0.2")


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44">
<rect width="44" height="44" rx="6" fill="#1d3557"/>
<path d="M11 30h22M11 24h22M11 18h22" stroke="#b08b3f" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="22" cy="12" r="3.4" fill="#f3efe6"/></svg>"""


def notfound(dist):
    body = """
<h1>This page does not exist</h1>
<p class="lede">The address is either out of date or was copied incorrectly.</p>
<ul>
<li><a href="/handbook/">The handbook, twelve chapters</a></li>
<li><a href="/methods/">Valuation methods</a></li>
<li><a href="/markets/">European market notes</a></li>
<li><a href="/glossary/">Glossary</a></li>
</ul>
"""
    html = page("/404/", "Page not found", "The requested page does not exist. The handbook, the valuation methods, the market notes and the glossary are listed here.", body, "0.1")
    open(os.path.join(dist, "404.html"), "w", encoding="utf-8").write(html)


def main():
    dist = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
    if os.path.isdir(dist):
        shutil.rmtree(dist)
    os.makedirs(dist)
    home(); handbook(); methods(); markets(); glossary(); statics()
    core.write(dist)
    notfound(dist)
    open(os.path.join(dist, "favicon.svg"), "w", encoding="utf-8").write(FAVICON)
    print("%d pages built" % len(core.PAGES))


if __name__ == "__main__":
    main()
