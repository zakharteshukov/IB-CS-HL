#!/usr/bin/env python3
"""
Add lesson outline to formatted transcript files
"""
import re
import os

def extract_sections(file_path):
    """Extract section headings from a formatted transcript file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all section headings (text between separator lines)
    # Pattern: ================ followed by text followed by ================
    pattern = r'={80,}\s*\n([^=]+?)\s*\n={80,}'
    matches = re.findall(pattern, content, re.MULTILINE)
    
    sections = []
    for match in matches:
        section = match.strip()
        if section and section not in sections:
            sections.append(section)
    
    return sections

def add_outline(file_path, sections):
    """Add outline to the top of the transcript file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find where the header ends (after "Transcription - Formatted")
    header_end = 0
    for i, line in enumerate(lines):
        if "Transcription - Formatted" in line:
            header_end = i + 1
            break
    
    # Create outline
    outline_lines = [
        "\n",
        "=" * 80 + "\n",
        "LESSON OUTLINE\n",
        "=" * 80 + "\n",
        "\n"
    ]
    
    # Add numbered sections
    for i, section in enumerate(sections, 1):
        outline_lines.append(f"{i}. {section}\n")
    
    outline_lines.append("\n")
    outline_lines.append("=" * 80 + "\n")
    outline_lines.append("\n")
    
    # Insert outline after header
    new_lines = lines[:header_end] + outline_lines + lines[header_end:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Added outline with {len(sections)} sections to {os.path.basename(file_path)}")

if __name__ == "__main__":
    transcripts_dir = "/Users/macbook/Downloads/mfs/education/SSIS/IB CS HL/recordings/transcripts/formatted"
    
    # Get all formatted transcript files
    files = [f for f in os.listdir(transcripts_dir) if f.endswith("FORMATTED.txt")]
    files.sort()
    
    for filename in files:
        file_path = os.path.join(transcripts_dir, filename)
        sections = extract_sections(file_path)
        if sections:
            add_outline(file_path, sections)
        else:
            print(f"No sections found in {filename}")
