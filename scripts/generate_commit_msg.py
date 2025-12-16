#!/usr/bin/env python3
import os
import subprocess
import google.generativeai as genai

import sys
import argparse

def get_staged_diff(files=None):
    """Gets the diff of staged changes."""
    cmd = ["git", "diff", "--cached"]
    if files:
        cmd.extend(files)
        
    result = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True, 
        check=True
    )
    return result.stdout

def get_commit_rules():
    """Reads the commit message rules."""
    rules_path = "Git-Commit-Message-rules.md"
    if os.path.exists(rules_path):
        with open(rules_path, "r") as f:
            return f.read()
    else:
        # High-Fidelity Fallback based on specific user requirements
        return """
        STRICT FORMATTING RULES:
        1. Header: type(scope): title
           - "type" must be one of: feat, fix, docs, style, refactor, test, chore
           - "scope" is optional but recommended
           - "title" must be < 50 chars, IMPERATIVE mood (e.g., "add" not "added"), NO trailing period.
        
        2. Body:
           - Must generally be separated from header by a blank line.
           - Use BULLET POINTS (-) for all details.
           - Wrap text at 72 characters.
           - Explain WHAT changed and WHY.
           - Do NOT repeat the title.
        
        3. NO Markdown formatting (no bold/italics/backticks).
        """

def generate_message(diff, rules):
    """Generates a commit message using Gemini."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        # Fail silently or verbose depending on need, but for CI script we print error
        print("Error: GEMINI_API_KEY not set.")
        return None

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-pro')

    prompt = f"""
    You are a strict Release Manager. Write a git commit message.
    
    RULES (Adhere strictly):
    {rules}

    CHANGES TO COMMIT:
    ```
    {diff}
    ```

    Output ONLY the raw commit message. No code blocks.
    """

    try:
        response = model.generate_content(prompt)
        message = response.text.replace("```", "").strip()
        return message
    except Exception as e:
        # Don't crash the pipeline, just return None to trigger fallback
        print(f"Gemini API Error: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="*", help="Specific files to diff")
    args = parser.parse_args()

    diff = get_staged_diff(args.files)
    if not diff.strip():
        # No changes in the targeted files
        print("No staged changes.")
        exit(0)

    rules = get_commit_rules()
    message = generate_message(diff, rules)

    if message:
        print(message)
    else:
        print("docs: sync rule indices (AI generation failed)")
