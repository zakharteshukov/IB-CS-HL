#!/usr/bin/env python3
"""
Process whisper transcription log and create formatted transcript
"""
import re
import sys

def process_log_file(log_path):
    """Extract transcription from log file and clean it"""
    with open(log_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Extract only timestamped lines (skip warnings and metadata)
    transcript_lines = []
    for line in lines:
        # Match timestamp format: [HH:MM:SS.mmm --> HH:MM:SS.mmm]  text
        match = re.match(r'\[(\d{2}:\d{2}:\d{2}\.\d{3})\s-->\s(\d{2}:\d{2}:\d{2}\.\d{3})\]\s+(.+)', line)
        if match:
            text = match.group(3).strip()
            # Skip single "You" entries (common false positives)
            if text != "You":
                transcript_lines.append(text)
    
    return transcript_lines

def create_original_transcript(transcript_lines, output_path):
    """Create original transcript without timestamps"""
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in transcript_lines:
            f.write(line + '\n')

def create_formatted_transcript(transcript_lines, output_path, week_num, topic):
    """Create formatted transcript with sections"""
    # Join all lines into continuous text
    full_text = ' '.join(transcript_lines)
    
    # Split into sentences (rough approximation)
    sentences = re.split(r'([.!?])\s+', full_text)
    # Rejoin sentences properly
    formatted_sentences = []
    for i in range(0, len(sentences)-1, 2):
        if i+1 < len(sentences):
            formatted_sentences.append(sentences[i] + sentences[i+1])
    if len(sentences) % 2 == 1:
        formatted_sentences.append(sentences[-1])
    
    # Write formatted transcript
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"IB COMPUTER SCIENCE HL - WEEK {week_num}\n")
        f.write(f"{topic}\n")
        f.write("Transcription - Formatted\n")
        f.write("\n")
        f.write("=" * 80 + "\n")
        f.write("CLASS INTRODUCTION & ADMINISTRATIVE MATTERS\n")
        f.write("=" * 80 + "\n")
        f.write("\n")
        
        # Write all text (we'll manually identify sections later if needed)
        current_section = []
        for sentence in formatted_sentences:
            sentence = sentence.strip()
            if sentence:
                current_section.append(sentence)
        
        # Write all content
        for sentence in current_section:
            f.write(sentence + "\n\n")

if __name__ == "__main__":
    log_file = "/Users/macbook/Downloads/mfs/education/SSIS/IB CS HL/recordings/logs/whisper-transcription-W1.log"
    original_output = "/Users/macbook/Downloads/mfs/education/SSIS/IB CS HL/recordings/transcripts/original/M2027_W1_Meet_Your_Teacher.txt"
    formatted_output = "/Users/macbook/Downloads/mfs/education/SSIS/IB CS HL/recordings/transcripts/formatted/M2027_W1_Meet_Your_Teacher - FORMATTED.txt"
    
    transcript_lines = process_log_file(log_file)
    create_original_transcript(transcript_lines, original_output)
    create_formatted_transcript(transcript_lines, formatted_output, "1", "Meet Your Teacher")
    
    print(f"Processed {len(transcript_lines)} transcript lines")
    print(f"Original transcript saved to: {original_output}")
    print(f"Formatted transcript saved to: {formatted_output}")

