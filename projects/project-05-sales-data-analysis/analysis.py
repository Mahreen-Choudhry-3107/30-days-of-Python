"""Sales Data Analysis - Day 27 project.

Concepts used: pandas cleaning, groupby, resampling, and Matplotlib charts.
Run generate_data.py first to create sales.csv.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # render to files; works without a display
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent


def load_and_clean(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    df = df.drop_duplicates().dropna()
    df = df[(df["quantity"] > 0) & (df["unit_price"] > 0)].copy()
    df["revenue"] = df["quantity"] * df["unit_price"]
    return df


def build_report(df: pd.DataFrame) -> str:
    total = df["revenue"].sum()
    by_category = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
    top_products = df.groupby("product")["revenue"].sum().nlargest(3)
    monthly = df.set_index("date").resample("MS")["revenue"].sum()
    growth = monthly.pct_change().mul(100).round(1)

    lines = [
        "SALES REPORT",
        "=" * 40,
        f"Orders: {len(df)}   Total revenue: {total:,.2f}",
        "",
        "Revenue by category:",
        by_category.round(2).to_string(),
        "",
        "Top 3 products:",
        top_products.round(2).to_string(),
        "",
        f"Best month : {monthly.idxmax():%B %Y} ({monthly.max():,.2f})",
        f"Worst month: {monthly.idxmin():%B %Y} ({monthly.min():,.2f})",
        "",
        "Month-over-month growth (%):",
        growth.dropna().to_string(),
    ]
    return "\n".join(lines)


def make_charts(df: pd.DataFrame, out_dir: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 4))
    df.groupby("category")["revenue"].sum().sort_values().plot(
        kind="barh", ax=ax, color="steelblue")
    ax.set_title("Revenue by category")
    ax.set_xlabel("Revenue")
    fig.tight_layout()
    fig.savefig(out_dir / "revenue_by_category.png", dpi=120)
    plt.close(fig)

    monthly = df.set_index("date").resample("MS")["revenue"].sum()
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(monthly.index, monthly.values, marker="o")
    ax.set_title("Monthly revenue")
    ax.set_ylabel("Revenue")
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(out_dir / "monthly_revenue.png", dpi=120)
    plt.close(fig)


def main() -> None:
    csv_path = HERE / "sales.csv"
    if not csv_path.exists():
        raise SystemExit("sales.csv not found. Run: python generate_data.py")
    df = load_and_clean(csv_path)
    report = build_report(df)
    print(report)
    (HERE / "report.txt").write_text(report, encoding="utf-8")
    make_charts(df, HERE)
    print("\nSaved report.txt, revenue_by_category.png, monthly_revenue.png")


if __name__ == "__main__":
    main()
