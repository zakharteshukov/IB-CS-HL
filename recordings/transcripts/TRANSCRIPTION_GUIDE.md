# Transcription Guide

This guide explains how to transcribe video files using OpenAI Whisper.

## Prerequisites

- OpenAI Whisper installed (via pipx or pip)
- Video files in `.mp4` format

## Folder Structure

```
recordings/
├── videos/                    # Source video files (.mp4)
├── transcripts/
│   ├── original/             # Raw, unformatted transcripts from Whisper
│   └── formatted/           # Manually formatted and cleaned transcripts
└── logs/                     # Transcription logs (auto-generated)
```

## Step-by-Step Transcription Process

### 1. Navigate to the Recordings Directory

```bash
cd recordings
```

### 2. Run Whisper Transcription

Use the following command to transcribe a video file:

```bash
whisper videos/<video_filename>.mp4 \
  --output_dir transcripts/original \
  --language en \
  --model base \
  --verbose true
```

**Command Options:**
- `--output_dir transcripts/original`: Output directory for the transcript
- `--language en`: Specify English language (optional, Whisper can auto-detect)
- `--model base`: Model size (options: tiny, base, small, medium, large)
  - `tiny`: Fastest, least accurate
  - `base`: Good balance (default)
  - `small`: Better accuracy
  - `medium`: High accuracy
  - `large`: Best accuracy, slowest
- `--verbose true`: Show detailed progress

**Example:**
```bash
whisper videos/M2027_W8_B1.1.1.mp4 \
  --output_dir transcripts/original \
  --language en \
  --model base
```

### 3. Check the Output

After transcription completes:
- The transcript will be saved in `transcripts/original/` as a `.txt` file
- A log file will be created in `logs/whisper-transcription-<identifier>.log`
- The transcript will contain timestamps by default

### 4. Remove Timestamps (Optional)

If you want to remove timestamps from the raw transcript, you can use:

```bash
# Using sed (macOS/Linux)
sed 's/\[.*\]//g' transcripts/original/<filename>.txt > transcripts/original/<filename>_clean.txt
```

Or manually edit the file to remove timestamp markers like `[00:00.000 --> 00:02.000]`.

### 5. Format the Transcript

After getting the raw transcript:
1. Copy the file from `transcripts/original/` to `transcripts/formatted/`
2. Rename it with ` - FORMATTED.txt` suffix
3. Manually edit to:
   - Add headers and title
   - Organize into sections
   - Remove filler words and false starts
   - Improve readability
   - Add section dividers

**Example workflow:**
```bash
# Copy original to formatted folder
cp transcripts/original/M2027_W8_B1.1.1.txt \
   transcripts/formatted/M2027_W8_B1.1.1 - FORMATTED.txt

# Then manually edit the formatted version
```

## Quick Reference Commands

### Basic Transcription
```bash
whisper videos/<filename>.mp4 --output_dir transcripts/original
```

### Transcription with Specific Model
```bash
whisper videos/<filename>.mp4 \
  --output_dir transcripts/original \
  --model small
```

### Transcription with Language Detection
```bash
whisper videos/<filename>.mp4 \
  --output_dir transcripts/original \
  --language en
```

### Batch Transcription (Multiple Files)

For multiple files, you can use a loop:

```bash
for file in videos/*.mp4; do
  filename=$(basename "$file" .mp4)
  whisper "$file" \
    --output_dir transcripts/original \
    --language en \
    --model base
done
```

## File Naming Convention

- **Videos**: `M2027_W<week>_<topic>.mp4` or `M2027_W<week>-<topic>.mp4`
- **Original Transcripts**: Same as video filename, `.txt` extension
- **Formatted Transcripts**: Same as video filename with ` - FORMATTED.txt` suffix

## Tips

1. **Model Selection**: Use `base` for most cases. Use `small` or `medium` for better accuracy if time allows.
2. **Language**: Always specify `--language en` for English videos to improve accuracy.
3. **Logs**: Check `logs/` folder if transcription fails or produces unexpected results.
4. **Formatting**: The formatted version should be readable and well-organized for study purposes.

## Troubleshooting

- **FP16 Warning**: If you see "FP16 is not supported on CPU; using FP32 instead", this is normal and can be ignored.
- **Slow Processing**: Large video files take time. Use a smaller model (`tiny` or `base`) for faster processing.
- **Poor Quality**: If transcription quality is poor, try:
  - Using a larger model (`small` or `medium`)
  - Ensuring the video has clear audio
  - Specifying the language explicitly
