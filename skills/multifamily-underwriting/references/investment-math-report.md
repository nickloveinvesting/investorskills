# Investment Math & Return Modeling for Small-Balance Multifamily (5–50 Units, Pre-1990)

## Executive Summary

Defensive underwriting is the discipline of assuming things go wrong and still demanding that the deal works. In the 2025–2026 environment—characterized by elevated interest rates, an insurance hard market, aging physical plant, and uneven rent growth—your final filter must be an investment model that preserves capital first and chases upside second.

For small-balance multifamily (5–50 units) built pre‑1990, the non‑negotiable underwriting metrics are tightening. Lenders and sophisticated buyers now treat a **1.25x DSCR** as the minimum floor, not a target, with 1.30x+ preferred for older assets and tertiary markets.[1][2][3] Reserve expectations have increased to **3–6 months of PITIA and operating expenses** as standard, reflecting volatility in taxes and insurance.[4] Breakeven occupancy must be modeled conservatively, often landing **5–10 percentage points below your realistic stabilized occupancy**, to create buffer for lease‑up slippage, make‑ready downtime, and unexpected maintenance.

Mathematically, a defensively underwritten deal in 2026 must:

- Clear **1.25x DSCR** on underwritten, not pro‑forma “wishful,” NOI, including realistic repairs & maintenance and full insurance/tax loads.
- Avoid **negative leverage**, i.e., situations where the **going‑in cap rate is below the all‑in cost of debt**, which drags cash‑on‑cash below the unlevered yield and forces you to rely on an aggressive exit to make the deal pencil.[5][6]
- Demonstrate a **yield-on-cost** spread of at least **150–200 bps over exit/market cap rate** for heavier value‑add in older stock, recognizing higher cap‑ex, operational risk, and exit liquidity risk.
- Remain viable under stress tests that include: (1) **10–15% OpEx shock** (driven largely by insurance and utilities), and (2) **50 bps annual expansion in exit cap rate**, compounding over the hold.[7][8]

Your go/no‑go framework should treat these as **kill switches**, not “soft” guidelines:

- If **stabilized DSCR < 1.25x** at reasonably conservative assumptions (no heroic rent growth, full insurance/tax loads, recurring cap‑ex), the deal is a pass.
- If **levered cash‑on‑cash at stabilization** is materially **lower than unlevered yield** (negative leverage) and cannot be remedied with structure (seller carry at below‑market rate, interest‑only period, principal‑only window), the deal is a pass.
- If **breakeven occupancy** sits above 85–88% on a C‑class, pre‑1990 asset in a non‑core market, you have razor‑thin margin for error; treat as high‑risk unless pricing is deeply discounted.

Owner financing and subject‑to structures can create attractive blended rates and front‑loaded cash flow, but they don’t change physics: if DSCR, breakeven, and yield‑on‑cost don’t clear conservative hurdles **after** stress testing, you walk. The role of your 5‑year dynamic pro forma is to aggregate operations, rehab, and financing into a single decision engine that answers one question: *Does this deal preserve capital through a bad cycle while compensating you for real risk?* If the model cannot defend that answer quantitatively, the correct move is **no‑go**, regardless of story, upside, or broker pressure.

---

## Foundational Model Architecture

### 1. Core Flow: From Gross Potential Rent to Cash Flow After Debt Service

At its simplest, your 5‑year pro forma should follow this stack for each year (and ideally each month, then aggregate):

1. **Unit‑Level Inputs**
   - Units, bedroom/bath mix, current rent roll, market rent by unit type.

2. **Income Stack**
   - **Gross Potential Rent (GPR)** = Sum of *market* rents at 100% physical occupancy.
   - **Loss to Lease (LTL)** = GPR – Contract Rent (actual in‑place rents). You’ll model LTL burn‑off separately.
   - **Physical Vacancy** = GPR × Vacancy Assumption (5–10% for stabilized, 10–15% during heavy turns depending on scale and phasing).[9]
   - **Economic Vacancy / Collection Loss** = % of GPR (1–3% typical; higher for rougher assets).
   - **Other Income** = RUBS, parking, storage, laundry, pet fees, etc.
   - **Effective Gross Income (EGI)** = GPR – Vacancy – Concessions – LTL (if you treat separately) + Other Income.

