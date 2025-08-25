
# Research Task 06 — AI-Generated Deep Fake Interview 🎥

**Author:** Siddharth Savla  
**Dataset:** Syracuse Men’s Soccer 2024 (from Task 05)  

---

## 📌 Project Overview
This project demonstrates how AI tools like **Gemini Veo 3 Fast** can be used to simulate a realistic, ESPN-style coach interview based on insights derived from the **Syracuse Men’s Soccer 2024 dataset** (Task 05).  
The interview highlights:
- Season performance recap
- Defensive strategy improvements
- Key player contributions
- Motivational closing message

The final output is a **25-second polished video** composed of three merged clips, edited professionally with CapCut.

---

## 🎯 Goal of the Task
- Transform insights from **Task 05** into an **AI-generated deep fake interview**.
- Simulate a realistic ESPN-style experience with dynamic camera angles, locker room vibes, and authentic crowd effects.
- Explore AI video generation tools, understand limitations, and learn iterative prompt engineering.

---

## 🛠️ Workflow

### **Step 1 — Understanding Requirements**
- Reviewed Task 06 instructions.

### **Step 2 — Exploring Tools**
Explored multiple AI tools for realistic video generation:
- **D-ID** & **HeyGen** → Tested but skipped due to watermark and paid plan limitations.
- **Synthesia** → Promising but unavailable under a student plan.
- **Gemini Veo 3 Fast** → Selected for its quality, dynamic scenes, and Gemini Pro subscription benefits.

**Limitations Faced:**
- 3-hour cooldown between generations.
- 8-second per clip limit → required splitting the interview into 3 parts.
- Dataset upload unsupported → manually summarized **Task 05** insights.

### **Step 3 — Building the Script & Prompts**
Created an **ESPN-style interview script** using **Task 05 insights**:
- Equal goals scored & conceded last season.
- Shot conversion lower than opponents.
- Recommended strengthening defense to improve win rate by ~30%.
- Highlighted players: **Gabe Threadgold** & **Michael Acquah**.

Added **realistic context details** to the prompts:
- Locker room/stadium/press conference backgrounds
- Crowd effects & lighting
- Camera angles & dynamic transitions
- Syracuse coach image for improved realism

### **Step 4 — Generating the Clips**
Used **Gemini Veo 3 Fast** to generate 3 individual clips:
1. **Season Recap** → Stadium backdrop, Syracuse banners, natural lighting.
2. **Defensive Strategy & Key Players** → Press conference setup, mics, branding.
3. **Motivational Closing** → Locker room vibe, blurred players, soft lighting.

### **Step 5 — Merging Final Interview**
- Used **CapCut** to merge all clips seamlessly.
- Added ESPN-style overlays, intro titles, and smooth transitions.
- Final runtime: **~25 seconds**.

---

## ⚙️ Tools Used

| Tool/Platform       | Purpose                      | Outcome             |
|---------------------|-------------------------------|----------------------|
| Gemini Veo 3 Fast   | AI video generation          | ✅ Generated 3 clips |
| Coach Image         | Realistic avatar + lip-sync  | ✅ Improved realism |
| CapCut              | Video merging + editing      | ✅ Final 25-sec video |
| D-ID / HeyGen       | Alternative video tools      | ❌ Explored only |
| Python              | Task 05 insights integration | ✅ Provided stats |

---

## 🧩 Prompts Used
All **Gemini Veo 3 prompts** are included in the [Task_06_Deep_Fake_Prompts.txt](./Task_06_Deep_Fake_Prompts.txt).

---

## 🚧 Challenges & Learnings

### **Challenges Faced**
- Explored multiple tools but finalized Gemini Veo 3 due to best free access & features.
- 3-hour clip generation cooldown caused delays.
- 8-second video limit → had to split and merge clips carefully.
- Gemini Veo didn’t allow direct dataset uploads → manually integrated insights.
- Early outputs lacked realism and required iterative refinements.

### **Key Learnings**
- Context-rich prompts and accurate stats = **realistic ESPN-style videos**.
- Using the Syracuse coach image improved lip-sync and authenticity.
- Small details like **camera angles, lighting, crowd effects** drastically improved realism.
- Combining AI outputs with **CapCut editing** enhanced overall quality.

---

## 🎞️ Final Output
- **Video Duration:** ~25 seconds  
- **Style:** ESPN-style Syracuse Men’s Soccer interview  
- **Content:** Season recap → defensive strategy → motivational message  
- **Quality:** Dynamic visuals, smooth transitions, dataset-backed insights  

---

## 📂 How to Run
1. Review the **Task06_Gemini_Veo3_Prompts.txt** file for prompt references.
2. Generate clips in **Gemini Veo 3 Fast** using the provided prompts.
3. Import clips into **CapCut**.
4. Add transitions, captions and cover image.
5. Export the **final merged interview video**.

---

## 📌 Takeaway
This project highlights the potential of **AI-powered video generation** while showing that high-quality results require:
- Accurate dataset integration
- Strong prompt engineering
- Iterative refinements
- Post-production editing

