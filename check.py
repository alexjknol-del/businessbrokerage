# -*- coding: utf-8 -*-
"""Checks the built site: links, anchors, register, duplicates and the sitemap."""
import os, re, sys, html

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
SITE = "https://businessbrokerage.eu"
MAIL = "info@businessbrokerage.eu"
ALLOWED = ("https://www.ibba.org", "https://single-market-economy.ec.europa.eu", "https://www.businessforsale.eu", SITE, "https://www.vanderzwaard.nl/", "https://dlsa.nl/", "https://advocaat-vanwegen.nl")

ADDRESS = r"\b(you|your|yours|we|our|ours|us)\b"
MONEY = r"(€|\$|£|EUR\s?\d|\d+\s?(euro|euros)\b)"

problems = []
pages = {}
for root, dirs, files in os.walk(DIST):
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            pages[p] = open(p, encoding="utf-8").read()

print("%d html files" % len(pages))
titles, metas = {}, {}

for p, raw in pages.items():
    rel = p.replace(DIST, "") or "/"
    text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)

    for m in re.finditer(ADDRESS, text, re.I):
        problems.append("%s: direct address '%s'" % (rel, m.group(0)))
    for m in re.finditer(MONEY, text, re.I):
        problems.append("%s: money reference '%s'" % (rel, m.group(0)))
    if "—" in text or "–" in text:
        problems.append("%s: dash character" % rel)
    for w in ("lorem", "TODO", "XXX", "placeholder"):
        if w.lower() in text.lower():
            problems.append("%s: filler '%s'" % (rel, w))

    t = re.search(r"<title>(.*?)</title>", raw, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', raw, re.S)
    if t:
        titles.setdefault(t.group(1), []).append(rel)
        if len(t.group(1)) > 70:
            problems.append("%s: title %d chars" % (rel, len(t.group(1))))
    else:
        problems.append("%s: no title" % rel)
    if d:
        metas.setdefault(d.group(1), []).append(rel)
        if not (60 <= len(d.group(1)) <= 175):
            problems.append("%s: meta %d chars" % (rel, len(d.group(1))))
    else:
        problems.append("%s: no meta description" % rel)

    for href in re.findall(r'href="([^"]+)"', raw):
        if href.startswith("#"):
            continue
        if href.startswith("/"):
            target = os.path.join(DIST, href.strip("/"), "index.html")
            if href in ("/style.css", "/favicon.svg"):
                target = os.path.join(DIST, href.strip("/"))
            if not os.path.exists(target):
                problems.append("%s: dead internal link %s" % (rel, href))
        elif href.startswith("http"):
            if not href.startswith(ALLOWED):
                problems.append("%s: unknown external host %s" % (rel, href))
        elif href.startswith("mailto:"):
            if href != "mailto:" + MAIL:
                problems.append("%s: unexpected mail address %s" % (rel, href))

    for anchor in re.findall(r'<a href="(https://www\.businessforsale\.eu[^"]*)"[^>]*>(.*?)</a>', raw, re.S):
        url, label = anchor
        clean = html.unescape(re.sub(r"<[^>]+>", "", label)).strip()
        if clean != url:
            problems.append("%s: anchor text is not the full url (%s)" % (rel, clean[:60]))

for t, ps in titles.items():
    if len(ps) > 1:
        problems.append("duplicate title %r on %s" % (t, ps))
for m, ps in metas.items():
    if len(ps) > 1:
        problems.append("duplicate meta on %s" % ps)

sm = open(os.path.join(DIST, "sitemap.xml"), encoding="utf-8").read()
locs = re.findall(r"<loc>(.*?)</loc>", sm)
for l in locs:
    path = l.replace(SITE, "")
    if not os.path.exists(os.path.join(DIST, path.strip("/"), "index.html")):
        problems.append("sitemap points at missing page %s" % l)
print("%d urls in sitemap" % len(locs))

if problems:
    print("\n%d findings:" % len(problems))
    for f in problems[:60]:
        print(" -", f)
    sys.exit(1)
print("no findings")