3. **Operating Expenses**
   - Line‑itemed: Taxes, Insurance, Utilities, Repairs & Maintenance, Contract Services, Payroll, Admin, Marketing, Turnover, Management Fee, Replacement Reserves.
   - **Net Operating Income (NOI)** = EGI – Operating Expenses (before debt service and capital items).

4. **Capital Items and Financing**
   - **Recurring Cap‑Ex / Reserves**: For older assets, build in reserves beyond lender requirement (e.g., $300–$400/unit/yr+ depending on systems and historicals).[10]
   - **Debt Service**: Principal + interest across all liens, including seller carries, wraps, and subject‑to debt.
   - **Cash Flow Before Tax (CFBT)** = NOI – Total Debt Service – Capital Items (if treated below NOI in your convention).

This structure must be **modular**: income, OpEx, and debt are separate blocks, each with its own assumptions and sensitivity toggles.

### 2. Normalizing T‑12s for Pre‑1990 Assets

Older, mom‑and‑pop operated assets routinely present distorted T‑12s. Your job is to normalize into **lender‑style, sustainable NOI**:

- **Strip non‑recurring items**
  - Remove one‑time costs (roof replacement, legal settlements, one‑off make‑readies) from OpEx but model them in your cap‑ex schedule.

- **Normalize owner expenses and payroll**
  - Add back **owner perks** (auto, cell, travel) if not required for operations.
  - Impute a **market management fee** (e.g., 3–5% of EGI) even if self‑managed historically.
  - Normalize payroll to market for on‑site or part‑time staff.

- **Reset taxes**
  - Model property taxes at **post‑sale assessed value**, not historical. In Texas, assume near‑purchase price with jurisdiction‑specific caps and protests; build **scenario flags** for 10–20% above your base assumption if the appraisal district gets aggressive.

- **Reset insurance**
  - Replace historical premium with **quoted or estimated 2025–2026 premium** based on current market (often 2–4x 2019 levels in some Sunbelt markets, with higher volatility for frame buildings).[11] Build your base case on current quotes and **stress case at +10–15%**.

- **Adjust utilities and R&M**
  - Older systems (galvanized, cast iron, polybutylene, aluminum wiring, original HVAC) imply **higher baseline R&M**. Do not normalize to Class A benchmarks; use a **% of EGI** check (e.g., total OpEx often 40–55% of EGI for C‑class, pre‑1990, depending on taxes/insurance) and **unit‑level $/unit** benchmarks.

The goal: **Underwritten NOI** should be a realistic, slightly pessimistic view of stabilized operations, not what the seller or broker claims.

### 3. Inputting "Vintage Risk"

Pre‑1990 stock demands explicit modeling of building‑system risk:

- **Electrical**
  - Aluminum wiring, Federal Pacific/Zinsco panels: flag as risk. Budget for panel replacements and potential rewiring over the 5‑year hold.

- **Plumbing**
  - Polybutylene, galvanized, and cast iron stacks: expect rising leak frequency and intrusive repairs.

- **Building Envelope & Life Safety**
  - Roof age, siding, balconies, stair systems, fire separations, sprinklers, smoke/CO detectors.

Practical modeling approach:

- Build a **Cap‑Ex Schedule** tab separate from OpEx.
- Create **system‑level line items** (Electrical, Plumbing, Roof, Parking, Unit Interiors, Life Safety).
- For each, assign:
  - Total budget.
  - Phasing by year (e.g., 30% Yr 1, 40% Yr 2, 30% Yr 3).
  - Impact on rent (if interior upgrades) and on R&M (expected drop after replacement).

Feed these cap‑ex outlays into your **cash flow** (equity draw or financed) and your **NOI trajectory** (post‑rehab rent and OpEx improvements), so the model directly reflects vintage risk and mitigation.

---

## Advanced Metric Calculation

### 1. DSCR: Formula, Buffers, and Reserve Integration

**Base formula**:[2][12]

> **DSCR = NOI / Total Debt Service**
>
> Where Total Debt Service = Sum of all required principal & interest payments for the period.

For layered capital stacks (first lien + seller carry/second + wrap), compute:

- **DSCR
a) Senior‑only DSCR** = NOI / Senior Debt Service.
- **b) Global DSCR** = NOI / (Senior + Junior + Required Preferred Equity Payments).

