# -*- coding: utf-8 -*-
"""Valuation methods, described as an adviser would apply them."""

METHODS = [
 dict(slug="multiples", title="Multiples of earnings",
  meta="How earnings multiples are used to value online businesses, which earnings figure is multiplied, and what moves a business up or down the range.",
  fig=("multiples", "Within one sector the spread between the lowest and highest multiple is usually wider than the spread in earnings."),
  lede="The multiple method takes a normalised earnings figure and applies a factor drawn from comparable transactions. It is the most used method in this market, and the most often misapplied.",
  sections=[
   ("Which earnings figure", [
    "The multiple is meaningless without naming the base. Three are common. EBITDA, which ignores financing and depreciation. Operating profit, which does not. And seller's discretionary earnings, which adds back a single owner's remuneration and personal costs, and is used for owner-operated businesses.",
    "A multiple quoted on one base and applied to another produces a number that is wrong by a wide margin. Comparisons between transactions are only useful when the base is identical."]),
   ("What moves the factor", [
    "<ul><li>Size: larger earnings attract a wider group of buyers and a higher factor</li><li>Stability: a flat three-year record is worth more than a spike</li><li>Dependence on the owner: the less, the higher</li><li>Concentration: one supplier or one channel carrying the business pulls the factor down</li><li>Growth that can be explained and repeated, rather than growth from one lucky season</li><li>Transferability: accounts, contracts and rankings that survive a change of owner</li></ul>"]),
   ("The limits", [
    "A multiple assumes the future resembles the past. Where a business is in transition, where a channel has just changed the rules, or where results depend on a contract about to expire, the method describes history rather than value.",
    "It also compresses everything into one number, which makes it a poor tool for negotiating individual terms. It sets a level; the terms are argued separately."]),
  ],
  links=[("Definitions of the profit figures used in valuations", "/knowledge-base/profit-definitions"),
         ("Seller's discretionary earnings explained", "/knowledge-base/sellers-discretionary-earnings-sde-en")]),

 dict(slug="discounted-cash-flow", title="Discounted cash flow",
  meta="How discounted cash flow is applied to online businesses, what the discount rate represents, and why the terminal value usually carries most of the outcome.",
  lede="Discounted cash flow builds value from expected future cash, discounted for time and risk. It is the most defensible method in theory and the most sensitive to assumptions in practice.",
  sections=[
   ("The mechanics", [
    "Free cash flow is projected for a number of years, then a terminal value represents everything after that. Both are discounted at a rate that reflects the cost of capital and the risk of the business.",
    "For a small online business the projection period is usually three to five years. Beyond that, forecasts for a company dependent on advertising platforms and marketplaces are not credible enough to carry weight."]),
   ("Where the sensitivity sits", [
    "In most models the terminal value accounts for more than half of the outcome, sometimes far more. That means two assumptions dominate: the long-term growth rate and the discount rate. A change of one percentage point in either moves the result substantially.",
    "This is why a discounted cash flow calculation should always be presented as a range across scenarios rather than as a single figure. A model that produces one number invites false precision."]),
   ("Working capital and investment", [
    "Cash flow is not profit. Stock that has to be bought before it is sold, payment terms that differ between suppliers and customers, and periodic reinvestment in the platform all consume cash that never appears in the profit line.",
    "For stock-carrying businesses this is often the difference between an attractive model and an unworkable one."]),
   ("When it is the right tool", [
    "Discounted cash flow earns its place where the future is expected to differ from the past for reasons that can be described: a new market being entered, a contract starting, a loss-making line being closed.",
    "For a stable business with a flat record, it usually confirms what a multiple already showed, at considerably more effort."]),
  ],
  links=[("Discounted cash flow in a business valuation", "/knowledge-base/discounted-cash-flow-en"),
         ("Adjusted present value as a variant", "/knowledge-base/adjusted-present-value-en")]),

 dict(slug="sde", title="Seller's discretionary earnings",
  meta="What seller's discretionary earnings measures, how it is calculated for an owner-operated online business, and where the method stops being useful.",
  lede="Seller's discretionary earnings describes what a single working owner takes out of a business in total. It is the standard base for valuing small owner-operated companies.",
  sections=[
   ("The calculation", [
    "Start from operating profit. Add back the owner's remuneration and benefits, one-off costs, private costs run through the company, and non-cash items such as depreciation where relevant.",
    "The result answers a specific question: what would an owner who works in the business have available in a year, before financing and tax."]),
   ("Why it exists", [
    "In owner-run companies the reported profit says as much about tax planning as about performance. One owner pays themselves a minimal salary, another a generous one; the underlying businesses can be identical.",
    "Normalising to a single measure makes those two comparable, which is the only way a multiple drawn from other transactions means anything."]),
   ("Where it breaks down", [
    "The method assumes one working owner. With two or three active shareholders, adding back all of their remuneration overstates what a single buyer could earn.",
    "It also assumes the buyer will work in the business. A buyer who intends to hire a manager has to deduct that salary again, which is why larger transactions move to EBITDA as the base."]),
   ("Presentation", [
    "Every add-back needs a reference to the accounts and a one-line explanation. A list of adjustments without evidence is the fastest way to lose credibility in due diligence, and the adjustments removed at that stage are never recovered."]),
  ],
  links=[("Seller's discretionary earnings in detail", "/knowledge-base/sellers-discretionary-earnings-sde-en"),
         ("Normalising the results of an online business", "/knowledge-base/normalization-of-online-business-results")]),

 dict(slug="asset-based", title="Asset based valuation",
  meta="When the value of a business is measured from its assets rather than its earnings, and how intangible assets such as domains and brands are treated.",
  lede="An asset based valuation adds up what the business owns and subtracts what it owes. It sets a floor rather than a market value, and it is the method of last resort for a trading company.",
  sections=[
   ("Where it applies", [
    "It is used when earnings are absent or unreliable: a business being wound down, one that has never made a profit, or a collection of assets being sold without an operation attached.",
    "It also serves as a check. A business valued below the realisable value of its stock and equipment is being priced incorrectly, or the assets are worth less than the books suggest."]),
   ("Intangibles", [
    "For online businesses the interesting assets are rarely physical. A domain with history, a registered trademark, a customer database, content that ranks, a marketplace account with reviews: none of these appear at their real value in a balance sheet, and some do not appear at all.",
    "Valuing them separately is possible but imprecise. Domains have an observable market; rankings and databases mostly do not."]),
   ("Stock", [
    "Stock is the item most often overstated. Age, seasonality and returnability determine what it is worth to a buyer, not what was paid for it.",
    "A stock list split by age and turnover per group settles the discussion faster than any argument about principle."]),
  ],
  links=[("How intrinsic value is determined", "/knowledge-base/intrinsic-value"),
         ("The importance of the domain name in securing intellectual property", "/knowledge-base/importance-domain-name-for-assurance-intellectual-property")]),

 dict(slug="comparables", title="Comparable transactions",
  meta="How comparable transactions are used to sanity check a valuation, and the reasons published transaction data on small online businesses should be treated with care.",
  lede="Comparable transactions ground a valuation in what has actually been paid. The difficulty is that in this segment the data is thin, and the comparisons are rarely as close as they look.",
  sections=[
   ("What counts as comparable", [
    "Same sector is not enough. A useful comparison matches size, margin structure, channel mix, degree of owner involvement and the structure of the transaction itself.",
    "Two businesses with identical turnover can be a world apart: one selling own-brand products at high margin through search, the other reselling third-party goods on a single marketplace."]),
   ("Reading reported figures", [
    "Reported transaction values often include deferred elements and earn-outs that may never be paid. A figure quoted as a headline is not the same as the amount received.",
    "Where the structure is not disclosed, a comparison should be treated as indicative at best."]),
   ("Practical use", [
    "Comparables work best as a boundary check on a valuation produced by another method. If a multiple falls far outside the observed range for similar businesses, there should be a specific and statable reason.",
    "Where no such reason exists, the assumption behind the calculation deserves a second look."]),
  ],
  links=[("A market report on e-commerce transactions", "/knowledge-base/market-report-e-commerce-ma-2022"),
         ("Determining the value of an online business", "/knowledge-base/determining-online-business-value")]),
]
