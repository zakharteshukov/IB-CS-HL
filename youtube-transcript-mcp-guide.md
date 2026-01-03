# YouTube Transcription via Docker MCP - Quick Guide

## Prerequisites
Ensure Docker is accessible. If `docker` command is not in PATH, use full path:
```bash
/Applications/Docker.app/Contents/Resources/bin/docker
```

## Connect Docker MCP Client
```bash
docker mcp client connect cursor
```

## List Available YouTube Transcript Tools
```bash
docker mcp tools ls | grep -i "youtube\|transcript"
```

Available tools:
- `get_transcript` - Plain text transcript
- `get_timed_transcript` - Transcript with timestamps
- `youtube-to-markdown` - Convert to markdown format

## Get Plain Text Transcript
```bash
docker mcp tools call get_transcript url="<youtube_url>"
```

Example:
```bash
docker mcp tools call get_transcript url="https://www.youtube.com/watch?v=e7MIqFX9M4I"
```

## Get Timed Transcript (with timestamps)
```bash
docker mcp tools call get_timed_transcript url="<youtube_url>"
```

Example:
```bash
docker mcp tools call get_timed_transcript url="https://www.youtube.com/watch?v=e7MIqFX9M4I"
```

## Convert to Markdown
```bash
docker mcp tools call youtube-to-markdown url="<youtube_url>"
```

## Save Output to File
```bash
docker mcp tools call get_transcript url="<youtube_url>" > transcript.txt
docker mcp tools call get_timed_transcript url="<youtube_url>" > transcript_timed.json
```

## Inspect Tool Details
```bash
docker mcp tools inspect get_transcript
docker mcp tools inspect get_timed_transcript
```

## Notes
- Use `url="..."` syntax (not `--url` flag)
- URLs with query parameters work fine
- Timed transcript returns JSON with `snippets` array containing `text`, `start`, and `duration`
- Plain transcript returns JSON with `title` and `transcript` fields