In 2025–2026, with more volatile expenses and rate risk:

- Treat **1.25x global DSCR** as the **minimum floor** at stabilized year, with a **target 1.30–1.35x** for pre‑1990 C‑class assets in non‑core locations.[1][3][13]
- Build a **DSCR Sensitivity Table**:
  - Rows: NOI ± 5–15%.
  - Columns: Interest rate shocks (+50–150 bps) or blended rate changes.

**Reserves integration:** Some lenders and rating agencies increasingly look at **Net Cash Flow after replacement reserves** when computing DSCR.[14]

- Define **NCF** = NOI – Replacement Reserves – Required Escrows (tax/insurance if lender treats them below the NOI line).
- For your internal standard, compute:

> **DSCR_conservative = (NOI – Recurring Cap‑Ex Proxy) / Total Debt Service**

This bakes in the reality that C‑class plumbing and electrical will not behave like a 2015 vintage asset.

**Kill switch:** if **DSCR_conservative** does not reach 1.25x by the earlier of (a) year 2 post‑stabilization or (b) end of rehab period, the deal fails your screen.

### 2. Negative Leverage and Yield on Cost vs. Market Cap Rate

**Negative leverage** occurs when the **going‑in cap rate** (NOI / Purchase Price) is **lower than the cost of debt or mortgage constant**, which means leverage **reduces** your return on equity instead of enhancing it.[5][6][15]

- **Mortgage constant** ≈ Annual Debt Service / Loan Amount.
- If **Cap Rate < Cost of Debt**, then **Levered CoC < Unlevered Cap Rate**—you’re borrowing expensive money to buy a cheaper yield.

In high‑rate 2025–2026 conditions, this is rampant. For defensive underwriting in small‑balance multifamily:

- Avoid deals where **going‑in cap < interest rate** unless:
  - You are buying at a deep discount to replacement cost, **and**
  - You have strong, **visible NOI growth** within 18–24 months (e.g., massive loss‑to‑lease, obvious operational mismanagement) **and**
  - You can structure below‑market, often seller‑financed or assumable debt.

**Yield on Cost (YoC)**:

> **YoC = Stabilized NOI / Total Project Cost**

Compare YoC to **market/exit cap rate**.

- For heavy value‑add on vintage C stock, target at least **150–200 bps YoC spread** over your **underwritten exit cap**, not today’s market cap.[16][17]
  - Example: If you underwrite exit at 7.0% cap, you want **YoC ≥ 8.5–9.0%**.

This spread compensates for:

- Execution risk on rehab.
- Vintage systems risk.
- Financing and refinance risk in a potentially higher‑rate world.

### 3. IRR vs. Equity Multiple

**IRR (Internal Rate of Return)** is the discount rate that sets NPV of all cash flows to zero. It is **time‑weighted**: earlier cash flows matter disproportionately.

In heavy rehab deals with:

- Negative or low cash flow in years 1–2 (due to vacancy spikes and cap‑ex), and
- Large back‑end sale proceeds,

IRR can look attractive even if **absolute dollars returned** versus risk are marginal.

**Equity Multiple (EM)** gives you total dollars out vs. dollars in:

> **Equity Multiple = Total Distributions to Equity / Total Equity Invested**

Defensive use:

- For 5‑year value‑add, target **≥ 1.8–2.0x equity multiple** on conservative exit assumptions.
- Use IRR primarily to compare timing of different structures (e.g., subject‑to + IO vs. fully amortizing), not as the sole go/no‑go.

Rule of thumb:

- If **IRR ≥ 15–16%** but **Equity Multiple < 1.6x** under conservative stresses, you’re probably taking timing risk without enough absolute gain.
- Prioritize **higher equity multiple at similar risk** over “flashy” IRR driven by aggressive exits.

### 4. Cash-on-Cash: Levered vs. Unlevered and Owner‑Finance Impacts

**Unlevered CoC (or Yield):**

> **Unlevered CoC = NOI / Total Purchase Price (or Total Cost)**

**Levered CoC:**

> **Levered CoC = (CFBT to Equity) / Total Equity Invested**

