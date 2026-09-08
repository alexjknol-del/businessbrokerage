# -*- coding: utf-8 -*-
"""Twelve handbook chapters. Third person throughout, no direct address."""

CHAPTERS = [
 dict(slug="mandate", title="The mandate: what a broker is engaged to do",
  meta="What a brokerage mandate covers, how exclusivity and duration are agreed, and where the responsibility of the adviser ends and that of the owner begins.",
  fig=("mandate", "The broker sits between the seller and a screened group of candidates, and keeps the traffic in both directions organised."),
  lede="A mandate is the agreement that turns an adviser into a representative. It sets out what will be done, in whose name, for how long, and under which restrictions.",
  sections=[
   ("What the document settles", [
    "A mandate answers four questions before any buyer is approached. Which entity or which set of assets is being offered. Whether the broker acts exclusively or alongside others. How long the engagement runs and how it ends. And what the adviser is allowed to disclose without asking again.",
    "Most disputes later in a process trace back to one of those four points being left vague. An owner who assumed the mandate covered only one country, or a broker who assumed a competitor could be approached, will discover the gap at the worst possible moment."]),
   ("Exclusive or open", [
    "An exclusive mandate gives one adviser the right to bring the business to market for a set period. In return the adviser invests in preparation: reworking figures, writing the memorandum, building a list of candidates.",
    "An open mandate spreads the work across several parties. It looks like a wider net, but in practice it often narrows the result. The same business appearing through three channels signals to buyers that nobody is in charge, and it makes confidentiality almost impossible to hold."]),
   ("Duration and tail", [
    "A typical term runs long enough to complete a full cycle: preparation, outreach, talks, an offer, an investigation and a transfer. Six to nine months is common for an online business, longer for anything with staff, warehousing or complex supplier agreements.",
    "Most mandates include a tail clause. If a buyer who was introduced during the mandate returns after it has ended, the adviser is still entitled to the agreed remuneration. The clause is standard practice and it protects both sides from an artificial pause in the talks."]),
   ("Where responsibility sits", [
    "A broker organises the process, prepares the documentation and manages the flow of information. The owner remains responsible for the accuracy of what is handed over. No adviser can warrant figures they did not produce.",
    "That division matters during due diligence. Questions about a supplier contract or a customer database go back to the owner. The adviser makes sure they arrive in a form the buyer can work with, and that the answer is given once rather than four times."]),
   ("Signals of a workable mandate", [
    "<ul><li>The scope names the entity, the assets and the countries involved</li><li>The remuneration model is written out in full, including what happens if the process stops</li><li>There is a defined list of parties who may not be approached without consent</li><li>Reporting is agreed: how often, in what form and with how much detail</li><li>Termination is possible on notice, in writing, without a dispute over who owns the buyer list</li></ul>"]),
  ],
  links=[("The platform where mandated listings are published", "/online-business-for-sale"),
         ("How a sale process is organised from first contact onwards", "/services/how-to")]),

 dict(slug="preparation", title="Preparing a business for the market",
  meta="The work that happens before a business is offered: cleaning up figures, separating private from company matters, and removing the dependencies that scare buyers off.",
  fig=("dataroom", "Preparation is largely a filing exercise. Six folders cover almost everything a buyer will ask for."),
  lede="Preparation decides how a business is received. Two companies with identical results can land very differently depending on how the story and the paperwork have been organised.",
  sections=[
   ("Normalising the figures", [
    "Owner-managed companies carry costs that a buyer will not inherit: a car that serves both purposes, a salary set for tax reasons rather than market reasons, one-off legal work, a family member on the payroll. Normalisation strips those out and shows what the business earns under ordinary management.",
    "The adjustment has to be defensible. Every correction needs a line in the accounts behind it, because the buyer's adviser will test each one. Corrections that cannot be evidenced are usually the first thing to be reversed during due diligence, and reversals late in a process cost more than an honest starting point."]),
   ("Separating private from company", [
    "A domain registered in a personal name, an advertising account run from a private login, stock held in a garage, a supplier agreement on a handshake. Each of these is small on its own and each of them is an obstacle at transfer.",
    "The fix is administrative rather than clever: register what belongs to the company in the name of the company, move accounts to company addresses, and put verbal arrangements on paper with the counterparty before a buyer asks about them."]),
   ("Reducing dependency", [
    "Buyers discount anything that walks out the door with the owner. That includes supplier relationships held by one person, a single channel producing most of the revenue, and processes that exist only as habits.",
    "Reducing dependency does not mean rebuilding the company. It means writing down how orders are handled, giving a second person access to the important accounts, and, where possible, adding a second source for the products or traffic that carry the business."]),
   ("What the file should contain", [
    "<ul><li>Annual accounts for three years and a current interim statement</li><li>A revenue breakdown by channel, product group and country</li><li>Supplier and customer agreements, including the ones that were never signed</li><li>Access to analytics and advertising accounts, with historic data intact</li><li>An inventory list with age and turnover per group</li><li>Registrations: domains, trademarks, licences, hosting</li></ul>",
    "A file that is complete at the start shortens every stage that follows. It is also the cheapest form of negotiating strength, because a buyer who cannot find gaps has little to argue about."]),
  ],
  links=[("An article on preparing a business for sale", "/knowledge-base/preparing-for-sale"),
         ("Normalising results before a valuation", "/knowledge-base/normalization-of-online-business-results")]),

 dict(slug="information-memorandum", title="The information memorandum",
  meta="What belongs in an information memorandum for an online business, in which order, and which details are better kept for a later stage of disclosure.",
  fig=("funnel", "Each stage of disclosure narrows the audience. The memorandum is written for the group that has already signed."),
  lede="The memorandum is the document that turns interest into a conversation. It has one job: to let a serious candidate decide whether the business is worth their time, without handing away what makes it work.",
  sections=[
   ("Structure that works", [
    "<ol><li>A summary of what the business does and what is being offered</li><li>The market and where the business sits in it</li><li>Products, suppliers and margins per group</li><li>Channels: search, advertising, marketplaces, email, partnerships</li><li>Operations: order handling, stock, returns, service</li><li>Financial history, normalised and explained</li><li>The team, and what happens to it after a transfer</li><li>The reason for sale, stated plainly</li><li>The structure that is envisaged and the terms that are open</li></ol>"]),
   ("Tone", [
    "A memorandum that reads like an advertisement invites suspicion. A memorandum that reads like a technical report loses the reader in the second chapter. The register that works sits between the two: descriptive, specific and open about weak points.",
    "Naming a weakness early is not a concession. It removes the surprise from due diligence, and it makes every other claim in the document more credible."]),
   ("What stays out", [
    "Supplier names, customer lists, exact search terms driving traffic and the details of any pending negotiation belong in a later stage. So do employment contracts and anything that identifies staff.",
    "A useful test: if a document leaking to a competitor would cause real damage, it does not belong in a memorandum that is sent out to a dozen parties."]),
   ("The advertisement is not the memorandum", [
    "A public listing describes the business in a few lines, without naming it. Its purpose is to attract enquiries, not to inform. The memorandum follows only after a non-disclosure agreement is in place and the candidate has been checked.",
    "Writing both from the same source material keeps the two consistent, which matters more than it sounds. Candidates compare them line by line."]),
  ],
  links=[("What a sales memorandum contains", "/knowledge-base/sales-memorandum"),
         ("Writing a listing that attracts the right enquiries", "/knowledge-base/creating-a-catchy-sales-ad")]),

 dict(slug="pricing", title="Setting an asking figure and a range",
  meta="How an asking figure is set for an online business, why a range works better than a single number, and how the opening position shapes the negotiation that follows.",
  fig=("multiples", "Larger, steadier and less dependent earnings are valued on higher multiples than small and volatile ones."),
  lede="An asking figure is a negotiating position, not a valuation. It is chosen to attract the right candidates and to leave room for the concessions that a process always demands.",
  sections=[
   ("A range beats a number", [
    "A single figure invites a single response: a lower one. A range invites a conversation about which end applies and why. It also allows the seller to signal what would justify the upper end, such as a shorter payment period or a longer handover.",
    "The width of the range says something in itself. Too narrow and there is nothing to discuss. Too wide and the seller looks unsure of what the business is worth."]),
   ("What sets the level", [
    "Three things carry most of the weight. The level of normalised earnings and how stable they have been. The degree to which the business runs without its owner. And how easily a buyer can see the earnings continuing under different ownership.",
    "Size matters more than most sellers expect. Larger businesses attract buyers with access to finance and a professional process, and that competition alone moves the level."]),
   ("Anchoring", [
    "The first figure mentioned frames everything that follows, which is why it should never be improvised in a first meeting. A prepared range, with the reasoning behind it written down, prevents a number being given away in an unguarded moment.",
    "Where the seller has a walk-away level, it belongs in a private note rather than in the conversation. Naming it turns it into the new starting point."]),
   ("When the market disagrees", [
    "If several qualified candidates arrive at similar conclusions well below the asking level, the market is giving an answer. The useful response is to find out which factor they are all pricing, because it is usually a single identifiable risk: one dominant supplier, a channel in decline, or figures that could not be reconciled.",
    "Fixing that factor is often worth more than defending the original figure."]),
  ],
  links=[("A structured way to determine the value of an online business", "/services/business-valuation"),
         ("What drives value in e-commerce", "/knowledge-base/e-commerce-value-drivers")]),

 dict(slug="buyer-search", title="Finding and screening buyers",
  meta="How candidate buyers for an online business are identified, approached and filtered, and why a shorter list usually produces a better outcome than a longer one.",
  fig=("funnel", "From a long list to a signed deal, each stage removes candidates for a different reason."),
  lede="The search is where a mandate earns its keep. Publishing a listing reaches people who are already looking. Approaching a list reaches the ones who were not.",
  sections=[
   ("Three sources", [
    "<ul><li><b>The platform.</b> Registered buyers who have described what they are looking for and can be matched against the profile of the business.</li><li><b>The direct approach.</b> Companies for which this business would be an addition rather than a purchase, contacted individually and confidentially.</li><li><b>The adjacent network.</b> Suppliers, partners, competitors and former employees, approached with more caution because the relationship survives the process either way.</li></ul>"]),
   ("Screening before disclosure", [
    "A candidate is worth the memorandum once three things are established: that they can fund a transaction of this size, that they have a reason to want this specific business, and that they are able to decide without a long chain of approvals.",
    "The check is not intrusive. A short conversation about what has been bought before, how the purchase would be funded and who else is involved in the decision filters out most of the traffic."]),
   ("The cost of a long list", [
    "Every additional party who receives the memorandum increases the chance of a leak, and each one absorbs the seller's attention. Ten well-chosen candidates usually produce more competitive tension than fifty poorly chosen ones, because the ten are all capable of finishing.",
    "Competition is useful, but it comes from candidates being real rather than numerous."]),
   ("Keeping the process running", [
    "Candidates move at different speeds. A schedule with a date for questions, a date for indications and a date for a decision keeps the group roughly aligned and prevents the fastest party from setting terms while the others are still reading.",
    "Where a candidate misses a step twice, the honest reading is usually that the interest was never firm."]),
  ],
  links=[("Registered buyers and the parties currently searching", "/online-business-for-sale/companies-wanted"),
         ("How the sale process is run on the platform", "/services/how-to")]),

 dict(slug="confidentiality", title="Confidentiality and staged disclosure",
  meta="How confidentiality is protected during a sale: anonymous listings, non-disclosure agreements, staged disclosure and what to do when word gets out anyway.",
  lede="Confidentiality is not a document; it is a sequence. Information is released in stages, and each stage costs the candidate something before the next one opens.",
  sections=[
   ("The stages", [
    "<ol><li>An anonymous description: sector, size band, structure, no names</li><li>A non-disclosure agreement, signed by the party who can bind the buyer</li><li>The memorandum, with suppliers and customers still masked</li><li>A managed data room, opened per subject as questions arise</li><li>Direct access to accounts and systems, usually only after signing</li></ol>"]),
   ("What an agreement actually does", [
    "A non-disclosure agreement rarely produces damages in practice, because proving loss from a leak is difficult. Its real function is to make the obligation explicit and to give the seller grounds to stop the process without argument.",
    "The clauses worth checking are the ones about non-solicitation of staff and suppliers, the duration, and whether advisers of the buyer are bound as well."]),
   ("Leaks", [
    "Most leaks are accidental: a candidate mentions the search to a supplier who also supplies the seller, or a job advertisement makes the timing obvious.",
    "The response that works is a short, factual message to the people affected, sent by the owner, before the rumour has time to grow. Denial usually confirms what it tries to hide."]),
   ("Staff", [
    "Telling the team early risks losing people; telling them late risks losing trust. In practice, the people who would have to answer buyer questions are informed once a deal is reasonably certain, under the same obligation of confidence, and the wider group at signing.",
    "Whatever the timing, staff should hear it from the owner rather than from a candidate walking through the warehouse."]),
  ],
  links=[("How information is shared during a sale", "/knowledge-base/sharing-information"),
         ("Customer data and privacy obligations at transfer", "/knowledge-base/customerbase-privacy-gdpr")]),

 dict(slug="negotiation", title="From indication to offer",
  meta="How a non-binding indication becomes a written offer, which points are negotiated first, and why price is rarely the item that decides a transaction.",
  fig=("bridge", "The headline figure and the amount that actually changes hands are separated by debt, cash and working capital."),
  lede="Negotiation in a business sale is less an argument about one number than an ordering exercise: which points are settled first, and which are left until the parties have invested enough to want a result.",
  sections=[
   ("Indications first", [
    "A non-binding indication states a range, the assumed structure, the conditions and a timetable. It costs the candidate little, which is why it should never be treated as agreement.",
    "Its value is comparative. Three indications side by side show which candidate has understood the business and which has copied a formula."]),
   ("Order of play", [
    "Structure before figure. Whether the transaction is an asset deal or a share deal changes the tax outcome for both parties, and a figure agreed before the structure is settled will have to be renegotiated.",
    "After structure come the terms that shift risk: how much is paid at closing, what is deferred, what depends on results, and which warranties are given and for how long."]),
   ("Where value actually moves", [
    "A lower headline figure paid in full at closing can be worth more than a higher one with half deferred over three years. The comparison that matters is what is certain, when it arrives and what has to be done to earn it.",
    "The same applies to working capital. A deal that leaves stock and receivables inside the business is not comparable to one that does not, however similar the two figures look."]),
   ("Deadlock", [
    "When the parties are apart on figure alone, the usual bridges are a deferred element, a vendor loan, or an earn-out tied to a measurable result. Each transfers risk in a different direction, and each is only workable if the measurement can be defined without ambiguity.",
    "Where the gap is about belief rather than risk, no structure will close it. Ending the conversation early is cheaper than a process that collapses during due diligence."]),
  ],
  links=[("From an agreed deal to the amount actually paid", "/knowledge-base/equity-bridge-from-deal-to-price"),
         ("What an earn-out is and how it is measured", "/knowledge-base/what-is-an-earn-out")]),

 dict(slug="term-sheet", title="The term sheet",
  meta="What a term sheet records, which parts are binding, and why the document is worth the time it takes even though most of it is not enforceable.",
  fig=("timeline", "A term sheet usually lands about halfway through a process and sets the schedule for everything after it."),
  lede="A term sheet writes down what the parties believe they have agreed, before lawyers turn it into contracts. Most of it is not binding, and it still determines the outcome.",
  sections=[
   ("What it contains", [
    "<ul><li>The object: shares or assets, and exactly which ones</li><li>The consideration and how it is split between closing and later</li><li>Conditions that must be met before signing</li><li>The scope and duration of the due diligence period</li><li>Exclusivity: whether the seller may keep talking to others</li><li>Warranties in outline, and any cap on liability</li><li>A timetable with dates rather than durations</li></ul>"]),
   ("The binding parts", [
    "Exclusivity, confidentiality and the allocation of the parties' own costs are usually binding. The commercial terms are not, and saying so explicitly avoids a later argument about whether a deal already existed.",
    "Exclusivity deserves attention because it is the moment the seller gives up leverage. A period long enough to complete an investigation, and no longer, is the balance most advisers aim for."]),
   ("Why it is worth the effort", [
    "Every point that is left open in a term sheet reappears during contract drafting, when both sides are tired and one of them has already stopped looking at alternatives. Points settled early are settled cheaply.",
    "A term sheet also functions as a test of decisiveness. A candidate who cannot commit to an outline will not commit to a contract."]),
  ],
  links=[("What a term sheet covers in a business transaction", "/knowledge-base/term-sheet"),
         ("The steps of an acquisition process", "/knowledge-base/business-acquisition-process")]),

 dict(slug="due-diligence", title="Due diligence",
  meta="How due diligence on an online business is organised, which areas are examined, and how findings translate into adjustments to the deal rather than the end of it.",
  fig=("dataroom", "Findings are grouped by subject so that each one can be answered once and closed."),
  lede="Due diligence is a structured search for the difference between what was represented and what is there. Well run, it confirms a deal. Badly run, it becomes an open-ended fishing trip.",
  sections=[
   ("The areas", [
    "<ul><li><b>Financial.</b> Reconciling reported results to bank statements and platform data, testing normalisation, checking working capital.</li><li><b>Commercial.</b> Concentration in customers, suppliers and channels; margin per product group; the trend behind the totals.</li><li><b>Legal.</b> Ownership of domains and trademarks, contract transferability, employment matters, disputes.</li><li><b>Technical.</b> Platform, hosting, integrations, code ownership, security and data handling.</li><li><b>Marketing.</b> Traffic sources, dependence on paid channels, the state of search visibility and the history of the accounts.</li></ul>"]),
   ("Scope and time", [
    "An investigation with a defined scope and a fixed end date produces answers. One without either produces new questions each week, and a seller who slowly loses patience and negotiating position.",
    "The scope belongs in the term sheet. Its limits are as important as its content."]),
   ("What findings do", [
    "Most findings do not end a transaction; they move a term. A supplier contract that cannot be transferred becomes a condition. Overstated normalisation becomes a lower figure. An undocumented process becomes a longer handover.",
    "Findings that do end transactions tend to share one trait: they suggest the information given earlier was not reliable. Accuracy is worth more than presentation, at every stage."]),
   ("The seller's own investigation", [
    "Sellers increasingly commission a scan of their own business before going to market. It surfaces the same issues earlier, when there is time to fix them and no counterparty is watching.",
    "It also shortens the buyer's work, which shortens the period during which a deal can fall apart."]),
  ],
  links=[("What a due diligence investigation covers", "/knowledge-base/due-diligence"),
         ("Business scans commissioned before going to market", "/services/due-diligence")]),

 dict(slug="deal-structures", title="Asset deal, share deal and what sits between",
  meta="The difference between an asset transaction and a share transaction, and the structures used when the two parties want different things.",
  fig=("asset", "The choice determines what moves, what stays behind and who carries the history."),
  lede="Structure is the first commercial decision in a transaction and the one most often taken last. It changes the tax outcome, the risk that transfers and the work involved in completing.",
  sections=[
   ("Asset transaction", [
    "Selected assets change hands: the domain, the stock, the customer database, the contracts that can be assigned. The legal entity stays with the seller, along with its history and most of its liabilities.",
    "Buyers tend to prefer this. It is cleaner, and unknown obligations from the past stay where they were. The complication is practical: every contract, licence and account has to be transferred individually, and some counterparties will use the moment to renegotiate."]),
   ("Share transaction", [
    "The entity itself is sold. Contracts, permits and registrations usually remain in place because the counterparty has not changed, which makes completion far simpler.",
    "The trade-off is that the history transfers too. Buyers respond with wider warranties, longer liability periods and, frequently, a portion of the consideration held back or placed with a third party."]),
   ("In between", [
    "<ul><li><b>Staged acquisition.</b> A first portion now, the rest on agreed dates or results.</li><li><b>Management buy-in or buy-out.</b> An incoming manager or the existing team takes over, often with seller financing.</li><li><b>Carve-out.</b> One brand or one webshop is separated from a larger group before sale.</li><li><b>Asset deal with a service agreement.</b> The seller continues to run parts of the operation for a defined period.</li></ul>"]),
   ("Choosing", [
    "The decision usually turns on three questions: how much of the value sits in transferable contracts, how much unknown history the entity carries, and what the tax position of the seller allows.",
    "Because the tax outcome differs per country and per shareholding structure, the structure is one of the few points where advice should be taken before a position is stated."]),
  ],
  links=[("Asset transaction or share transaction, compared", "/knowledge-base/asset-or-share-transaction"),
         ("Buy-in and buy-out routes", "/knowledge-base/management-buy-in-out")]),

 dict(slug="financing", title="How buyers fund a transaction",
  meta="The funding routes behind acquisitions of online businesses: equity, bank debt, seller financing, earn-outs and revenue based finance, and what each means for the seller.",
  fig=("escrow", "Where part of the consideration is held by a third party, the release conditions are as important as the amount."),
  lede="How a buyer funds a purchase shapes what the seller ends up with. A funding structure that looks like the buyer's problem is, in practice, a shared one.",
  sections=[
   ("The usual components", [
    "<ul><li><b>Own funds.</b> The portion the buyer brings. It signals commitment more than anything else in an offer.</li><li><b>Bank finance.</b> Available where there are tangible assets or a long, stable record. Online businesses without stock often struggle here.</li><li><b>Seller financing.</b> Part of the consideration is left in the business as a loan, repaid over time. Common, and often the element that makes a deal possible.</li><li><b>Earn-out.</b> A part tied to results after the transfer.</li><li><b>Revenue based finance.</b> Repayment as a share of turnover; used mostly in smaller e-commerce transactions.</li></ul>"]),
   ("What a seller should ask", [
    "Whether the funding is confirmed or expected. Who the lender is and what conditions attach. Whether the deferred elements are secured, and against what. And what happens to those elements if the business underperforms for reasons the seller does not control.",
    "A buyer who cannot answer these questions in a first conversation is not yet in a position to make a firm offer."]),
   ("Security", [
    "Deferred amounts can be protected with a pledge over shares, a bank guarantee, a personal commitment or an escrow arrangement. Each has a different cost and a different level of comfort.",
    "The instrument matters less than the trigger: what event releases the money, who determines that the event has occurred, and how a disagreement about it is resolved."]),
  ],
  links=[("Financing a business takeover", "/knowledge-base/financing-business-takeover"),
         ("Vendor loans and how they are structured", "/knowledge-base/vendor-loan")]),

 dict(slug="closing-and-handover", title="Signing, transfer and handover",
  meta="What happens between signing and a completed handover of an online business: accounts, contracts, stock, data and the support period that follows.",
  fig=("handover", "A handover is a checklist. Most disputes after closing concern an item that was never on it."),
  lede="Signing is a legal moment; the handover is an operational one. They are rarely the same day, and the gap between them needs its own plan.",
  sections=[
   ("The sequence", [
    "<ol><li>Contracts signed and conditions confirmed as met</li><li>Payment of the amount due at closing, or its deposit with a third party</li><li>Transfer of domains, hosting, platform and payment providers</li><li>Reassignment of advertising, analytics and marketplace accounts</li><li>Notification of suppliers, and where required their consent</li><li>Stock count and transfer of location</li><li>Customer data transferred under the agreed conditions</li></ol>"]),
   ("Accounts are the hard part", [
    "Advertising and marketplace accounts frequently cannot simply change owner. Some are tied to a legal entity, some to a person, some carry history that is lost if a new account is opened.",
    "This is worth checking during preparation rather than after signing. A marketplace account that cannot be transferred can be a material part of the value on offer."]),
   ("The support period", [
    "A defined period of support, with agreed availability and a clear end, works better than an open promise to help. It gives the buyer a real transfer of knowledge and gives the seller a horizon.",
    "Where a longer involvement is wanted, it belongs in a separate agreement with its own terms rather than as an informal extension of goodwill."]),
   ("After the handover", [
    "Deferred payments, earn-out measurement and warranty periods keep the parties connected for months or years. Agreeing in advance how results will be reported, and who checks them, removes most of the friction from that phase.",
    "The last practical step is unglamorous and often forgotten: closing down duplicate access, revoking old logins and confirming in writing that everything on the list has moved."]),
  ],
  links=[("Transferring an online business in practice", "/knowledge-base/transfer-online-business"),
         ("The transfer document used at completion", "/knowledge-base/transfer-document")]),
]
