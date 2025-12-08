#!/usr/bin/env python3
"""
Create properly formatted transcript for W5 with clear section separations
"""
import re

def read_original_transcript(file_path):
    """Read the original transcript"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def create_formatted_transcript(lines, output_path):
    """Create formatted transcript with clear sections"""
    
    # Join lines and split into paragraphs
    full_text = ' '.join(lines)
    
    # Split into sentences (rough approximation)
    sentences = re.split(r'([.!?])\s+', full_text)
    # Rejoin sentences properly
    formatted_sentences = []
    for i in range(0, len(sentences)-1, 2):
        if i+1 < len(sentences):
            formatted_sentences.append(sentences[i] + sentences[i+1])
    if len(sentences) % 2 == 1:
        formatted_sentences.append(sentences[-1])
    
    # Identify section boundaries based on content
    content = ' '.join(lines)
    
    # Find section markers
    sections = []
    current_section = []
    current_title = "CLASS INTRODUCTION & ADMINISTRATIVE MATTERS"
    
    # Keywords for section detection
    boolean_keywords = ['boolean', 'bullion', 'algebra', 'law', 'identity', 'null', 'complement', 
                       'domination', 'distributive', 'demorgan', 'absorption', 'simplification']
    kmap_keywords = ['k map', 'k-map', 'kmap', 'minterm', 'adjacent', 'pairing', 'sigma']
    logic_gate_keywords = ['logic gate', 'and gate', 'or gate', 'not gate', 'nand', 'xor', 'xnor']
    
    i = 0
    while i < len(formatted_sentences):
        sentence = formatted_sentences[i].strip()
        if not sentence:
            i += 1
            continue
            
        sentence_lower = sentence.lower()
        
        # Check for section transitions
        if i < 10:  # First few sentences are intro
            current_section.append(sentence)
        elif any(kw in sentence_lower for kw in boolean_keywords) and 'boolean' not in current_title.lower():
            if current_section:
                sections.append((current_title, current_section))
            current_title = "BOOLEAN ALGEBRA RULES & LAWS"
            current_section = [sentence]
        elif any(kw in sentence_lower for kw in kmap_keywords) and 'k map' not in current_title.lower():
            if current_section:
                sections.append((current_title, current_section))
            current_title = "K-MAPS (KARNAUGH MAPS) - SIMPLIFICATION"
            current_section = [sentence]
        elif any(kw in sentence_lower for kw in ['next week', 'thank you', 'bye', 'meet next']) and 'closing' not in current_title.lower():
            if current_section:
                sections.append((current_title, current_section))
            current_title = "CLOSING REMARKS & NEXT WEEK PREVIEW"
            current_section = [sentence]
        else:
            current_section.append(sentence)
        
        i += 1
    
    # Add last section
    if current_section:
        sections.append((current_title, current_section))
    
    # Write formatted transcript
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("IB COMPUTER SCIENCE HL - WEEK 5\n")
        f.write("A1.2.3-A1.2.5 - Logic Gates, Boolean Algebra & K-maps\n")
        f.write("Transcription - Formatted\n")
        f.write("\n")
        
        for title, content_list in sections:
            f.write("=" * 80 + "\n")
            f.write(title + "\n")
            f.write("=" * 80 + "\n")
            f.write("\n")
            
            # Write content with proper paragraph breaks
            paragraph = []
            for sentence in content_list:
                sentence = sentence.strip()
                if sentence:
                    paragraph.append(sentence)
                    # Break paragraph every 3-4 sentences or on natural breaks
                    if len(paragraph) >= 3 and (sentence.endswith('.') or sentence.endswith('?') or sentence.endswith('!')):
                        f.write(' '.join(paragraph) + "\n\n")
                        paragraph = []
            
            # Write remaining paragraph
            if paragraph:
                f.write(' '.join(paragraph) + "\n\n")

if __name__ == "__main__":
    original_file = "/Users/macbook/Downloads/mfs/education/SSIS/IB CS HL/recordings/transcripts/original/M2027_W5_A1.2.3-A1.2.5.txt"
    formatted_file = "/Users/macbook/Downloads/mfs/education/SSIS/IB CS HL/recordings/transcripts/formatted/M2027_W5_A1.2.3-A1.2.5 - FORMATTED.txt"
    
    lines = read_original_transcript(original_file)
    create_formatted_transcript(lines, formatted_file)
    
    print(f"Formatted transcript created: {formatted_file}")