In owner‑financed deals with low down payments and creative structures, Year 1 levered CoC can explode upward—but you must distinguish **sustainable yield** from **temporary boost**.

For pre‑1990, small‑balance assets in 2026:

- Target **Year 1 levered CoC** ≥ 6–8% on conservative assumptions **after** funding adequate reserves.
- Target **stabilized levered CoC** ≥ 8–10% once rehab is complete and DSCR ≥ 1.25–1.30x.

Be especially careful when:

- Down payment is <10–15% via seller carry or second liens.
- Early‑year debt service is artificially low due to interest‑only or principal‑only periods.

The model should clearly separate:

- **Operating cash flow** (from NOI), and
- **Financing effects** (e.g., IO, blended rates) so you can see whether CoC is driven by true operational strength or just “cheap” structure.

---

## Creative Finance Modeling

### 1. Owner Financing, Wraps, and Subject‑To Structures

In a **wraparound mortgage** or **subject‑to** structure:[18][19]

- The existing first lien stays in place (often at a below‑market fixed rate).
- The seller creates a new note (wrap or carry) at a different rate and terms.
- You pay the seller; the seller (ideally) services the underlying loan.

Modeling basics:

- **Existing Loan (Subject‑To)**
  - Input: Original balance, remaining term, interest rate, amortization schedule.
  - Use a standard amortization schedule to map remaining principal and annual debt service.

- **New Seller Note / Wrap**
  - Input: New principal (often equal to or greater than underlying balance), interest rate (often higher than underlying), amortization, and balloon.
  - Build a schedule for this note as a separate tranche.

- **Total Debt Service**
  - **If true wrap:** your payment on the wrap note includes pass‑through to the underlying loan; in your model, treat **total annual debt service** as the **wrap payment** (not double‑counting the underlying).
  - **If subject‑to + second lien:** debt service is the sum of **subject‑to P&I** + **second‑lien P&I or IO**.

### 2. Blended Rate Calculation

For multiple tranches (e.g., 70% subject‑to at 3.5%, 15% seller carry at 7.5%), compute the **blended interest rate**:

> **Blended Rate = (Σ Tranche Interest Expense) / (Σ Tranche Principal Balance)**

At underwriting point (Year 1):

- Let:
  - Loan 1: Balance L1, Rate r1.
  - Loan 2: Balance L2, Rate r2.

Then:

> **Blended Rate ≈ (L1×r1 + L2×r2) / (L1 + L2)**

In Excel, implement as:

- `=SUMPRODUCT(Balances_Range, Rates_Range) / SUM(Balances_Range)`

Use this blended rate for quick sanity checks on whether you’re **overpaying for leverage** relative to your going‑in cap.

### 3. Principal-Only and Interest-Only Periods

**Principal‑Only Periods** (rare but possible in seller finance):

- Payment is entirely principal; no interest accrues.
- Early‑year cash flow is **lower** than with IO (since principal must be retired), but **equity builds quickly**.
- Cash‑on‑cash can look weaker, but overall **equity multiple and DSCR improve** over time.

Modeling approach:

- Create a **flag** for months/years where interest rate is set to 0 and payment equals scheduled principal.
- Track **principal reduction** as a component of **equity build**, separate from cash distributions.

**Interest‑Only (IO) Periods**:

- Payment = Interest only; no amortization.
- DSCR appears stronger (since debt service is lower) and CoC increases.
- IRR can improve significantly because early‑year cash flow is high, especially in heavy rehab where you need liquidity.

Modeling approach:

- For IO years, set scheduled principal to 0; payment = Beginning Balance × Interest Rate.
- After IO expires, switch to amortizing schedule.

Impact on metrics:

- **IRR**: IO **front‑loads cash flow**, boosting IRR due to time value of money.
- **Equity Multiple**: May not change much unless IO period allows for more cap‑ex and NOI growth that feeds into higher terminal value.
- **Risk**: Balloon or refi risk at IO expiry—stress test DSCR and refinance economics at that point.

Rule: Use IO as a **bridge** to stabilization, not an excuse to overpay. If the asset fails DSCR or CoC tests **after** IO ends, the deal is fragile.

### 4. Effective Cost of Capital

For creative stacks, compute **effective cost of capital** to equity:

