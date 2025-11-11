# 📦 Publishing Guide for Runway MCP Server

This guide walks you through publishing your MCP server to PyPI and the official MCP Registry.

## ✅ Prerequisites Checklist

Before publishing, make sure you have:

- [x] Python 3.10+ installed
- [x] Package structure created (✅ DONE!)
- [x] `pyproject.toml` configured (✅ DONE!)
- [x] `server.json` created (✅ DONE!)
- [x] README with mcp-name identifier (✅ DONE!)
- [ ] PyPI account ([create one here](https://pypi.org/account/register/))
- [ ] GitHub account
- [ ] Runway API key for testing

## 📝 Step-by-Step Publishing Process

### Part 1: Publish to PyPI

#### 1. Install Build Tools

```bash
# Make sure you're in the project directory
cd /Users/sid/Desktop/4.\ Coding\ Projects/runway-mcp-server

# Install build tools
pip install --upgrade build twine
```

#### 2. Test Your Package Locally

```bash
# Install in development mode
pip install -e .

# Test that it works
runway-mcp-server --help
# OR test with MCP Inspector
npx @modelcontextprotocol/inspector uvx runway-mcp-server
```

#### 3. Build the Package

```bash
# Clean any previous builds
rm -rf dist/ build/ *.egg-info

# Build distribution files
python -m build

# You should now see files in dist/:
# - runway-mcp-server-0.1.0.tar.gz (source distribution)
# - runway-mcp-server-0.1.0-py3-none-any.whl (wheel distribution)
```

#### 4. Check the Package

```bash
# Verify the package metadata
twine check dist/*

# Should show:
# Checking dist/runway-mcp-server-0.1.0.tar.gz: PASSED
# Checking dist/runway-mcp-server-0.1.0-py3-none-any.whl: PASSED
```

#### 5. Upload to PyPI

```bash
# Upload to PyPI (you'll be prompted for username and password)
twine upload dist/*

# Or use an API token (recommended):
# 1. Go to https://pypi.org/manage/account/token/
# 2. Create a new API token
# 3. Use it like this:
twine upload -u __token__ -p pypi-YOUR_TOKEN_HERE dist/*
```

**🎉 Your package is now on PyPI!** Anyone can install it with: `pip install runway-mcp-server`

---

### Part 2: Publish to MCP Registry

#### 1. Install MCP Publisher CLI

```bash
# Mac/Linux with Homebrew (easiest)
brew install mcp-publisher

# Or download binary directly
curl -L "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher && sudo mv mcp-publisher /usr/local/bin/
```

#### 2. Verify server.json

```bash
# Make sure server.json is valid
cat server.json

# Check that the version matches pyproject.toml
# Both should say "0.1.0"
```

#### 3. Authenticate with GitHub

```bash
# This will open your browser for OAuth
mcp-publisher login github

# Follow the prompts to authorize with GitHub
# This creates .mcpregistry_github_token (already in .gitignore)
```

#### 4. Publish to Registry

```bash
# Publish your server
mcp-publisher publish

# You should see:
# ✓ Successfully published
```

**⚠️ Note:** The registry is in preview and can be slow. If it fails, just retry:
```bash
mcp-publisher publish  # Try again if it times out
```

#### 5. Verify Publication

```bash
# Check that your server appears in the registry
curl "https://registry.modelcontextprotocol.io/v0/servers?search=runway-mcp-server"

# You should see your server metadata in the JSON response
```

**🎉 Your server is now in the official MCP Registry!**

---

## 🧪 Testing the Published Package

### Test with uvx

```bash
# This simulates how users will install it
uvx runway-mcp-server

# Set your API key first
export RUNWAY_API_KEY=your_key_here
```

### Test in Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "runway": {
      "command": "uvx",
      "args": ["runway-mcp-server"],
      "env": {
        "RUNWAY_API_KEY": "your_actual_key_here"
      }
    }
  }
}
```

Restart Claude Desktop and test!

---

## 🔄 Updating Your Package

When you make changes and want to release a new version:

### 1. Update Version Numbers

Update the version in **three places**:

1. `pyproject.toml`: Change `version = "0.1.0"` to `version = "0.1.1"`
2. `server.json`: Change `"version": "0.1.0"` to `"version": "0.1.1"`
3. `src/runway_mcp_server/__init__.py`: Change `__version__ = "0.1.0"` to `__version__ = "0.1.1"`

### 2. Rebuild and Republish

```bash
# Clean old builds
rm -rf dist/ build/ *.egg-info

# Build new version
python -m build

# Upload to PyPI
twine upload dist/*

# Wait 1-2 minutes for PyPI to propagate, then publish to MCP Registry
mcp-publisher publish
```

---

## 🐛 Troubleshooting

### "Package not found on PyPI"
- Wait a few minutes after uploading to PyPI
- Verify: https://pypi.org/project/runway-mcp-server/

### "mcp-name not found in README"
- Check that `<!-- mcp-name: io.github.sidart10/runway-mcp-server -->` is in README.md
- Make sure it's on PyPI (the registry checks the PyPI README)

### "Authentication failed"
- Re-run: `mcp-publisher login github`
- Make sure you're logged into GitHub in your browser

### "Version already exists"
- You can't re-upload the same version
- Increment the version number in all three places

### "Registry timeout"
- The registry is in preview and can be slow
- Just retry: `mcp-publisher publish`

---

## 📊 Post-Publication

After publishing:

1. **Star your own repo** on GitHub for visibility
2. **Share on social media** (Twitter, LinkedIn)
3. **Post in MCP community channels**:
   - [MCP Discord](https://discord.gg/modelcontextprotocol)
   - [GitHub Discussions](https://github.com/modelcontextprotocol/discussions)
4. **Monitor issues** on your GitHub repo
5. **Keep it updated** with new Runway features

---

## 🎯 Quick Reference

**PyPI package page:** https://pypi.org/project/runway-mcp-server/

**MCP Registry entry:** https://registry.modelcontextprotocol.io/v0/servers?search=runway-mcp-server

**Installation command:** `uvx runway-mcp-server`

**Your GitHub repo:** https://github.com/sidart10/runway-mcp-server

---

## 📞 Need Help?

- **PyPI issues:** https://pypi.org/help/
- **MCP Registry issues:** https://github.com/modelcontextprotocol/registry/issues
- **Runway API issues:** https://help.runwayml.com

Good luck with your launch! 🚀

