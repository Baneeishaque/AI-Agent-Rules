#!/usr/bin/env python3
import os
import re
import sys
from collections import defaultdict

# Configuration
RULES_DIR = "."
TEMPLATES_DIR = "templates"
README_TEMPLATE = os.path.join(TEMPLATES_DIR, "README.md.template")
INDEX_TEMPLATE = os.path.join(TEMPLATES_DIR, "agent-rules.md.template")
README_OUTPUT = "README.md"
INDEX_OUTPUT = "agent-rules.md"

def parse_metadata(content):
    """Extracts metadata from the markdown content."""
    meta_match = re.search(r"^<!--\s*(.*?)\s*-->", content, re.DOTALL)
    if not meta_match:
        return None
    
    meta_text = meta_match.group(1)
    metadata = {}
    for line in meta_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()
    return metadata

def get_rule_files():
    """Retrieves all *-rules.md files in the current directory."""
    return [f for f in os.listdir(RULES_DIR) if f.endswith("-rules.md") and f != "agent-rules.md" and f != "README.md"]

def generate_readme_tables(rules_by_category):
    """Generates the markdown tables for README.md."""
    output = []
    
    # Sort categories alphabetically ASC
    sorted_categories = sorted(rules_by_category.keys())
    
    for category in sorted_categories:
        rules = rules_by_category[category]
        if not rules:
            continue
            
        output.append(f"### {category}")
        output.append("| Rule File | Purpose |")
        output.append("|-----------|---------|")
        
        # Sort rules by filename
        sorted_rules = sorted(rules, key=lambda x: x['filename'])
        
        for rule in sorted_rules:
            link = f"[`{rule['filename']}`](./{rule['filename']})"
            output.append(f"| {link} | {rule['description']} |")
        
        output.append("") # Empty line after table
        
    return "\n".join(output)

def generate_index_table(all_rules):
    """Generates the flat table for agent-rules.md."""
    output = []
    output.append("| Rule Domain | File Name | Description |")
    output.append("|---|---|---|")
    
    # Sort by Title (Rule Domain)
    sorted_rules = sorted(all_rules, key=lambda x: x['title'])
    
    for rule in sorted_rules:
        link = f"[{rule['filename']}](./{rule['filename']})"
        output.append(f"| {rule['title']} | {link} | {rule['description']} |")
        
    return "\n".join(output)

def main():
    rule_files = get_rule_files()
    valid_rules = []
    errors = []

    print(f"🔍 Scanning {len(rule_files)} rule files...")

    for filename in rule_files:
        filepath = os.path.join(RULES_DIR, filename)
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            
            metadata = parse_metadata(content)
            
            missing_fields = []
            if not metadata:
                missing_fields = ["metadata_block"]
            else:
                if 'title' not in metadata: missing_fields.append('title')
                if 'description' not in metadata: missing_fields.append('description')
                if 'category' not in metadata: missing_fields.append('category')

            if missing_fields:
                errors.append({"file": filename, "missing": missing_fields})
            else:
                metadata['filename'] = filename
                valid_rules.append(metadata)

        except Exception as e:
            errors.append({"file": filename, "missing": [f"READ_ERROR: {str(e)}"]})

    # Validation Check
    if errors:
        print("\n❌ Validation Failed! The following files have missing metadata:")
        print(f"{'File':<40} | {'Missing Fields'}")
        print("-" * 60)
        for error in errors:
            print(f"{error['file']:<40} | {', '.join(error['missing'])}")
        print("\nPlease add the missing metadata to these files and retry.")
        sys.exit(1)

    print("✅ All files validated successfully.")

    # Group by Category for README
    rules_by_category = defaultdict(list)
    for rule in valid_rules:
        rules_by_category[rule['category']].append(rule)

    # Generate Content
    readme_content_block = generate_readme_tables(rules_by_category)
    index_content_block = generate_index_table(valid_rules)

    # Write README.md
    try:
        with open(README_TEMPLATE, 'r') as f:
            readme_template = f.read()
        
        new_readme = readme_template.replace("<!-- RULES_README -->", readme_content_block)
        
        with open(README_OUTPUT, 'w') as f:
            f.write(new_readme)
        print(f"📄 Generated {README_OUTPUT}")
        
    except FileNotFoundError:
        print(f"❌ Template not found: {README_TEMPLATE}")
        sys.exit(1)

    # Write agent-rules.md
    try:
        with open(INDEX_TEMPLATE, 'r') as f:
            index_template = f.read()
            
        new_index = index_template.replace("<!-- RULES_INDEX -->", index_content_block)
        
        with open(INDEX_OUTPUT, 'w') as f:
            f.write(new_index)
        print(f"📄 Generated {INDEX_OUTPUT}")

    except FileNotFoundError:
        print(f"❌ Template not found: {INDEX_TEMPLATE}")
        sys.exit(1)

if __name__ == "__main__":
    main()