1. Compute **blended interest rate** (as above).
2. Incorporate **fees and points** (e.g., wrap execution fees, legal, additional reserves) by annualizing them over the expected hold.
3. Compare:
   - **Unlevered yield** (YoC) vs.
   - **Levered CoC** and
   - **Blended cost of debt**.

If your **unlevered yield** is 7.5% and **blended cost of debt** is 8.0–8.5%, you are in negative leverage unless value‑add is both **high probability and near‑term**.

---

## Stress-Testing & Sensitivity Analysis

### 1. Capital Preservation Test: 10% OpEx / Insurance Shock

Objective: Prove that the deal survives a **10–15% jump in OpEx**, driven primarily by insurance and utilities, without:

- DSCR falling below 1.15–1.20x, or
- Cash flow turning persistently negative.

Implementation:

1. Create **global stress switches** for OpEx and specific categories (Insurance, Utilities, R&M).
2. Use either scenario manager or separate columns:
   - Base Case.
   - **Stress Case 1:** +10% Insurance only.
   - **Stress Case 2:** +10% All OpEx.
   - **Stress Case 3:** +15% All OpEx.
3. For each case, recompute:
   - NOI.
   - DSCR (global).
   - Levered CoC.

Build an **Excel Data Table** with:

- Rows = Insurance increase (0%, 5%, 10%, 15%, 20%).
- Columns = Rent growth scenarios (0%, 2%, 3%).
- Intersection cell = DSCR or CFBT in Year 3.

Interpretation:

- If modest rent growth (2–3%) cannot offset a 10% insurance shock while keeping DSCR ≥ 1.25x, treat the deal as marginal.
- In markets with particularly volatile insurance regimes, test **20–25% insurance spikes** as a tail scenario.[11]

### 2. Market Softening Test: Exit Cap Rate Expansion

Exit cap rates are tightly connected to interest rates and credit spreads; rising rates tend to **expand cap rates and depress values**.[7][20][21]

For defensive underwriting:

- Take current market cap (from recent sales) and add a **minimum 50 bps per year of hold** for heavy‑value‑add, C‑class, pre‑1990 assets, or at least **100–200 bps over going‑in cap**.[16][22]

Implementation:

1. Base exit cap = max(current market cap, going‑in cap) + **conservative premium** (e.g., +100 bps).
2. Create sensitivity table:
   - Rows = Exit cap rate (Base – 50 bps, Base, Base + 50, +100 bps).
   - Columns = Year 5 NOI ± 5–15% (NOI growth scenarios).
   - Intersection cell = Equity Multiple or Sale Proceeds.

Remember:

> **Sale Price = Exit Year NOI / Exit Cap Rate**

Even a **50 bps increase in exit cap** can reduce value by double‑digit percentages; some research shows a 50 bps shift can change value by ~10–12% depending on starting yields.[7][20]

Interpretation:

- If Exit Cap +50–100 bps plus NOI –5% still delivers **≥ 1.6–1.7x equity multiple**, the deal is defensible.
- If the investment only works at flat or compressing cap rates, it is **speculation**, not conservative value‑add.

### 3. Breakeven Occupancy Analysis

Breakeven occupancy tells you the minimum **economic occupancy** required to cover operating expenses and debt service:

> **Breakeven Occupancy = (Operating Expenses + Debt Service) / Gross Potential Income**

Use **EGI or GPR** depending on your convention, but be consistent.

For pre‑1990 C‑class assets:

- A **breakeven occupancy above ~85–88%** is risky; above 90% is a red flag in secondary/tertiary markets.

Modeling steps:

1. Compute annual operating expenses (excluding depreciation and large one‑time cap‑ex).
2. Add **total annual debt service**.
3. Divide by **GPR** at market rents.

Stress‑test:

- Run scenarios where rents flatten or small concessions are added.
- If breakeven shifts upward materially (e.g., from 82% to 88%) with modest OpEx growth or rate increases, you’re running a tight ship.

---

## Practical Application: Building the Tool

### 1. Logical Flow for the Spreadsheet

Recommend a **tabbed structure**:

1. **Assumptions Tab**
   - Purchase price, closing costs, equity, debt terms (rate, amortization, IO period, points), hold period.
   - Rent growth, vacancy, loss‑to‑lease burn‑off schedule, expense inflation by category.
   - Exit cap rate assumptions and sales cost (brokerage, transfer tax).

