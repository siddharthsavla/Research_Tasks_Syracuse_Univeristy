import os
import json
import time
from datetime import datetime
import google.generativeai as genai
import anthropic
from experiment_design import get_all_prompts

"""
Task 08 - Run Experiment
This script:
1. Imports the generated prompts.
2. Queries multiple LLM APIs for each prompt.
3. Runs each prompt N times to get multiple samples.
4. Saves all data in a structured log file.
"""

# --- CONFIGURATION ---
SAMPLES_PER_PROMPT = 5  # Get 5 responses per prompt
RESULTS_FILE = 'results/raw_responses.json'
MODELS_TO_TEST = {
    'gemini': 'gemini-1.5-pro-latest',
    'claude': 'claude-3-haiku-20240307' # Using Haiku for speed/cost
}

# --- API CLIENTS ---
try:
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    gemini_model = genai.GenerativeModel(MODELS_TO_TEST['gemini'])
except Exception as e:
    print(f"Could not configure Gemini client. Set GEMINI_API_KEY. Error: {e}")
    gemini_model = None

try:
    claude_client = anthropic.Anthropic(api_key=os.environ.get("CLAUDE_API_KEY"))
except Exception as e:
    print(f"Could not configure Anthropic client. Set CLAUDE_API_KEY. Error: {e}")
    claude_client = None


def query_gemini(prompt_text):
    """Sends a prompt to the Gemini API and returns the text response."""
    if not gemini_model:
        return "ERROR: Gemini client not initialized."
    try:
        response = gemini_model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        return f"ERROR: Gemini API call failed: {e}"

def query_claude(prompt_text):
    """Sends a prompt to the Claude API and returns the text response."""
    if not claude_client:
        return "ERROR: Claude client not initialized."
    try:
        message = claude_client.messages.create(
            model=MODELS_TO_TEST['claude'],
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt_text}
            ]
        )
        return message.content[0].text
    except Exception as e:
        return f"ERROR: Claude API call failed: {e}"

def run_experiment():
    """
    Main function to run the full bias detection experiment.
    """
    print("Starting Task 08 Bias Detection Experiment...")
    all_prompts = get_all_prompts()
    all_results = []
    
    total_queries = len(all_prompts) * SAMPLES_PER_PROMPT * len(MODELS_TO_TEST)
    print(f"Total queries to run: {total_queries}")
    
    query_count = 0
    for prompt in all_prompts:
        for i in range(SAMPLES_PER_PROMPT):
            # Query Gemini
            if gemini_model:
                query_count += 1
                print(f"Running Query {query_count}/{total_queries} (Gemini, Sample {i+1}, {prompt['hypothesis']})...")
                response_text = query_gemini(prompt['prompt_text'])
                
                all_results.append({
                    "timestamp": datetime.now().isoformat(),
                    "model_provider": "google",
                    "model_version": MODELS_TO_TEST['gemini'],
                    "sample_num": i + 1,
                    "hypothesis": prompt['hypothesis'],
                    "condition": prompt['condition'],
                    "prompt_text": prompt['prompt_text'],
                    "response_text": response_text
                })
                time.sleep(1) # Basic rate limiting

            # Query Claude
            if claude_client:
                query_count += 1
                print(f"Running Query {query_count}/{total_queries} (Claude, Sample {i+1}, {prompt['hypothesis']})...")
                response_text = query_claude(prompt['prompt_text'])

                all_results.append({
                    "timestamp": datetime.now().isoformat(),
                    "model_provider": "anthropic",
                    "model_version": MODELS_TO_TEST['claude'],
                    "sample_num": i + 1,
                    "hypothesis": prompt['hypothesis'],
                    "condition": prompt['condition'],
                    "prompt_text": prompt['prompt_text'],
                    "response_text": response_text
                })
                time.sleep(1) # Basic rate limiting
    
    # Save all results to the structured log file
    os.makedirs('results', exist_ok=True)
    with open(RESULTS_FILE, 'w') as f:
        json.dump(all_results, f, indent=2)

    print(f"\nExperiment complete. All {len(all_results)} responses saved to {RESULTS_FILE}")

if __name__ == "__main__":
    if not gemini_model and not claude_client:
        print("ERROR: No LLM clients are configured. Set API keys to run the experiment.")
    else:
        run_experiment()