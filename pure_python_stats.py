import sys
import csv
from collections import defaultdict, Counter
import statistics
from pathlib import Path

# Set default file name and default group-by columns
filename = "2024_fb_ads_president_scored_anon.csv"
GROUP_KEYS = ["Page Id", "Ad Id"]

# Allow user to pass file name from the command line
if len(sys.argv) > 1:
    filename = sys.argv[1]

# Allow user to pass custom group-by columns from the command line
if len(sys.argv) > 2:
    GROUP_KEYS = sys.argv[2:]

# Check if the file exists before trying to read it
if not Path(filename).exists():
    sys.exit(f"File not found: {filename}")

# Step 1: Load the CSV data into a list of dictionaries
with open(filename, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(f"\nLoaded {len(data)} rows from {filename}")

# Step 2: Identify which columns are numeric and which are text
sample_row = data[0]
numeric_cols = []
text_cols = []

# Check the first 10 rows of each column to guess the data type
for col in sample_row:
    is_num = True
    for row in data[:10]:
        val = row.get(col, "")
        try:
            float(val)
        except:
            is_num = False
            break
    if is_num:
        numeric_cols.append(col)
    else:
        text_cols.append(col)

print("\nNumeric columns:", numeric_cols)
print("Text columns   :", text_cols)

# Step 3: Calculate overall statistics for numeric columns
print("\n=== Overall Numeric Stats ===")

for col in numeric_cols:
    nums = []
    for row in data:
        val = row.get(col, "").strip()
        if val not in ("", "null", "NA"):
            try:
                nums.append(float(val))
            except:
                pass
    if nums:
        print(f"\n{col}:")
        print(" Count:", len(nums))
        print(" Mean :", round(statistics.mean(nums), 2))
        print(" Min  :", min(nums))
        print(" Max  :", max(nums))
        if len(nums) > 1:
            print(" Std  :", round(statistics.stdev(nums), 2))
        else:
            print(" Std  : N/A (only one value)")
    else:
        print(f"\n{col}: No valid numeric values")

# Step 4: Calculate overall statistics for text/categorical columns
print("\n=== Text/Categorical Stats ===")

for col in text_cols:
    values = [row[col] for row in data if row[col]]
    counter = Counter(values)
    print(f"\n{col}:")
    print(" Unique values :", len(set(values)))
    if counter:
        top, freq = counter.most_common(1)[0]
        print(" Most common   :", f"{top} ({freq} times)")
    else:
        print(" No values found.")

# Step 5: Calculate grouped statistics if valid group-by columns are present
group_keys = GROUP_KEYS

# Check if all specified group keys actually exist in the dataset
if not all(k in sample_row for k in group_keys):
    print(f"\nSkipping grouped stats: some group-by columns not found in data: {group_keys}")
else:
    print(f"\n=== Grouped Stats by {group_keys} ===")

    grouped = defaultdict(list)

    # Group rows by the given keys
    for row in data:
        key = tuple(row[k] for k in group_keys)
        grouped[key].append(row)

    count = 0

    # For each group, print statistics for numeric columns
    for key, rows in grouped.items():
        print(f"\nGroup: {key}")
        for col in numeric_cols:
            values = []
            for row in rows:
                val = row.get(col, "").strip()
                if val not in ("", "null", "NA"):
                    try:
                        values.append(float(val))
                    except:
                        pass
            if values:
                mean = statistics.mean(values)
                std = statistics.stdev(values) if len(values) > 1 else "N/A"
                print(f"{col}: count={len(values)}, mean={round(mean, 2)}, std={std}")
        count += 1
        if count == 5:
            break