2. **Rent Roll & Income Tab**
   - Unit‑level rent roll with current and target rents, renovation premium per unit type.
   - Formulas for GPR, LTL, physical and economic vacancy, other income.

3. **Operating Expenses Tab**
   - Line‑item expenses with **base year $/unit or % of EGI** and annual escalation.
   - Separate flags for insurance and utilities to apply higher volatility (e.g., base + 5% per year, plus separate shock scenarios).

4. **Cap‑Ex & Rehab Tab**
   - Phased interior and exterior budget, by system.
   - Link unit turns to rent increases and downtime.

5. **Debt Schedule Tab**
   - Separate amortization tables for each tranche: first lien, seller carry, wrap, mezzanine.
   - Flags for IO and principal‑only periods.

6. **Pro Forma Summary Tab**
   - Year‑by‑year NOI, debt service, DSCR, CoC, IRR, Equity Multiple.
   - Base and stressed cases side‑by‑side.

7. **Sensitivity Tab**
   - Excel Data Tables for DSCR vs. NOI/rates, Equity Multiple vs. exit cap/NOI, CoC vs. OpEx shocks.

### 2. Error-Checking and Guardrails

Because mistakes are expensive, embed **error checks**:

- **Balance checks**: Ensure total sources (equity + debt) = total uses (purchase + cap‑ex + closing + reserves).
- **Sign checks**: Cash flows should be negative at acquisition, positive in operations (unless assumed capital calls). Use conditional formatting to flag unexpected negative years.
- **DSCR checks**: Highlight any year where DSCR_conservative < 1.20x in yellow and <1.10x in red.
- **Breakeven checks**: Flag when breakeven occupancy > 88%.
- **Negative leverage flag**: If going‑in cap < blended cost of debt, return a clear “NEGATIVE LEVERAGE” warning.

Use nested IF statements or LOOKUP‑based logic to trigger warnings and adjust outputs (for example, turning a summary cell red and surfacing a “No‑Go per policy” text when multiple rules fail).

---

## Interconnections

Your Category 9/10 model is the **integration layer** for other categories:

- **Operations (Cat 7)** feed unit‑level rents, actual vs. market comparisons, realistic economic vacancy, and OpEx detail. The pro forma must be fed by *operational truth*, not broker OM averages.
- **Rehab (Cat 4)** drives cap‑ex line items, timing of unit turns, rent premium assumptions, and temporary vacancy spikes. Rehab phasing and scope directly shape YoC and DSCR trajectory.
- **Negotiation & Offer (Cat 10)** flows from the model output: once you define **minimum DSCR, YoC spread, CoC, and equity multiple thresholds**, you can back into **maximum supportable purchase price** by iterating purchase price until these thresholds are just met under conservative assumptions.

In practice, this means your model is not just a scoreboard—it is a **pricing engine**. You reverse‑solve for price: “At what basis do I hit 1.30x DSCR, 9% YoC vs. 7.5% exit cap, and 1.8x equity multiple under stressed exit?” That number becomes your walk‑away price.

---

## Key Takeaways & Action Items

1. **DSCR 1.25x is the floor, not the target**—aim for 1.30–1.35x on older, small‑balance assets.
2. **Negative leverage is a structural red flag**: if cap < cost of debt, walk unless structure and pricing are extraordinarily favorable and near‑term NOI growth is clear.
3. **Model YoC vs. exit cap with at least a 150–200 bps spread** for heavy value‑add.
4. **Use conservative, normalized T‑12s**: reset taxes, reset insurance, adjust R&M and payroll to realistic levels.
5. **Treat insurance as a volatile variable**, not a fixed line item; build +10–20% shock tests into your standard underwriting.
6. **Separate operating performance from financing tricks**: IO and principal‑only periods should be clearly isolated so you don’t confuse structural boost with real NOI strength.
7. **Use Equity Multiple alongside IRR**; in choppy markets, EM is often a cleaner test of whether the risk is worth the dollars returned.
8. **Breakeven occupancy above mid‑80s is a warning sign** in C‑class, pre‑1990 assets.
9. **Make stress testing standard**, not optional: every deal gets OpEx shock, rate shock, and exit cap expansion tables.
10. **Leverage Excel Data Tables and scenario switches** to run quick what‑ifs instead of hard‑coding multiple copies of your model.
11. **Integrate rehab and operations** tightly: every dollar of cap‑ex should have a rent/expense rationale and show up in the pro forma.
12. **Use the model as a pricing engine** to back into max offer price under conservative constraints.
13. **Codify kill switches** (DSCR, YoC spread, CoC, breakeven) so you are not negotiating with yourself once you like a deal’s story.
14. **Favor capital preservation over stretch returns**: if stress tests show you barely surviving modest shocks, it is not the right deal.

