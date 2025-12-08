# Whisper Transcription Guide

## Installation Complete ✅

Whisper is installed and ready to use!

## Basic Usage

```bash
# Transcribe a video to text file
whisper video.mp4 --output_format txt

# Specify output directory
whisper video.mp4 --output_format txt --output_dir ./transcriptions

# Use a specific model (faster = less accurate, slower = more accurate)
whisper video.mp4 --model medium --output_format txt

# Specify language (faster processing)
whisper video.mp4 --language en --output_format txt
```

## Available Models (speed vs accuracy trade-off)

- `tiny` - Fastest, least accurate (~39M parameters)
- `base` - Fast, less accurate (~74M parameters)
- `small` - Balanced (~244M parameters)
- `medium` - Slower, more accurate (~769M parameters) ⭐ Recommended
- `large` - Slowest, most accurate (~1550M parameters)
- `large-v2` - Latest large model
- `large-v3` - Latest large model (best quality)

## Model Selection Guide

For a 2-hour video on M2 Pro:
- **`tiny`**: ~5-10 minutes (fastest, lower quality)
- **`base`**: ~10-15 minutes (fast, decent quality)
- **`small`**: ~20-30 minutes (balanced) ⭐ Good choice
- **`medium`**: ~40-60 minutes (high quality) ⭐ Recommended
- **`large-v3`**: ~60-90 minutes (best quality, slowest)

## Timing Estimates for 2-Hour Video on MacBook M2 Pro

Based on typical M2 Pro performance:

| Model | Estimated Time | Quality | Use Case |
|-------|---------------|---------|----------|
| tiny | 5-10 minutes | Basic | Quick drafts |
| base | 10-15 minutes | Good | General use |
| small | 20-30 minutes | Very Good | Balanced ⭐ |
| medium | 40-60 minutes | Excellent | High quality ⭐ |
| large-v3 | 60-90 minutes | Best | Maximum accuracy |

**Note**: First run will download the model (~500MB-3GB depending on model), which adds a few minutes.

## Recommended Command for 2-Hour Video

```bash
# High quality transcription (recommended)
whisper video.mp4 --model medium --language en --output_format txt --output_dir ./transcriptions

# Faster option with good quality
whisper video.mp4 --model small --language en --output_format txt --output_dir ./transcriptions
```

## Output Formats

- `txt` - Plain text file
- `srt` - Subtitle file
- `vtt` - WebVTT subtitle file
- `json` - JSON with timestamps
- `tsv` - Tab-separated values
- `all` - All formats

## Tips

1. **First run**: The model will be downloaded automatically (one-time, ~500MB-3GB)
2. **Language**: Specifying `--language en` speeds up processing
3. **GPU**: M2 Pro uses Neural Engine automatically for acceleration
4. **Memory**: `large` models need ~10GB RAM, `medium` needs ~5GB
5. **Output**: Files are saved in the same directory as input by default

## Example Workflow

```bash
# Navigate to your video directory
cd /path/to/videos

# Transcribe with medium model (recommended balance)
whisper my-video.mp4 --model medium --language en --output_format txt

# Output will be: my-video.txt
```
