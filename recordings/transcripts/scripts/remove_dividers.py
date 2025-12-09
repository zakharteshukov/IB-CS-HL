#!/usr/bin/env python3
"""
Script to remove markdown dividers (---) from all markdown transcript files.
"""

import os
from pathlib import Path

def remove_dividers(input_file):
    """Remove markdown dividers (---) from a markdown file."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Remove lines that are just "---" (with optional whitespace)
    cleaned_lines = []
    for line in lines:
        if line.strip() == '---':
            continue  # Skip divider lines
        cleaned_lines.append(line)
    
    # Write back to file
    with open(input_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
    
    print(f"✓ Removed dividers from: {input_file.name}")


def main():
    """Main function to process all markdown transcript files."""
    
    # Get the script directory and find the formatted directory
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    formatted_dir = base_dir / 'formatted'
    
    if not formatted_dir.exists():
        print(f"Error: Directory not found: {formatted_dir}")
        return
    
    # Find all .md files
    md_files = list(formatted_dir.glob('*.md'))
    
    if not md_files:
        print(f"No .md files found in {formatted_dir}")
        return
    
    print(f"Found {len(md_files)} markdown file(s) to process...\n")
    
    # Process each file
    for md_file in md_files:
        remove_dividers(md_file)
    
    print(f"\n✓ Complete! Processed {len(md_files)} file(s).")


if __name__ == '__main__':
    main()