### Checklist Before Making an Offer

- [ ] T‑12 normalized; taxes and insurance reset to realistic 2025–2026 levels.
- [ ] All debt tranches modeled, including seller carries, wraps, and subject‑to loans.
- [ ] DSCR_conservative ≥ 1.25x at stabilized year; ≥ 1.20x during rehab.
- [ ] No negative leverage *or* clearly justified, near‑term value‑add with structure that lowers blended cost of capital.
- [ ] YoC ≥ exit cap + 150–200 bps.
- [ ] Equity Multiple ≥ 1.8x under base case; ≥ 1.6–1.7x under stressed exit cap/NOI.
- [ ] Year 1 and stabilized levered CoC meet your minimum target after reserves.
- [ ] Breakeven occupancy ≤ mid‑80s; sensitivity shows survivability with modest rent or OpEx shocks.
- [ ] Insurance shock (+10–15%) and exit cap expansion (+50–100 bps) stress tests passed.
- [ ] Error checks (balances, signs, DSCR, negative leverage flag) all clear.
- [ ] Resulting maximum supportable purchase price used as your **ceiling** in negotiations.

If any of the core kill switches fail under conservative assumptions, the default answer is **no‑go**, regardless of narrative upside.

---

## References

[1] Fannie Mae Multifamily. "Near-Stabilization Execution Term Sheet" (Minimum DSCR 1.25x for Tier 2). 2024.[36]
[2] JPMorgan Chase. "What is debt service coverage ratio (DSCR) in real estate?" 2025.[34]
[3] Multifamily.Loans. "How DSCR Loans Are Used in Multifamily Investing." 2023.[28]
[4] Park Place Finance. "DSCR Loan Requirements for High Net Worth Investors." 2025.[39]
[5] PropertyMetrics. "Negative Leverage: What You Should Know." 2025.[35]
[6] CrowdStreet. "What Is Negative Leverage In CRE?" 2026.[26]
[7] CoreCast. "Exit Cap Rates vs. Growth Rates in Terminal Value." 2025.[37]
[8] First National Realty Partners. "Introduction to Commercial Real Estate Stress Testing." 2024.[27]
[9] Gallagher & Mohan. "Stress Testing Strategies for Robust Real Estate Financial Analysis." 2024.[21]
[10] Freddie Mac. "Multifamily Maturity Risk Report." January 2024.[42]
[11] Insula Capital Group. "2025–2026 DSCR Lending Evolution: How Product Innovation, Credit Pressure, and Hybrid Structures Are Reshaping Real Estate." 2026.[48]
[12] CEP Multifamily. "How Real Estate Investors Use Debt Coverage Ratio." 2025.[31]
[13] Biz2Credit. "Rental Property Lenders and DSCR Loans: Investor Guide." 2025.[45]
[14] Fannie Mae Multifamily Guide. "Calculating the DSCR and LTV." 2023.[25]
[15] Lee & Associates. "Welcome to Negative Leverage in CRE." 2022.[23]
[16] Wall Street Prep. "Cap Rates and Interest Rates: Relationship in Real Estate." 2024.[46]
[17] CFA Institute. "The Interplay Between Cap Rates and Interest Rates." 2024.[40]
[18] Lone Star Land Law. "Wraparound Transactions in Texas." 2024.[41]
[19] Silb Law Firm. "Wraparound Loan Explained: Owner Financing with Existing Mortgage." 2025.[47]
[20] J.P. Acquisitions. "2 Different Approaches to Underwriting Exit Cap Rates." 2024.[43]
[21] CoreCast Blog. "Exit Cap Rates vs. Growth Rates in Terminal Value." 2025.[37]
