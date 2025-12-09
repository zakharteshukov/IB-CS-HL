#!/usr/bin/env python3
"""
Interactive script to convert a single file to markdown format.
Prompts user for file path, converts it, saves in same directory, and deletes original.
"""

import os
import re
from pathlib import Path


def convert_txt_to_markdown(input_file, output_file):
    """Convert a transcript .txt file to markdown format."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    markdown_lines = []
    i = 0
    skip_next_separator = False
    
    # Process header (first few lines)
    while i < len(lines) and i < 5:
        line = lines[i].strip()
        if line and not line.startswith('='):
            if i == 0:
                # First line becomes main title
                markdown_lines.append(f"# {line}\n\n")
            elif i == 1:
                # Second line becomes subtitle
                markdown_lines.append(f"## {line}\n\n")
            elif i == 2 and "Transcription" in line:
                # Make "Transcription - Formatted" italic
                markdown_lines.append(f"*{line}*\n\n")
            elif line:
                markdown_lines.append(f"{line}\n")
        elif not line:
            markdown_lines.append("\n")
        i += 1
    
    # Process the rest of the file
    while i < len(lines):
        line = lines[i]
        original_line = line
        line_stripped = line.strip()
        
        # Check for separator lines (===)
        if re.match(r'^=+$', line_stripped):
            # Look ahead to find the header text after separator
            j = i + 1
            # Skip empty lines after separator
            while j < len(lines) and not lines[j].strip():
                j += 1
            
            if j < len(lines):
                header_line = lines[j].strip()
                # Check if it's actually a header (not another separator)
                if header_line and not re.match(r'^=+$', header_line):
                    # Headers are typically:
                    # - Short (less than 80 chars)
                    # - All caps or title case
                    # - Don't contain sentence-ending punctuation in the middle
                    # - Don't start with lowercase letters
                    is_likely_header = (
                        len(header_line) < 80 and
                        not re.search(r'[.!?]\s+[a-z]', header_line) and  # No sentence breaks
                        (header_line.isupper() or 
                         (header_line[0].isupper() and not header_line.startswith(('This ', 'So ', 'Okay ', 'All ', 'The ', 'A ', 'An '))))
                    )
                    
                    if is_likely_header:
                        markdown_lines.append(f"\n## {header_line}\n\n")
                        i = j + 1  # Skip separator, empty lines, and header
                        continue
            
            # Just a separator with no clear header, skip it
            i += 1
            continue
        
        # Skip empty lines that are just between sections
        if not line_stripped:
            # Check context: if surrounded by separators or at start/end, skip
            prev_non_empty = i - 1
            while prev_non_empty >= 0 and not lines[prev_non_empty].strip():
                prev_non_empty -= 1
            
            next_non_empty = i + 1
            while next_non_empty < len(lines) and not lines[next_non_empty].strip():
                next_non_empty += 1
            
            # If previous was separator or next is separator, skip this empty line
            if (prev_non_empty >= 0 and re.match(r'^=+$', lines[prev_non_empty].strip())) or \
               (next_non_empty < len(lines) and re.match(r'^=+$', lines[next_non_empty].strip())):
                i += 1
                continue
            
            # Otherwise, keep a single empty line
            if not markdown_lines or markdown_lines[-1] != "\n":
                markdown_lines.append("\n")
            i += 1
            continue
        
        # Check for numbered lists (lines starting with numbers followed by period)
        if re.match(r'^\d+\.', line_stripped):
            # Count leading spaces for indentation
            leading_spaces = len(line) - len(line.lstrip())
            indent_markdown = '  ' * (leading_spaces // 2)
            markdown_lines.append(f"{indent_markdown}{line_stripped}\n")
        
        # Check for bullet points (lines starting with - or *)
        elif re.match(r'^[\s]*[-*]', line_stripped):
            # Count leading spaces for indentation
            leading_spaces = len(line) - len(line.lstrip())
            indent_markdown = '  ' * (leading_spaces // 2)
            # Ensure it starts with - for markdown
            bullet_line = line_stripped
            if bullet_line.startswith('*'):
                bullet_line = '-' + bullet_line[1:]
            markdown_lines.append(f"{indent_markdown}{bullet_line}\n")
        
        # Regular content lines
        else:
            markdown_lines.append(f"{line}\n")
        
        i += 1
    
    # Clean up excessive blank lines (more than 2 consecutive)
    cleaned_lines = []
    blank_count = 0
    for line in markdown_lines:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 2:
                cleaned_lines.append(line)
        else:
            blank_count = 0
            cleaned_lines.append(line)
    
    # Write the markdown file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)


def main():
    """Main function to prompt user and convert file."""
    
    # Prompt user for file path
    file_path = input("Enter the path to the file you want to convert: ").strip()
    
    # Remove quotes if user included them
    file_path = file_path.strip('"\'')
    
    # Convert to Path object
    input_file = Path(file_path)
    
    # Validate file exists
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        return
    
    if not input_file.is_file():
        print(f"Error: Path is not a file: {input_file}")
        return
    
    # Get the directory and create output filename
    file_dir = input_file.parent
    file_stem = input_file.stem
    output_file = file_dir / f"{file_stem}.md"
    
    # Check if output file already exists
    if output_file.exists():
        response = input(f"Warning: {output_file.name} already exists. Overwrite? (y/n): ").strip().lower()
        if response != 'y':
            print("Conversion cancelled.")
            return
    
    try:
        # Convert the file
        print(f"Converting {input_file.name} to markdown...")
        convert_txt_to_markdown(input_file, output_file)
        
        # Delete the original file
        print(f"Deleting original file: {input_file.name}")
        input_file.unlink()
        
        print(f"✓ Successfully converted and saved: {output_file}")
        print(f"✓ Original file deleted: {input_file.name}")
        
    except Exception as e:
        print(f"Error during conversion: {e}")
        # If output file was created but there was an error, clean it up
        if output_file.exists():
            output_file.unlink()
        return


if __name__ == '__main__':
    main()
