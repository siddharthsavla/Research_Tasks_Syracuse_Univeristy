import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

"""
Task 08 - Analyze Bias
This script:
1. Loads the raw JSON results from `run_experiment.py`.
2. Performs quantitative analysis (sentiment, counts).
3. Runs statistical tests (chi-square).
4. Saves analysis outputs (tables, charts) to the `analysis/` directory.
"""

RESULTS_FILE = 'results/raw_responses.json'
ANALYSIS_DIR = 'analysis'

def analyze_framing_effect(df):
    """
    Analyzes H1: Framing Effect.
    Looks at sentiment and player recommendations.
    """
    print("Analyzing H1: Framing Effect...")
    
    # Filter for this hypothesis
    h1_df = df[df['hypothesis'] == 'H1_Framing_Effect'].copy()
    if h1_df.empty:
        print("No data found for H1_Framing_Effect.")
        return

    # 1. Quantitative Sentiment Analysis
    analyzer = SentimentIntensityAnalyzer()
    h1_df['sentiment_compound'] = h1_df['response_text'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    
    sentiment_summary = h1_df.groupby('condition')['sentiment_compound'].mean()
    print("\n--- Sentiment Summary (Compound Score) ---")
    print(sentiment_summary)
    
    # 2. Quantitative Recommendation Counting
    # This is a simple example; a real-world case would use regex or NLP
    def find_player_recommendation(text):
        text_lower = text.lower()
        if "player a" in text_lower: return "Player A"
        if "player b" in text_lower: return "Player B"
        if "player c" in text_lower: return "Player C"
        if "player d" in text_lower: return "Player D"
        if "player e" in text_lower: return "Player E"
        return "None"

    h1_df['recommended_player'] = h1_df['response_text'].apply(find_player_recommendation)
    
    # Create a contingency table
    contingency_table = pd.crosstab(h1_df['recommended_player'], h1_df['condition'])
    print("\n--- Player Recommendation Contingency Table ---")
    print(contingency_table)

    # 3. Statistical Test (Chi-Square)
    try:
        chi2, p_value, _, _ = chi2_contingency(contingency_table)
        print(f"\nChi-Square Test: chi2={chi2:.2f}, p-value={p_value:.4f}")
        if p_value < 0.05:
            print("Result: The difference in recommendations is STATISTICALLY SIGNIFICANT.")
        else:
            print("Result: The difference in recommendations is NOT statistically significant.")
    except ValueError as e:
        print(f"Could not run Chi-Square test (likely not enough data): {e}")

    # 4. Save Visualization
    ax = sentiment_summary.plot(kind='bar',
                                title='Average Sentiment by Prompt Condition',
                                rot=0,
                                color=['green', 'red', 'blue'])
    ax.set_ylabel('Avg. Compound Sentiment Score')
    ax.set_xlabel('Prompt Condition')
    plt.tight_layout()
    fig_path = os.path.join(ANALYSIS_DIR, 'framing_effect_visualization.png')
    plt.savefig(fig_path)
    print(f"Saved sentiment visualization to '{fig_path}'")
    
    # Save summary table
    table_path = os.path.join(ANALYSIS_DIR, 'bias_summary_table.csv')
    contingency_table.to_csv(table_path)
    print(f"Saved summary table to '{table_path}'")


def main():
    try:
        with open(RESULTS_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: Results file not found at '{RESULTS_FILE}'.")
        print("Please run `run_experiment.py` first.")
        return
    except json.JSONDecodeError:
        print(f"ERROR: Results file '{RESULTS_FILE}' is empty or corrupted.")
        return

    if not data:
        print("Results file is empty. No analysis to perform.")
        return

    df = pd.DataFrame(data)
    
    # Ensure analysis directory exists
    os.makedirs(ANALYSIS_DIR, exist_ok=True)
    
    analyze_framing_effect(df)
    # TODO: Add analysis for H2: Confirmation Bias

    print("\nAnalysis complete.")

if __name__ == "__main__":
    main()