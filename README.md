# Runway MCP Server

<!-- mcp-name: io.github.sidart10/runway-mcp-server -->

A Model Context Protocol (MCP) server for Runway ML, providing comprehensive AI video generation and editing capabilities through Gen-4, Veo 3, and Aleph models.

**MCP Registry Name:** `io.github.sidart10/runway-mcp-server`

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Available Tools](#available-tools)
- [Usage Examples](#usage-examples)
- [Documentation](#documentation)
- [Project Structure](#project-structure)
- [Rate Limits](#rate-limits)
- [Troubleshooting](#troubleshooting)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Resources](#resources)

---

## Features

### Video Generation
- **Text-to-Video** - Generate videos from text descriptions using Veo 3 models
- **Image-to-Video** - Animate static images with Gen-4 and Gen-3 models
- **Keyframe Control** - Precise control with first/last frame specification

### Video Editing
- **Aleph Video Editing** - Advanced video-to-video transformations:
  - Add, remove, or replace objects in existing videos
  - Change camera angles and generate novel views
  - Transform lighting, style, and environments
  - Generate shot continuations

### Image Generation
- **Gen-4 Image Models** - High-fidelity image generation with reference support
- **Reference Images** - Consistent characters and styles using tagged references

### Advanced Tools
- **Video Extension** - Extend videos by 5-10 seconds
- **4K Upscaling** - Enhance videos to 4K resolution
- **Style Transfer** - Apply artistic styles to existing videos

---

## Installation

### Option 1: Install from PyPI (Recommended)

```bash
# Install with uvx (automatically manages dependencies)
uvx runway-mcp-server

# Or install globally with pip
pip install runway-mcp-server
```

### Option 2: Install from Source

```bash
# Clone the repository
git clone https://github.com/sidart10/runway-mcp-server.git
cd runway-mcp-server

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate    # Windows

# Install in development mode
pip install -e .
```

### Requirements

- Python 3.10 or higher
- Runway API key from [dev.runwayml.com](https://dev.runwayml.com)

---

## Configuration

### Step 1: Configure API Key

Set your Runway API key as an environment variable or in a `.env` file:

```bash
# .env file
RUNWAY_API_KEY=your_api_key_here
```

### Step 2: Add to MCP Client Configuration

**For Cursor:**

Edit `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "runway": {
      "command": "uvx",
      "args": ["runway-mcp-server"],
      "env": {
        "RUNWAY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**For Claude Desktop:**

Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "runway": {
      "command": "uvx",
      "args": ["runway-mcp-server"],
      "env": {
        "RUNWAY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### Step 3: Restart Client

Restart Cursor or Claude Desktop to load the server.

---

## Available Tools

The server exposes the following MCP tools:

| Tool | Description | Use Case |
|------|-------------|----------|
| `generate_image_gen4` | Generate high-quality images with Gen-4 models | Creating images with consistent characters/styles |
| `generate_video_text_to_video` | Generate videos from text descriptions | Creating videos from prompts using Veo 3 |
| `generate_video_image_to_video` | Animate static images | Bringing images to life with motion |
| `generate_video_first_last_frame` | Generate video between two frames | Precise control over start and end states |
| `edit_video_with_aleph` | Transform existing videos with AI | Object manipulation, camera changes, lighting |
| `restyle_video` | Apply artistic styles to videos | Style transfer and aesthetic transformations |
| `extend_video` | Extend video duration | Adding 5-10 seconds to existing videos |
| `upscale_video_4k` | Upscale to 4K resolution | Enhancing video quality for production |
| `get_task_status` | Check generation progress | Monitoring long-running tasks |
| `cancel_task` | Cancel running tasks | Stopping unwanted generation jobs |
| `list_available_models` | List all available models | Discovering model capabilities |
| `get_api_info` | Server configuration info | Debugging and setup verification |

---

## Usage Examples

### Generate Video from Text

```
Generate a 6-second video of a golden retriever and orange cat sitting together on a cozy couch with warm cinematic lighting
```

### Edit Video with Aleph

```
Edit this video to remove all people from the scene: https://example.com/video.mp4
```

### Animate an Image

```
Animate this image with a time-lapse of clouds moving across the sky: https://example.com/sunset.jpg
```

### Generate Image with Reference

```
Generate a Gen-4 image of @Hero standing on a mountaintop at sunset, 1920x1080 resolution
```

### Style Transfer

```
Transform this video into a vibrant watercolor painting style: https://example.com/video.mp4
```

---

## Documentation

### Getting Started
- [Quick Start Guide](docs/QUICKSTART.md) - Installation and setup walkthrough
- [Features Guide](docs/FEATURES.md) - Comprehensive feature documentation
- [Aleph Guide](docs/ALEPH_GUIDE.md) - In-depth video editing guide

### Technical Documentation
- [Architecture](docs/ARCHITECTURE.md) - System design and implementation patterns
- [Architecture Review](docs/ARCHITECTURE_REVIEW.md) - Code quality and design review
- [Test Results](docs/TEST_RESULTS.md) - Automated test suite results

### Development
- [Publishing Guide](docs/PUBLISHING_GUIDE.md) - Instructions for publishing updates
- [Package Transformation](docs/PACKAGE_TRANSFORMATION_SUMMARY.md) - Package structure details
- [Testing Guide](tests/README.md) - Running and writing tests

---

## Project Structure

```
runway-mcp-server/
├── src/                           # Package source code
│   └── runway_mcp_server/
│       ├── __init__.py            # Package initialization
│       └── server.py              # Main server implementation
├── docs/                          # Documentation
│   ├── QUICKSTART.md              # Quick start guide
│   ├── ARCHITECTURE.md            # System architecture
│   ├── ARCHITECTURE_REVIEW.md     # Code review
│   ├── FEATURES.md                # Feature documentation
│   ├── ALEPH_GUIDE.md             # Aleph editing guide
│   ├── TEST_RESULTS.md            # Test reports
│   ├── PUBLISHING_GUIDE.md        # Publishing instructions
│   └── PACKAGE_TRANSFORMATION_SUMMARY.md  # Packaging details
├── tests/                         # Test suite
│   ├── test_server.py             # Comprehensive tests
│   └── README.md                  # Testing guide
├── config/                        # Configuration templates
│   └── mcp_config_example.json    # Example MCP configuration
├── pyproject.toml                 # Package configuration
├── server.json                    # MCP Registry metadata
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment template
├── README.md                      # This file
└── .env                           # API key (create this)
```

---

## Rate Limits

API usage is rate-limited based on your Runway subscription plan:

- **Gen-4 Turbo:** Approximately 5 credits per second of video
- **Aleph Editing:** Approximately 15 credits per second of video
- **Gen-3 Alpha:** Varies by model and settings

Monitor your usage and check credit balance at [dev.runwayml.com](https://dev.runwayml.com).

---

## Troubleshooting

### API Key Not Loading

Verify your `.env` file exists and contains the API key:

```bash
# Check if .env file exists
ls -la .env

# Verify key loads correctly
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('OK' if os.getenv('RUNWAY_API_KEY') else 'MISSING')"
```

### Server Won't Start

1. Verify Python version: `python3 --version` (must be 3.10+)
2. Ensure virtual environment is activated
3. Check dependencies are installed: `pip list | grep mcp`
4. Review server logs for specific error messages

### Task Timeouts

Video generation is compute-intensive and may take several minutes:

- **Text-to-video:** 2-5 minutes
- **Image-to-video:** 3-7 minutes
- **Aleph editing:** 5-10 minutes
- **4K upscaling:** 3-5 minutes

Use `get_task_status(task_id)` to monitor progress instead of waiting synchronously.

### Import Errors

If you encounter import errors after installation:

```bash
# Reinstall the package
pip uninstall runway-mcp-server
pip install runway-mcp-server

# Or for development
pip install -e .
```

---

## Testing

Run the comprehensive test suite:

```bash
# Activate virtual environment
source venv/bin/activate

# Run tests
python tests/test_server.py
```

Expected output: All tests should pass with detailed results.

See [tests/README.md](tests/README.md) for detailed testing documentation.

---

## Contributing

Contributions are welcome! This project follows the Model Context Protocol specification.

### Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/runway-mcp-server.git`
3. Create a branch: `git checkout -b feature/your-feature`
4. Install in development mode: `pip install -e .`
5. Make your changes
6. Run tests: `python tests/test_server.py`
7. Commit and push: `git commit -am "Add feature" && git push origin feature/your-feature`
8. Open a pull request

### Code Style

- Follow PEP 8 style guidelines
- Include docstrings for all functions
- Add type hints where appropriate
- Write tests for new features

---

## License

MIT License - see LICENSE file for details.

This MCP server is provided as-is for use with the Runway API. Runway API usage is subject to [Runway's terms of service](https://runwayml.com/terms).

---

## Resources

- **Runway Developer Portal:** [dev.runwayml.com](https://dev.runwayml.com)
- **Runway API Documentation:** [docs.dev.runwayml.com](https://docs.dev.runwayml.com)
- **MCP Specification:** [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **MCP Registry:** [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io)
- **PyPI Package:** [pypi.org/project/runway-mcp-server](https://pypi.org/project/runway-mcp-server)
- **Issue Tracker:** [github.com/sidart10/runway-mcp-server/issues](https://github.com/sidart10/runway-mcp-server/issues)

---

## Support

For issues or questions:

1. Check the [documentation](docs/)
2. Search [existing issues](https://github.com/sidart10/runway-mcp-server/issues)
3. Review [Runway's help center](https://help.runwayml.com)
4. Open a [new issue](https://github.com/sidart10/runway-mcp-server/issues/new) if needed

---

**Built for the Runway AI community**

For updates and announcements, watch this repository or follow development on GitHub.
