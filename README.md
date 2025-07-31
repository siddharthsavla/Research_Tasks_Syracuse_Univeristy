Task 05 - Descriptive Statistics & LLM Validation
Dataset: Syracuse Men’s Soccer 2024 (Public Stats)
Author: Siddharth Savla

📌 Project Overview
This project is part of Task 05: Descriptive Statistics and Large Language Models (LLMs).
The goal is to analyze a sports dataset using Python and then validate LLM responses to natural language questions based on the same dataset.

The project demonstrates:

Descriptive statistics computation using Python (Pandas)

Querying a Large Language Model (ChatGPT) with the same questions

Comparison of LLM outputs vs Python calculations

Identifying hallucinations or reasoning errors by the LLM

Making coaching recommendations based on data

📊 Dataset
File: syracuse_mens_soccer_2024_full.xlsx

Sheets:

Players → Player‑level stats (G, A, SH, SOG%, Cards, GW Goals)

Goalies → Keeper stats (Minutes, Goals Against, Saves, GAA, Shutouts)

Team Totals → Syracuse & Opponent cumulative stats

🔹 Analyses Performed
The notebook answers 7 key questions:

1️⃣ Average Goals per Game
2️⃣ Top 3 Players by Total Points (G+A)
3️⃣ Player with Highest Shot Accuracy (≥5 shots)
4️⃣ Highest Impact per 90 mins (G+A per 90)
5️⃣ Game-Winning Contribution
6️⃣ Discipline vs Performance (G+A per Card)
7️⃣ Coaching Question:
Should the team focus on attack or defense to increase wins by 30%, and which 2 players should be prioritized?

For each question, the notebook includes:

Python analysis result

LLM (ChatGPT) answer

Comparison note ✅/❌ to indicate agreement

📂 Repository Contents

Task_05_Descriptive_Stats/
│
├── Task_05_LLM_Validation_Final.ipynb   # Main notebook with Python + LLM comparison
├── README.md                             # Project documentation (this file)
⚡ Key Findings
LLM Accuracy: LLM correctly answered most factual questions, but small-sample anomalies (e.g., Michal Gradus) required human reasoning.

Coaching Insight: Team has equal goals scored and conceded, with slightly worse shot conversion than opponents → focus on defense to convert draws into wins.

High-Impact Players:

Gabe Threadgold → Consistent scorer and most disciplined

Michael Acquah → Top assister and strong per‑minute impact

✅ How to Run
Clone the repository:
git clone https://github.com/<your-username>/Task_05_Descriptive_Stats.git

Open the notebook in Jupyter/VSCode:
jupyter notebook Task_05_LLM_Validation_Final.ipynb
Ensure you have pandas installed:
pip install pandas 

✨ Reflection
LLMs can answer basic descriptive questions correctly when data is small and structured.
Reasoning-intensive tasks (like coaching recommendations) still need Python validation to avoid hallucinations.

