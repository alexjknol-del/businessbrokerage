# -*- coding: utf-8 -*-
"""Schematic line drawings for businessbrokerage.eu. Navy line art, no fills."""

N = "#1d3557"   # navy
G = "#b08b3f"   # gold
B = "#8c3b2e"   # brick
M = "#5b6672"


def _svg(vb, body):
    return '<svg viewBox="%s" xmlns="http://www.w3.org/2000/svg" role="img">%s</svg>' % (vb, body)


def _t(x, y, s, anchor="middle", size=12, fill=N):
    return ('<text x="%s" y="%s" text-anchor="%s" font-size="%s" fill="%s" '
            'font-family="Georgia,serif">%s</text>' % (x, y, anchor, size, fill, s))


def process_line():
    steps = ["Mandate", "Preparation", "Market", "Talks", "Offer", "Due diligence", "Transfer"]
    b = ''
    x = 40
    for i, s in enumerate(steps):
        b += f'<circle cx="{x}" cy="70" r="9" fill="none" stroke="{N}" stroke-width="2"/>'
        b += f'<circle cx="{x}" cy="70" r="3" fill="{G}"/>'
        b += _t(x, 100, s, size=11)
        if i < len(steps) - 1:
            b += f'<line x1="{x+11}" y1="70" x2="{x+69}" y2="70" stroke="{N}" stroke-width="1.5"/>'
        x += 80
    return _svg("0 0 620 130", b)


def mandate():
    b = f'''
<rect x="30" y="40" width="160" height="80" fill="none" stroke="{N}" stroke-width="2"/>
{_t(110, 70, "Seller")}{_t(110, 92, "owner of the business", size=10, fill=M)}
<rect x="230" y="40" width="160" height="80" fill="none" stroke="{N}" stroke-width="2"/>
{_t(310, 70, "Broker")}{_t(310, 92, "mandated adviser", size=10, fill=M)}
<rect x="430" y="40" width="160" height="80" fill="none" stroke="{N}" stroke-width="2"/>
{_t(510, 70, "Buyers")}{_t(510, 92, "screened candidates", size=10, fill=M)}
<line x1="190" y1="80" x2="230" y2="80" stroke="{G}" stroke-width="2"/>
<polygon points="230,80 222,76 222,84" fill="{G}"/>
<line x1="390" y1="80" x2="430" y2="80" stroke="{G}" stroke-width="2"/>
<polygon points="430,80 422,76 422,84" fill="{G}"/>
{_t(210, 34, "mandate", size=10, fill=M)}{_t(410, 34, "outreach", size=10, fill=M)}
<path d="M510 128 C 510 160, 110 160, 110 128" fill="none" stroke="{B}" stroke-width="1.5" stroke-dasharray="5 4"/>
{_t(310, 158, "offers and questions travel back through the broker", size=10, fill=M)}
'''
    return _svg("0 0 620 175", b)


def funnel():
    rows = [("Long list", 560), ("Approached", 440), ("Signed an NDA", 320), ("Serious talks", 200), ("Offers", 110), ("Deal", 60)]
    b = ''
    y = 20
    for label, w in rows:
        x = (620 - w) / 2
        b += f'<rect x="{x}" y="{y}" width="{w}" height="26" fill="none" stroke="{N}" stroke-width="1.6"/>'
        b += _t(310, y + 18, label, size=11)
        y += 34
    return _svg("0 0 620 230", b)


def asset_vs_share():
    b = f'''
<rect x="24" y="34" width="270" height="150" fill="none" stroke="{N}" stroke-width="2"/>
{_t(159, 56, "Asset transaction", size=13)}
<line x1="44" y1="68" x2="274" y2="68" stroke="{M}" stroke-width="1"/>
{_t(159, 92, "selected assets move", size=11, fill=M)}
{_t(159, 112, "domain, stock, contracts, data", size=11, fill=M)}
{_t(159, 140, "the legal entity stays behind", size=11, fill=B)}
<rect x="326" y="34" width="270" height="150" fill="none" stroke="{N}" stroke-width="2"/>
{_t(461, 56, "Share transaction", size=13)}
<line x1="346" y1="68" x2="576" y2="68" stroke="{M}" stroke-width="1"/>
{_t(461, 92, "the entity itself changes hands", size=11, fill=M)}
{_t(461, 112, "with its history and obligations", size=11, fill=M)}
{_t(461, 140, "contracts usually stay in place", size=11, fill=B)}
'''
    return _svg("0 0 620 200", b)


def bridge():
    bars = [("Enterprise value", 150), ("minus debt", 40), ("plus cash", 25), ("working capital", 30), ("Equity price", 105)]
    b = ''
    x = 40
    base = 170
    for i, (label, h) in enumerate(bars):
        col = G if i in (0, len(bars) - 1) else N
        b += f'<rect x="{x}" y="{base-h}" width="70" height="{h}" fill="none" stroke="{col}" stroke-width="2"/>'
        b += _t(x + 35, 190, label, size=10, fill=M)
        x += 110
    b += f'<line x1="30" y1="{base}" x2="590" y2="{base}" stroke="{N}" stroke-width="1.5"/>'
    return _svg("0 0 620 205", b)


def timeline():
    weeks = [("Week 0", "mandate signed"), ("Week 2", "memorandum ready"), ("Week 4", "market approached"),
             ("Week 8", "first meetings"), ("Week 12", "offer accepted"), ("Week 18", "due diligence done"),
             ("Week 22", "transfer")]
    b = f'<line x1="40" y1="46" x2="580" y2="46" stroke="{N}" stroke-width="1.5"/>'
    x = 40
    for wk, what in weeks:
        b += f'<line x1="{x}" y1="38" x2="{x}" y2="54" stroke="{G}" stroke-width="2"/>'
        b += _t(x, 30, wk, size=10)
        b += _t(x, 72, what, size=10, fill=M)
        x += 90
    return _svg("0 0 620 90", b)


