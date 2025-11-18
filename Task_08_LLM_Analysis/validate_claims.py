import json
import pandas as pd
from experiment_design import GROUND_TRUTH

"""
Task 08 - Validate LLM Claims
This script:
1. Loads the raw JSON results.
2. Defines the "ground truth" (imported from experiment_design).
3. Checks LLM responses for factual claims.
4. Compares claims against the ground truth to find "fabrications".
"""

RESULTS_FILE = 'results/raw_responses.json'

def validate_responses(all_responses):
    """
    Iterates through responses and checks for fabricated claims.
    This is a simple example. A robust solution would use regex or NER.
    """
    print("Validating LLM claims against Ground Truth...")
    
    fabrication_count = 0
    total_responses = len(all_responses)
    fabrications_found = []

    for i, response in enumerate(all_responses):
        text = response['response_text'].lower()
        
        # Example check: Did the LLM claim the wrong "most efficient" player?
        # Ground truth is Player E.
        if "most efficient" in text or "highest shot efficiency" in text:
            if "player a" in text or "player b" in text or "player c" in text or "player d" in text:
                if "player e" not in text:
                    # The LLM made a claim about efficiency and got