# Day 27: Data Analysis with NumPy, pandas & Matplotlib

> **Phase 4 – Advanced & Professional** | Estimated time: 3.5 hours

## 🎯 Learning objectives

- Use NumPy arrays for fast numerical work.
- Load, clean, transform, and summarize data with pandas.
- Create basic charts with Matplotlib.

## 📖 Concepts

```bash
pip install numpy pandas matplotlib
```

### NumPy

```python
import numpy as np

a = np.array([1, 2, 3, 4])
a * 2                       # vectorized: [2 4 6 8]
a.mean(), a.std(), a.sum()
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
np.zeros((2, 3))
np.random.default_rng(42).integers(0, 10, size=5)

m = np.array([[1, 2], [3, 4]])
m.shape          # (2, 2)
m.T              # transpose
m @ m            # matrix multiplication
a[a > 2]         # boolean indexing
```

Vectorized operations are much faster than Python loops.

### pandas: Series and DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Ali", "Sara", "Omar"],
    "dept": ["IT", "HR", "IT"],
    "salary": [50000, 60000, 55000],
})

df.head()
df.info()
df.describe()
df.shape, df.columns, df.dtypes
```

### Loading and saving

```python
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")        # needs openpyxl
df = pd.read_json("data.json")
df.to_csv("clean.csv", index=False)
```

### Selecting data

```python
df["salary"]                       # column (Series)
df[["name", "salary"]]             # multiple columns
df.loc[0]                          # row by label
df.iloc[0:2]                       # rows by position
df[df["salary"] > 52000]           # boolean filter
df[(df["dept"] == "IT") & (df["salary"] > 50000)]   # use & | ~ with parentheses
df.query("dept == 'IT' and salary > 50000")
```

### Cleaning

```python
df.isna().sum()                    # missing values per column
df.dropna()                        # drop rows with missing values
df["salary"] = df["salary"].fillna(df["salary"].median())
df.drop_duplicates()
df["date"] = pd.to_datetime(df["date"])
df["name"] = df["name"].str.strip().str.title()
df["salary"] = df["salary"].astype(float)
df = df.rename(columns={"salary": "monthly_salary"})
```

### Transforming

```python
df["annual"] = df["monthly_salary"] * 12
df["band"] = pd.cut(df["monthly_salary"], bins=[0, 52000, 58000, 1e9],
                    labels=["low", "mid", "high"])
df["salary_rank"] = df["monthly_salary"].rank(ascending=False)
df = df.sort_values("monthly_salary", ascending=False)
df["name_len"] = df["name"].apply(len)
```

### Grouping and aggregation

```python
df.groupby("dept")["monthly_salary"].mean()
df.groupby("dept").agg(
    headcount=("name", "count"),
    avg_salary=("monthly_salary", "mean"),
    max_salary=("monthly_salary", "max"),
)
pd.pivot_table(df, index="dept", values="monthly_salary", aggfunc="sum")
```

### Merging

```python
pd.merge(orders, customers, on="customer_id", how="left")   # like SQL JOIN
pd.concat([df1, df2], ignore_index=True)
```

### Time series

```python
sales["date"] = pd.to_datetime(sales["date"])
monthly = sales.set_index("date").resample("MS")["amount"].sum()
```

### Visualization

```python
import matplotlib.pyplot as plt

df.groupby("dept")["monthly_salary"].mean().plot(kind="bar", title="Average salary")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig("salary.png", dpi=150)
plt.show()

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(monthly.index, monthly.values, marker="o")
ax.set_title("Monthly sales")
ax.grid(True)
```

Chart choices: **line** for trends over time, **bar** for category comparison, **histogram** for distributions, **scatter** for relationships. Always label axes and add a title.

### Good practices

- Avoid row-by-row loops (`iterrows`); use vectorized operations.
- Keep raw data untouched; write cleaned data to a new file.
- Document assumptions about missing and outlier values.
- Chained filters returning a view/copy can raise `SettingWithCopyWarning`; use `.loc` and `.copy()`.

## ⚠️ Common mistakes

- Using `and` / `or` instead of `&` / `|` in pandas filters.
- Forgetting parentheses around each condition.
- Not checking `dtypes` (numbers stored as strings).
- Ignoring missing values before calculating statistics.

## 🏋️ Exercises

1. Load a CSV, print `info()` and `describe()`, and report the missing values per column.
2. Find the top 5 products by revenue.
3. Compute month-over-month revenue growth.
4. Create a bar chart and a line chart from grouped data and save both as PNG.
5. Merge a customers table with an orders table and find the top customers.

## 🛠 Mini project: Sales data analysis

Analyze a sales CSV: clean the data, compute revenue by category and month, find top products, and generate charts and a text report.

📁 Complete code: [`projects/project-05-sales-data-analysis`](../../projects/project-05-sales-data-analysis/README.md)

## 📝 Summary

- NumPy provides fast arrays; pandas provides labeled tabular data.
- Clean first, then filter, group, and visualize.
- Prefer vectorized operations over loops.

⬅️ [Day 26](../day-26-rest-api-with-fastapi/README.md) | ➡️ [Day 28 – CLI Tools & Automation](../day-28-cli-tools-and-automation/README.md)
