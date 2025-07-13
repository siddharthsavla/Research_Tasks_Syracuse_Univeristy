# Task_04_Descriptive_Stats

## 📄 Author

**Siddharth Savla**

## 🔎 Project Overview

This project explores descriptive statistics on social media activity datasets related to the **2024 U.S. Presidential Election**, using three approaches:

1. **Pure Python (no third-party libraries)**
2. **Pandas (powerful data analysis tool)**
3. **Polars (a faster alternative to pandas)**

Each script performs detailed column-wise analysis, including:

- Count, mean, min, max, and standard deviation for numeric fields
- Unique value counts and most frequent values for categorical fields
- Grouped analysis by `page_id` and `page_id + ad_id` or other relevant groupings

## 📂 Datasets Used

- `2024_fb_ads_president_scored_anon.csv`
- `2024_fb_posts_president_scored_anon.csv`
- `2024_tw_posts_president_scored_anon.csv`

---

## 📃 File Descriptions

- `pure_python_stats.py`: Computes stats using only Python's standard libraries (`csv`, `math`, `statistics`, `collections`)
- `pandas_stats.py`: Uses `pandas` to calculate descriptive statistics using `.describe()`, `.value_counts()`, etc.
- `polar.py`: Uses `polars` to replicate similar functionality with `group_by()`, `.agg()`, and `.n_unique()`

---

## 💡 Instructions to Run

Open your terminal or Anaconda shell and run the scripts like so:

```bash
# For Pure Python
python pure_python_stats.py 2024_fb_ads_president_scored_anon.csv
python pure_python_stats.py 2024_fb_posts_president_scored_anon.csv
python pure_python_stats.py 2024_tw_posts_president_scored_anon.csv

# For Pandas
python pandas_stats.py 2024_fb_ads_president_scored_anon.csv
python pandas_stats.py 2024_fb_posts_president_scored_anon.csv
python pandas_stats.py 2024_tw_posts_president_scored_anon.csv

# For Polars
python polar.py 2024_fb_ads_president_scored_anon.csv
python polar.py 2024_fb_posts_president_scored_anon.csv
python polar.py 2024_tw_posts_president_scored_anon.csv
```

---

## 📖 Key Insights & Observations

- Many of the columns had missing values represented as `"null"`, `"NA"`, or blanks. These were filtered before computing numeric stats.
- Facebook ads data had high variability in impressions and estimated spend, indicating some posts had significant promotion while others did not.
- In the Twitter dataset, `retweetCount` showed a wide range, highlighting varying levels of public engagement.
- Facebook posts had concentrated activity by a few pages, as seen in `Facebook_Id`, suggesting limited source diversity.

---

## ⚠️ Challenges Faced

- **Data Cleaning:** Especially in the pure Python version, identifying numeric vs text fields without hardcoding required checking multiple sample rows.
- **Standard Deviation:** Implementing it manually was tricky, especially ensuring it behaves like pandas when only one value is present.
- **Grouped stats:** Handling nested aggregation using dictionaries in pure Python was more verbose and error-prone than pandas.
- **Polars compatibility:** `value_counts` had to be done via expressions on single columns. It's fast, but error-prone if not careful.

---

## 🔍 Personal Reflections on the Data

This dataset provides a rich snapshot of digital campaigning trends during the 2024 U.S. elections. The ad and post engagement metrics vary widely across platforms, reflecting different strategies on Facebook vs. Twitter. The grouped analysis reveals which accounts were the most active, and how performance metrics differ by post or ad.


---

Feel free to reach out with questions or suggestions!