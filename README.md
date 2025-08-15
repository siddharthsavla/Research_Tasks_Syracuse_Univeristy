# 🧠 Task 05: Descriptive Statistics & LLM Validation  
**Dataset:** Syracuse Men's Soccer – 2024 Season  

This project blends Python-powered descriptive analytics with LLM-based reasoning to analyze player and team performance. We compare both outputs to validate insights, surface efficiency metrics, and provide tactical takeaways.

---

## 📦 Dataset

- **File:** `syracuse_mens_soccer_2024_full.xlsx`  
- **Sheets used:**  
  - `Players` – Player-level stats (e.g., goals, assists, shots)  
  - `Goalies` – Goalkeeper stats (e.g., saves, minutes, goals against)  
  - `Team Totals` – Aggregated team vs. opponent performance

---

## ✅ Workflow

1. Load and preprocess player/team data using `pandas`
2. Perform Python-based statistical analysis
3. Ask LLM (ChatGPT) the same analytical question
4. Compare LLM's interpretation with our programmatic output
5. Validate, correct, or challenge LLM logic where needed

---

## 📊 Analysis Summary

| No. | Topic | Metric |
|-----|-------|--------|
| 1️⃣ | Team Scoring Rate | Average Goals per Game |
| 2️⃣ | Top Performers | Most Points (Goals + Assists) |
| 3️⃣ | Shooting Precision | Shot Accuracy (SOG / SH) |
| 4️⃣ | Impact per Minute | G+A per 90 minutes |
| 5️⃣ | Game Winners | Goals that led to wins |
| 6️⃣ | Discipline ROI | (G+A) per Card (YC + RC) |
| 7️⃣ | Coach Strategy | Attack vs. Defense Focus |
| 8️⃣ | Goal Conversion Rate | Goals per Shot (min 5 shots) |
| 9️⃣ | Goalkeeper Efficiency | Saves per Goal Allowed |
| 🔟 | Underrated Playmakers | Points per Shot (PTS / SH) |

---

## 📅 Weekly Progress

- ✅ **Last Week (Tasks 1–7):** Team scoring efficiency, top performers, discipline-to-contribution ratio, and a recommendation for next season’s coaching focus.
- ✅ **This Week (Tasks 8–10):**  
  - Identified **Kristjan Fortier** as the most efficient scorer by goals/shot  
  - Evaluated **goalkeeper performance** with Jason Smith leading in saves per GA  
  - Highlighted **underrated players** by their **points per shot**, again spotlighting Fortier’s efficiency

---

## 🧠 LLM Validation

For each task, the LLM was prompted to answer based on the context of the data. Its outputs were compared with our Python calculations. We marked each as:

- ✅ **Match:** LLM aligned with Python results  
- ⚠️ **Partial Match:** LLM was close, but with minor discrepancies  
- ❌ **Mismatch:** Incorrect or logically flawed response  

The comparison not only tested the LLM’s accuracy but also revealed when it added contextual insights—like recognizing underutilized talent or explaining stats in simple terms.

---

## 🔧 Tools Used

- **Python Libraries:** `pandas`, `matplotlib`  
- **Interface:** Jupyter Notebook  
- **AI Validation:** ChatGPT  
- **Source:** Excel dataset from Syracuse Men’s Soccer team

---

## 📌 Conclusion

This task demonstrated how combining programmatic analysis with AI interpretation can uncover deeper insights into sports data. We were able to validate key performance trends, identify high-efficiency players, and generate actionable strategies—all while verifying the reliability of LLM outputs against hard data.

---
