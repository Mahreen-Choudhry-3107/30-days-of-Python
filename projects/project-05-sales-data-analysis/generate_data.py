"""Generate a reproducible sample sales dataset (sales.csv)."""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)
PRODUCTS = {
    "Laptop": ("Electronics", 900),
    "Phone": ("Electronics", 600),
    "Headphones": ("Electronics", 80),
    "Desk": ("Furniture", 250),
    "Chair": ("Furniture", 150),
    "Notebook": ("Stationery", 4),
    "Pen": ("Stationery", 1.5),
}

out = Path(__file__).parent / "sales.csv"
start = date(2025, 1, 1)
with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "product", "category", "quantity", "unit_price"])
    for _ in range(500):
        product = random.choice(list(PRODUCTS))
        category, price = PRODUCTS[product]
        day = start + timedelta(days=random.randint(0, 364))
        writer.writerow([day.isoformat(), product, category,
                         random.randint(1, 5), price])
print(f"Wrote {out}")
