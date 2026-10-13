"""Refresh data/gmp_vs_listing.csv from the PaisaTools GMP track record API.
Usage: python scripts/refresh.py   (no dependencies beyond the standard library)
"""
import csv, json, urllib.request, pathlib, datetime

API = "https://paisatools-api.nilaykabariya12.workers.dev/api/ipo/accuracy"
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "gmp_vs_listing.csv"

req = urllib.request.Request(API, headers={"User-Agent": "india-ipo-gmp-accuracy/1.0 (+https://github.com/nils44344/india-ipo-gmp-accuracy)"})
with urllib.request.urlopen(req, timeout=30) as r:
    d = json.load(r)

rows = sorted(d["items"], key=lambda x: x["listed_ms"])
fields = ["listing_date", "company", "symbol", "board", "issue_price_inr", "gmp_inr",
          "gmp_implied_gain_pct", "actual_listing_gain_pct", "direction_correct", "abs_gap_pct_points"]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(fields)
    for x in rows:
        day = datetime.datetime.fromtimestamp(x["listed_ms"] / 1000, datetime.timezone.utc).date().isoformat()
        w.writerow([day, x["name"], x["symbol"], x["board"], x["issue"], x["gmp"], x["predicted"], x["actual"],
                    "yes" if x["hit"] else "no", x["err"]])
print(f"{len(rows)} rows -> {OUT}  (hit rate {d['hitRate']}%, avg gap ±{d['avgErr']} pts, since {d['since']})")
