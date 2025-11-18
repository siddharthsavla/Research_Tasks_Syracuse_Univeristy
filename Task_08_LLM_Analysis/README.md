# Task 08 - Bias Detection in LLM Data Narratives

## 1. Project Overview

This repository contains the full submission for **Research Task 8: Bias Detection in LLM Data Narratives**. The objective of this project was to design and execute a controlled experiment to detect potential biases (e.g., framing effects, confirmation bias) in LLM-generated data narratives.

The experiment used a sanitized version of the Syracuse Men's Soccer 2024 dataset (from Task 5). We tested multiple hypotheses by providing LLMs (Gemini and Claude) with minimally different prompts and analyzing the resulting narratives for statistical and qualitative differences.

This repository includes all code, analysis, and documentation required to reproduce the experiment.

## 2. Repository Structure

Task_08_Bias_Detection/ ├── .gitignore ├── README.md ├── REPORT.md ├── requirements.txt ├── experiment_design.py ├── run_experiment.py ├── analyze_bias.py ├── validate_claims.py ├── prompts/ │ └── prompt_templates.json ├── results/ │ ├── .gitkeep │ └── raw_responses_EXAMPLE.json └── analysis/ ├── .gitkeep ├── bias_summary_table.csv └── framing_effect_visualization.png

## 3. How to Reproduce the Experiment

To reproduce this experiment, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[YourUsername]/Task_08_Bias_Detection.git
    cd Task_08_Bias_Detection
    ```

2.  **Set up Environment:**
    Create a Python virtual environment and install the required libraries.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Set API Keys:**
    The `run_experiment.py` script requires API keys for the LLMs you are testing. Set them as environment variables:
    ```bash
    export GEMINI_API_KEY="your_api_key_here"
    export CLAUDE_API_KEY="your_api_key_here"
    ```

4.  **Run the Experiment Pipeline:**
    Execute the scripts in the following order:

    * **Step 1: Generate Prompts (Optional - for review)**
        This script contains the functions that `run_experiment.py` imports to generate prompts.
        ```bash
        python experiment_design.py
        ```

    * **Step 2: Run the Experiment (Data Collection)**
        This will query the LLM APIs and save all responses to `results/raw_responses.json`.
        ```bash
        python run_experiment.py
        ```

    * **Step 3: Analyze Results**
        This will load the raw results and generate the summary tables and visualizations in the `analysis/` directory.
        ```bash
        python analyze_bias.py
        ```

    * **Step 4: Validate LLM Claims**
        This will check the generated responses against the ground-truth data.
        ```bash
        python validate_claims.py
        ```

5.  **Review the Final Report:**
    All findings are synthesized in `REPORT.md`.