# Market Sizing Methods

**Purpose:** Estimate market size credibly and fast. Used by `/market-sizing`, `/value-sizing`.

---

## Three Methods
| Method | How | Strength | Weakness |
|---|---|---|---|
| **Top-down** | Start from a total (population, industry revenue) and filter by segment, penetration, and share | Fast, uses published data | Can hide weak assumptions behind big numbers |
| **Bottom-up** | Units × price: number of customers × usage × price | Grounded in the unit economics | Needs customer and price data; risk of missing segments |
| **Analog / triangulation** | Compare to a similar market, region, or period | Fast sanity check | Analog may not hold |

**Rule:** Use at least two methods and reconcile. A gap above ±20-30% means an assumption is wrong. Find it.

## TAM / SAM / SOM
- **TAM:** Total demand for the product category.
- **SAM:** The part you can serve with your product and geography.
- **SOM:** The part you can realistically capture in the plan period.

## Process (6 steps)
1. **Define the market precisely:** product, customer, geography, time, price basis, what is excluded.
2. **Pick the unit:** revenue, units, transactions, users.
3. **Build top-down:** each filter written with source and rationale.
4. **Build bottom-up:** segment customers, size each, apply usage and price.
5. **Triangulate:** compare, explain the gap, adjust.
6. **Sensitivity:** vary the three biggest assumptions; report a range.

## Example Skeleton (travel distribution)
- Top-down: global hotel bookings × share booked through intermediaries × share in target region × average commission.
- Bottom-up: number of corporate travel programs in region × average spend × managed-travel penetration × take rate.
- Analog: more mature region's penetration curve applied with a lag.

## Back-of-Envelope Discipline
- Round aggressively; keep powers of ten honest.
- Write every assumption on the page.
- Check units on both sides.
- Ask: does the per-customer figure make sense?

## Source Hierarchy
1. Client internal data
2. Company filings and regulator data
3. Industry associations and government statistics
4. Analyst reports and databases
5. Expert interviews
6. Press and web (lowest; verify)

Cite the source and year for every input. Mark estimates as estimates.
