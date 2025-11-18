# Bias Detection in LLM Data Narratives: Final Report

**Task:** Research Task 08  
**Author:** Siddharth Savla  
**Date:** November 15, 2025  

## 1. Executive Summary (300 Words)

This report details the findings of a controlled experiment to detect bias in LLM-generated data narratives. Using the anonymized 2024 Syracuse Men's Soccer dataset, we tested how **framing effects** and **confirmation bias** impact the analytical outputs of two leading LLMs: Google's Gemini and Anthropic's Claude.

Our experiment confirms that **bias is clearly present and statistically significant**. We found that **framing effects** were the most prominent bias; prompts using negative language ("struggling players") caused both LLMs to recommend different players and use significantly more negative language than identical prompts with positive framing ("developing players").

We also found evidence of **confirmation bias**. When primed with a (false) hypothesis, the LLMs were more likely to "find" supporting evidence in the data, often by cherry-picking specific statistics or, in some cases, fabricating claims that were not supported by the ground-truth data.

The key takeaway is that LLMs are highly susceptible to the user's framing. The same dataset can produce contradictory recommendations based on the phrasing of the query. This highlights a critical vulnerability in using LLMs for objective data analysis. We propose mitigation strategies, such as "bias-reducing" prompt wrappers, to improve the objectivity of LLM-generated insights.

## 2. Methodology

### Experimental Design

1.  **Dataset:** Anonymized 2024 Syracuse Men's Soccer dataset. All player names were replaced with identifiers (e.g., "Player A," "Player B") to prevent PII leakage.
2.  **LLMs Tested:** Google Gemini and Anthropic Claude (via SU Enterprise License).
3.  **Ground Truth:** A set of objective statistical facts was established using `validate_claims.py` *before* the experiment (e.g., "Player C had the highest shot conversion rate").
4.  **Hypotheses:**
    * **H1 (Framing Effect):** Prompts using negative framing (e.g., "struggling") will result in different player recommendations and more negative sentiment than prompts with positive framing (e.g., "developing"), even with identical data.
    * **H2 (Confirmation Bias):** Prompts that suggest a hypothesis (e.g., "Our defense seems to be the main problem, can you find supporting data?") will cause the LLM to selectively focus on defensive statistics and ignore contrary offensive data.
5.  **Data Collection:** We ran each prompt 5 times per LLM to account for randomness (temperature). All prompts, raw responses, models, and timestamps were logged in `results/raw_responses.json`.

### Analysis Approach

1.  **Quantitative:** We parsed the JSON results using `analyze_bias.py`. We ran sentiment analysis on each response and used a chi-square test to determine if the differences in player recommendations between prompt conditions were statistically significant.
2.  **Qualitative:** We manually reviewed responses for patterns in language, cherry-picked statistics, and contradictions.
3.  **Validation:** We used `validate_claims.py` to compare every factual claim in the LLM responses against the ground-truth data to calculate a "fabrication rate" for each condition.

## 3. Results

### H1: Framing Effect (Significant)

Our analysis confirmed a strong framing effect.

* **Quantitative:** The choice of player recommended for coaching was statistically dependent on the prompt's framing (positive vs. negative). With the "developing" prompt, Player A (high potential, low current output) was recommended 80% of the time. With the "struggling" prompt, Player B (high output, high error rate) was recommended 90% of the time. A chi-square test confirms this difference is not due to chance (p < 0.01).
* **Qualitative:** Sentiment in the "struggling" prompt responses was, on average, 55% more negative than in the "developing" prompt responses.
* **Visualization:** See `analysis/framing_effect_visualization.png`.

### H2: Confirmation Bias (Present)

We found clear evidence of confirmation bias.

* **Quantitative:** When primed with the "defense is the problem" hypothesis, 100% of responses (both models) focused their analysis *exclusively* on defensive metrics, ignoring the fact that offensive conversion rates were also below average.
* **Qualitative:** In this condition, Gemini fabricated a statistic, claiming "defensive errors led to goals in 40% of games," a fact not present in the dataset. This "fabrication rate" was 0% in the neutral control prompt. The LLM "invented" data to support the user's primed hypothesis.

## 4. Bias Catalogue

| Bias Detected | Severity | Description |
| :--- | :--- | :--- |
| **Framing Effect** | **High** | The LLM's recommendations and sentiment are dictated by the positive/negative framing of the user's prompt, not just the data. |
| **Confirmation Bias** | **High** | The LLM will actively try to confirm a user's stated hypothesis, even if it means cherry-picking data or fabricating new "facts." |
| **Selection Bias** | **Medium** | The LLM tends to focus on the first few players or statistics mentioned in the prompt (primacy bias) and often ignores data points listed later. |

## 5. Mitigation Strategies

1.  **"Role-Based" Priming:** Instead of a simple prompt, prime the LLM with a role: `"You are an objective, unbiased data scientist. Your task is to look at all the data and provide the most statistically sound recommendation. Ignore any sentiment in my prompt."`
2.  **Ask for Contradictions:** Actively ask the LLM to challenge the premise: `"Based on this data, find evidence that *supports* my hypothesis AND evidence that *contradicts* it."`
3.  **Chain-of-Thought Validation:** Force the LLM to show its work: `"First, list the raw statistics for Player A. Second, list the raw statistics for Player B. Third, explain your recommendation based *only* on those statistics."`

## 6. Limitations

* **Model Scope:** This experiment was limited to Gemini and Claude. These biases may differ in severity or nature on other models (e.g., GPT-4).
* **Data Scope:** The dataset was small. Biases may be amplified or reduced with larger, more complex datasets.
* **Demographic Bias:** We could not test for demographic bias (e.g., based on nationality, class) as our dataset was anonymized and lacked this information. This remains a critical area for future research.