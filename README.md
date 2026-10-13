# India IPO GMP vs actual listing: an open track record

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23349741.svg)](https://doi.org/10.5281/zenodo.23349741)


How well does the grey market premium (GMP) predict an Indian IPO's listing? This dataset records the GMP of every mainboard IPO **before it listed** and compares it with the **actual listing-day result**. No values are back-filled.

**Live, auto-updating version:** https://paisatools.co.in/ipo/gmp-accuracy

## What it shows so far

35 mainboard IPOs listed between 3 September and 8 October 2026:

| Measure | Result |
|---|---|
| Direction correct (GMP and actual listing had the same sign) | **74%** |
| Average gap between GMP-implied and actual listing gain | **±12.5 percentage points** |
| GMP too optimistic / too pessimistic | **18 / 17** |

In short, GMP is a fair signal of which way an IPO will open, but an unreliable guide to how much. The error runs in both directions, so it isn't only hype.

## The data

`data/gmp_vs_listing.csv`, one row per IPO:

| Column | Meaning |
|---|---|
| `listing_date` | Listing date (YYYY-MM-DD) |
| `company` | Company name |
| `symbol` | Exchange symbol as recorded |
| `board` | Mainboard or SME |
| `issue_price_inr` | Issue price (upper end of the price band), ₹ |
| `gmp_inr` | Last grey-market premium recorded before listing, ₹ |
| `gmp_implied_gain_pct` | GMP as a % of the issue price |
| `actual_listing_gain_pct` | Listing-day close vs the issue price, % |
| `direction_correct` | `yes` if the GMP-implied and actual gains had the same sign |
| `abs_gap_pct_points` | Absolute gap between implied and actual gain, in percentage points |

To refresh it: `python scripts/refresh.py` (standard library only).

## Methodology and limitations (read before citing)

- **GMP implied** = the last grey-market premium recorded before listing, as a % of the issue price (upper end of the band).
- **Actual** = the listing-day close vs the issue price.
- **Direction correct** means GMP and the actual result had the same sign (both positive, or both negative/flat). It does not mean the size was right.
- **GMP is blended from public grey-market trackers.** It is unofficial and moves through the day, so the recorded figure is one snapshot, not a consensus.
- **No back-filling.** An IPO enters the table only if its GMP was captured live before listing. Records are written once and never revised.
- **Small sample.** The sample is 35 IPOs and grows with every listing.
- **Base rate.** Most Indian IPOs list at a premium, so a high "direction correct" rate partly reflects that base rate. The average gap is the more informative number.
- **Not investment advice.** GMP comes from an unregulated, informal market.

## Citation

> PaisaTools (2026). *India IPO GMP vs actual listing track record.* https://paisatools.co.in/ipo/gmp-accuracy

## Licence

The data is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): use it freely, including commercially, with attribution to PaisaTools and a link to https://paisatools.co.in/ipo/gmp-accuracy. The script in `scripts/` is MIT-licensed.


## Cite
PaisaTools (2026). DOI: [10.5281/zenodo.23349741](https://doi.org/10.5281/zenodo.23349741)
