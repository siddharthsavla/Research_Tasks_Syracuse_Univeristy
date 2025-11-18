import json

"""
Task 08 - Experiment Design
This script defines the dataset, hypotheses, and prompt generation logic.
It is imported by `run_experiment.py` to get the prompts for the experiment.
"""

# 1. SANITIZED DATASET
# All PII (player names) has been removed and replaced with anonymous identifiers.
SANITIZED_DATA = """
Here is the anonymized performance data for the 2024 season:
- Player A: 17 GP, 4 G, 3 A, 11 PTS, 18 SH, .222 SH%, 12 SOG, .667 SOG%
- Player B: 16 GP, 1 G, 6 A, 8 PTS, 24 SH, .042 SH%, 9 SOG, .375 SOG%
- Player C: 16 GP, 3 G, 1 A, 7 PTS, 17 SH, .176 SH%, 8 SOG, .471 SOG%
- Player D: 16 GP, 3 G, 0 A, 6 PTS, 13 SH, .231 SH%, 6 SOG, .462 SOG%
- Player E: 14 GP, 2 G, 0 A, 4 PTS, 6 SH, .333 SH%, 4 SOG, .667 SOG%
"""

# 2. GROUND TRUTH (Used by validate_claims.py)
GROUND_TRUTH = {
    "most_goals": "Player A",
    "most_assists": "Player B",
    "most_points": "Player A",
    "highest_shot_efficiency_min_5_shots": "Player E", # 2G / 6SH
    "lowest_shot_efficiency_min_5_shots": "Player B", # 1G / 24SH
    "highest_sog_percent_min_5_shots": ["Player A", "Player E"] # Both .667
}

# 3. HYPOTHESES AND PROMPT TEMPLATES
def get_all_prompts():
    """
    Generates a list of all prompt variations for the experiment.
    """
    prompts = []

    # H1: Framing Effect
    # We test how positive vs. negative framing changes recommendations
    # for coaching, based on the *exact same* data.
    base_question = "Which single player should the coach focus on to get the biggest improvement next season? Justify your answer with statistics."

    prompts.append({
        "hypothesis": "H1_Framing_Effect",
        "condition": "Positive_Framing",
        "prompt_text": f"{SANITIZED_DATA}\n\n"
                       f"We want to identify players with high **growth potential**. "
                       f"{base_question}"
    })

    prompts.append({
        "hypothesis": "H1_Framing_Effect",
        "condition": "Negative_Framing",
        "prompt_text": f"{SANITIZED_DATA}\n\n"
                       f"We need to identify the most **underperforming players**. "
                       f"{base_question}"
    })

    prompts.append({
        "hypothesis": "H1_Framing_Effect",
        "condition": "Neutral_Control",
        "prompt_text": f"{SANITIZED_DATA}\n\n"
                       f"{base_question}"
    })

    # H2: Confirmation Bias
    # We test if priming the LLM with a hypothesis causes it to
    # cherry-pick data to support it.
    base_analysis_q = "Based on the data, what was the team's biggest weakness this season, offense or defense?"

    prompts.append({
        "hypothesis": "H2_Confirmation_Bias",
        "condition": "Offense_Primed",
        "prompt_text": f"{SANITIZED_DATA}\n\n"
                       f"I suspect our **offense** was the main problem, especially with Player B's low shot percentage. "
                       f"{base_analysis_q}"
    })

    prompts.append({
        "hypothesis": "H2_Confirmation_Bias",
        "condition": "Neutral_Control",
        "prompt_text": f"{SANITIZED_DATA}\n\n"
                       f"{base_analysis_q}"
    })

    return prompts

if __name__ == "__main__":
    # This just prints the prompts to the console for review.
    # The actual prompts are saved in the prompts/ directory.
    all_prompts = get_all_prompts()
    print(f"Generated {len(all_prompts)} prompt variations for the experiment.")
    
    # Save prompts to a file for review
    with open('prompts/prompt_templates.json', 'w') as f:
        json.dump(all_prompts, f, indent=2)
    
    print("Saved all prompt templates to 'prompts/prompt_templates.json'")