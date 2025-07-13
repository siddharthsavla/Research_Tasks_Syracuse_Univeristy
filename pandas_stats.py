import sys
import pandas as pd
from pathlib import Path

# Default filename and group-by columns
filename = "2024_fb_ads_president_scored_anon.csv"
GROUP_KEYS = ["Page Id", "Ad Id"]

# Allow filename and group keys to be passed from command line
if len(sys.argv) > 1:
    filename = sys.argv[1]
if len(sys.argv) > 2:
    GROUP_KEYS = sys.argv[2:]

# Check that the file exists
if not Path(filename).exists():
    sys.exit(f"File not found: {filename}")

# Step 1: Load the CSV file
df = pd.read_csv(filename)
print(f"\nLoaded {df.shape[0]} rows and {df.shape[1]} columns from {filename}")

# Step 2: Identify numeric and text columns
numeric_cols = df.select_dtypes(include='number').columns.tolist()
text_cols = df.select_dtypes(include='object').columns.tolist()

print("\nNumeric columns:", numeric_cols)
print("Text columns   :", text_cols)

# Step 3: Overall statistics for numeric columns
print("\n=== Overall Numeric Stats ===")
print(df[numeric_cols].describe().T)

# Step 4: Stats for text columns
print("\n=== Text / Categorical Stats ===")
for col in text_cols:
    print(f"\n{col}:")
    print(" Unique values :", df[col].nunique())
    if not df[col].dropna().empty:
        top = df[col].value_counts().head(1)
        print(" Most common   :", f"{top.index[0]} ({top.iloc[0]} times)")
    else:
        print(" No values found.")

# Step 5: Grouped statistics (mean, min, max, std) by group keys
if not all(k in df.columns for k in GROUP_KEYS):
    print(f"\nSkipping grouped stats: Some group-by keys not found: {GROUP_KEYS}")
else:
    print(f"\n=== Grouped Stats by {GROUP_KEYS} ===")
    grouped = df.groupby(GROUP_KEYS)[numeric_cols].agg(['mean', 'min', 'max', 'std'])
    print(grouped.head(5))
