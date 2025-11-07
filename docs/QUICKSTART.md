# 🚀 Quick Start Guide - Runway MCP Server

Get up and running with Runway AI in 5 minutes!

## Step 1: Get Your API Key

1. Go to [dev.runwayml.com](https://dev.runwayml.com)
2. Sign up or log in
3. Create an organization
4. Generate an API key
5. Copy your key (starts with `rw_`)

## Step 2: Install

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export RUNWAY_API_KEY="rw_your_api_key_here"
```

## Step 3: Test the Server

```bash
# Run the example script
python example_usage.py
```

## Step 4: Configure MCP

### For Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "runway": {
      "command": "python",
      "args": ["/full/path/to/runway_mcp_server.py"],
      "env": {
        "RUNWAY_API_KEY": "rw_your_api_key_here"
      }
    }
  }
}
```

### For Other MCP Clients

Use the same configuration format in your MCP client's settings.

## Step 5: Start Creating!

### Quick Examples

#### Generate a Video
```
Generate a video of a sunset over the ocean with waves
```

#### Edit a Video with Aleph
```
Edit this video to remove the person in the background:
[video URL]
```

#### Create an Image
```
Create a cyberpunk cityscape at night with neon lights
```

## 🎯 Most Popular Features

### 1. **Aleph Video Editing** ⭐
The game-changer for video editing:
- Remove unwanted objects
- Add new elements
- Change camera angles
- Transform lighting and style

### 2. **Text-to-Video**
Create videos from descriptions in seconds

### 3. **Image-to-Video**
Bring your images to life with motion

### 4. **Style Transfer**
Apply artistic styles to existing videos

## 💡 Tips for Best Results

### Writing Good Prompts

**DO:**
- Be specific: "Aerial drone shot moving forward"
- Describe lighting: "Golden hour sunlight"
- Mention style: "Cinematic, professional"
- Include motion: "Slow pan left to right"

**DON'T:**
- Be vague: "Nice video"
- Skip details
- Use conflicting descriptions

### Aleph Editing Tips

**Structure your prompts:**
1. Action verb (add, remove, change, replace)
2. What to modify
3. How it should look

**Examples:**
- ✅ "Remove the car from the left side of the frame"
- ✅ "Add rain falling throughout the scene"
- ✅ "Change the lighting to dramatic sunset"
- ❌ "Make it better"

## 📊 Understanding Credits

- **5 seconds of video** ≈ 25 credits (Gen-4 Turbo)
- **1 image** ≈ 10 credits (Gen-4 Image)
- **Aleph editing** ≈ 75 credits per 5s (15/sec)

Standard plan: 625 credits/month = ~125 seconds of video

## ⚡ Speed Optimization

1. **Use Gen-4 Turbo** for fast iterations
2. **Start with 5-second videos** for testing
3. **Set `wait_for_completion=False`** to continue working
4. **Check status later** with `get_task_status()`

## 🔧 Troubleshooting

### "API key not set"
```bash
export RUNWAY_API_KEY="your_key"
# Or add to ~/.bashrc or ~/.zshrc
```

### "Task failed"
- Check your prompt for clarity
- Verify video/image URLs are accessible
- Ensure content complies with Runway policies

### "Timeout"
- Increase `max_wait` in function calls
- Check task status manually
- Runway's servers may be busy

## 📚 Next Steps

1. **Read the full README.md** for comprehensive examples
2. **Check out example_usage.py** for code samples
3. **Visit the Runway Help Center**: [help.runwayml.com](https://help.runwayml.com)
4. **Join the Discord** for community support

## 🎬 Sample Workflow

### Create a Marketing Video

1. **Generate base footage**:
   ```python
   generate_video_text_to_video(
       prompt_text="Product floating in minimalist white space, studio lighting",
       duration=5
   )
   ```

2. **Edit with Aleph**:
   ```python
   edit_video_with_aleph(
       input_video="[video from step 1]",
       prompt_text="Add sparkle effects around the product"
   )
   ```

3. **Extend the video**:
   ```python
   extend_video(
       input_video="[video from step 2]",
       extension_duration=5
   )
   ```

4. **Upscale to 4K**:
   ```python
   upscale_video_4k(
       input_video="[video from step 3]"
   )
   ```

## 🌟 Feature Highlights

| Feature | Speed | Quality | Credits/sec |
|---------|-------|---------|-------------|
| Gen-4 Turbo | ⚡⚡⚡ | ⭐⭐⭐⭐ | 5 |
| Aleph Edit | ⚡⚡ | ⭐⭐⭐⭐⭐ | 15 |
| Gen-3 Alpha | ⚡⚡ | ⭐⭐⭐⭐⭐ | 10 |

## 💬 Getting Help

- **Documentation**: This README and docs
- **API Docs**: [docs.dev.runwayml.com](https://docs.dev.runwayml.com)
- **Help Center**: [help.runwayml.com](https://help.runwayml.com)
- **Developer Portal**: [dev.runwayml.com](https://dev.runwayml.com)

---

**You're ready to create! 🎉**

Start with simple text-to-video, then explore Aleph editing for advanced workflows.
