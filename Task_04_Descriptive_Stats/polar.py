# polars_stats.py
import sys
from pathlib import Path
import polars as pl

# -------- 1. Command-line setup --------
DATA_PATH = "2024_fb_ads_president_scored_anon.csv"
GROUP_KEYS = ["Page Id", "Ad Id"]

if len(sys.argv) > 1:
    DATA_PATH = sys.argv[1]
if len(sys.argv) > 2:
    GROUP_KEYS = sys.argv[2:]

print(f"\nUSING FILE : {DATA_PATH}")
print(f"GROUPING BY: {GROUP_KEYS}")

if not Path(DATA_PATH).exists():
    sys.exit(f"File not found: {DATA_PATH}")

# -------- 2. Load data --------
df = pl.read_csv(DATA_PATH)

# -------- 3. Identify numeric and text columns --------
numeric_types = (
    pl.Int8, pl.Int16, pl.Int32, pl.Int64,
    pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64,
    pl.Float32, pl.Float64
)

numeric_cols = [col for col in df.columns if df[col].dtype in numeric_types]
text_cols = [col for col in df.columns if df[col].dtype == pl.Utf8]

print("\nNumeric columns:", numeric_cols)
print("Text columns   :", text_cols)

# -------- 4. Overall numeric stats --------
print("\n=== OVERALL NUMERIC STATS ===")
for col in numeric_cols:
    stats = df.select(
        pl.col(col).count().alias("count"),
        pl.col(col).mean().alias("mean"),
        pl.col(col).min().alias("min"),
        pl.col(col).max().alias("max"),
        pl.col(col).std().alias("std")
    )
    print(f"\n{col}:")
    print(stats)

# -------- 5. Categorical (text) stats --------
print("\n=== TEXT / CATEGORICAL STATS ===")
for col in text_cols:
    unique_ct = df[col].n_unique()
    vc = df[col].value_counts()

    # Detect count column (usually "count")
    count_col = [c for c in vc.columns if c != col][0] if vc.columns else None

    print(f"\n{col}:")
    print(" Unique values :", unique_ct)

    if count_col and vc.shape[0] > 0:
        most_common = vc.sort(count_col, descending=True).row(0)
        print(f" Most common   : {most_common[0]} ({most_common[1]} times)")
    else:
        print(" Most common   : N/A")


# -------- 6. Grouped stats --------
if all(k in df.columns for k in GROUP_KEYS):
    print(f"\n=== GROUPED NUMERIC STATS BY {GROUP_KEYS} ===")

    agg_exprs = []
    for col in numeric_cols:
        agg_exprs += [
            pl.col(col).mean().alias(f"{col}_mean"),
            pl.col(col).min().alias(f"{col}_min"),
            pl.col(col).max().alias(f"{col}_max"),
            pl.col(col).std().alias(f"{col}_std"),
        ]

    grouped = df.group_by(GROUP_KEYS).agg(agg_exprs)
    print(grouped.head(5))  # Show only 5 groups
else:
    print("\nSkipping grouped stats: group keys not found in dataset.")
