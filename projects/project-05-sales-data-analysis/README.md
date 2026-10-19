# Project 05: Sales Data Analysis

**Day 27 project** | Difficulty: ⭐⭐⭐

Clean a sales dataset with pandas, compute business metrics, and generate charts.

## Setup and run

```bash
pip install pandas matplotlib
python generate_data.py     # creates sales.csv (500 sample orders)
python analysis.py          # prints report, saves report.txt and two PNG charts
```

## What it does

- Cleans data (duplicates, missing values, invalid quantities and prices).
- Revenue by category, top products, best/worst month, month-over-month growth.
- Saves a bar chart and a line chart.

## Concepts used

pandas `groupby`, `resample`, `nlargest`, boolean filtering, Matplotlib figures.

## Extension ideas

- Replace the sample data with a real dataset (e.g. from Kaggle).
- Add a regional breakdown and a customer table with a merge.
- Build an interactive dashboard with Streamlit.