def dataroom():
    folders = ["Corporate", "Financial", "Commercial", "Legal", "Technical", "People"]
    b = ''
    x, y = 40, 30
    for i, f in enumerate(folders):
        b += f'<path d="M{x} {y+16} h34 l8 -10 h58 v76 h-100 z" fill="none" stroke="{N}" stroke-width="1.8"/>'
        b += _t(x + 50, y + 60, f, size=11)
        x += 190
        if i % 3 == 2:
            x = 40
            y += 100
    return _svg("0 0 620 235", b)


def earnout():
    b = f'''
<line x1="50" y1="170" x2="590" y2="170" stroke="{N}" stroke-width="1.5"/>
<line x1="50" y1="20" x2="50" y2="170" stroke="{N}" stroke-width="1.5"/>
<rect x="80" y="70" width="120" height="100" fill="none" stroke="{G}" stroke-width="2"/>
{_t(140, 60, "at closing", size=10, fill=M)}
<rect x="240" y="120" width="120" height="50" fill="none" stroke="{N}" stroke-width="2"/>
{_t(300, 110, "year one", size=10, fill=M)}
<rect x="400" y="130" width="120" height="40" fill="none" stroke="{N}" stroke-width="2"/>
{_t(460, 120, "year two", size=10, fill=M)}
{_t(320, 195, "the part after closing depends on agreed results", size=11, fill=M)}
'''
    return _svg("0 0 620 210", b)


def map_europe():
    pts = [("NL", 300, 70), ("BE", 285, 92), ("DE", 350, 82), ("FR", 265, 120), ("ES", 210, 175),
           ("IT", 355, 155), ("PL", 415, 70), ("SE", 375, 22)]
    b = f'<rect x="20" y="10" width="580" height="200" fill="none" stroke="{M}" stroke-width="1" stroke-dasharray="4 5"/>'
    for code, x, y in pts:
        b += f'<circle cx="{x}" cy="{y}" r="16" fill="none" stroke="{N}" stroke-width="1.8"/>'
        b += _t(x, y + 4, code, size=11)
    b += _t(310, 202, "markets covered in this section", size=10, fill=M)
    return _svg("0 0 620 220", b)


def multiples():
    b = f'<line x1="60" y1="160" x2="580" y2="160" stroke="{N}" stroke-width="1.5"/>'
    b += f'<line x1="60" y1="20" x2="60" y2="160" stroke="{N}" stroke-width="1.5"/>'
    pts = [(110, 130), (180, 120), (250, 100), (320, 92), (390, 74), (460, 66), (530, 50)]
    d = " ".join(("M%d %d" % p) if i == 0 else ("L%d %d" % p) for i, p in enumerate(pts))
    b += f'<path d="{d}" fill="none" stroke="{G}" stroke-width="2.5"/>'
    for x, y in pts:
        b += f'<circle cx="{x}" cy="{y}" r="4" fill="{N}"/>'
    b += _t(320, 182, "larger and steadier earnings sit at higher multiples", size=11, fill=M)
    b += _t(40, 90, "multiple", size=10, fill=M, anchor="middle")
    return _svg("0 0 620 195", b)


def escrow():
    b = f'''
<rect x="50" y="50" width="140" height="70" fill="none" stroke="{N}" stroke-width="2"/>{_t(120, 90, "Buyer")}
<rect x="430" y="50" width="140" height="70" fill="none" stroke="{N}" stroke-width="2"/>{_t(500, 90, "Seller")}
<rect x="240" y="35" width="140" height="100" fill="none" stroke="{G}" stroke-width="2"/>
{_t(310, 70, "Escrow", size=13)}{_t(310, 92, "third party holds", size=10, fill=M)}{_t(310, 110, "funds until conditions", size=10, fill=M)}
<line x1="190" y1="85" x2="240" y2="85" stroke="{N}" stroke-width="2"/><polygon points="240,85 232,81 232,89" fill="{N}"/>
<line x1="380" y1="85" x2="430" y2="85" stroke="{N}" stroke-width="2"/><polygon points="430,85 422,81 422,89" fill="{N}"/>
'''
    return _svg("0 0 620 155", b)


def handover():
    rows = ["Accounts and logins", "Supplier contracts", "Advertising accounts", "Customer data", "Stock and returns", "Introductions"]
    b = ''
    y = 26
    for r in rows:
        b += f'<rect x="60" y="{y}" width="16" height="16" fill="none" stroke="{N}" stroke-width="1.8"/>'
        b += f'<path d="M63 {y+8} l4 5 l8 -10" fill="none" stroke="{G}" stroke-width="2"/>'
        b += _t(92, y + 13, r, anchor="start", size=12)
        y += 30
    return _svg("0 0 620 200", b)


FIGS = {
    "process": process_line, "mandate": mandate, "funnel": funnel, "asset": asset_vs_share,
    "bridge": bridge, "timeline": timeline, "dataroom": dataroom, "earnout": earnout,
    "map": map_europe, "multiples": multiples, "escrow": escrow, "handover": handover,
}


def fig(name, caption=""):
    f = FIGS.get(name)
    if not f:
        return ""
    cap = '<figcaption>%s</figcaption>' % caption if caption else ""
    return '<figure class="fig">%s%s</figure>' % (f(), cap)
