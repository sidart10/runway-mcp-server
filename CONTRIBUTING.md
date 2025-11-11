# 🤝 Contributing to Runway MCP Server

Thank you for your interest in contributing to the Runway MCP Server! This guide will help you get started.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Running Tests](#running-tests)
- [Submitting Changes](#submitting-changes)
- [Code Standards](#code-standards)

---

## Code of Conduct

This project follows a simple code of conduct:

- **Be respectful** - Treat all contributors with respect
- **Be collaborative** - Work together to improve the project
- **Be constructive** - Provide helpful feedback and suggestions
- **Be professional** - Maintain a professional demeanor in all interactions

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- A Runway API key (from [dev.runwayml.com](https://dev.runwayml.com))

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/runway-mcp-server.git
   cd runway-mcp-server
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   # or: venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -e .
   pip install pytest pytest-asyncio  # Optional: for unit tests
   ```

4. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your RUNWAY_API_KEY
   ```

---

## Running Tests

### Comprehensive Test Suite

Run the full test suite:

```bash
source venv/bin/activate
python tests/test_server.py
```

Expected output:
```
🎉 ALL TESTS PASSED!
Your Runway MCP Server is ready to use!
```

### Individual Tests (Future)

When unit tests are added:

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_api_client.py

# Run with coverage
pytest --cov=runway_mcp_server --cov-report=html
```

---

## Submitting Changes

### Workflow

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or: git checkout -b fix/your-bug-fix
   ```

2. **Make Your Changes**
   - Follow the [Code Standards](#code-standards)
   - Add tests if applicable
   - Update documentation as needed

3. **Test Your Changes**
   ```bash
   python tests/test_server.py
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: Add feature description"
   # or: git commit -m "fix: Fix bug description"
   ```

5. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Describe your changes clearly

### Commit Message Format

We follow conventional commits:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Test additions or changes
- `refactor:` - Code refactoring
- `style:` - Code style changes (formatting)
- `chore:` - Maintenance tasks

Examples:
```
feat: Add support for Runway Gen-5 models
fix: Correct timeout handling in wait_for_task
docs: Update installation instructions
test: Add unit tests for API client
```

---

## Code Standards

### Python Style

Follow PEP 8 and these additional guidelines:

#### 1. Type Hints
Always use type hints:

```python
# ✅ Good
async def generate_video(
    prompt_text: str,
    model: str = "veo3.1",
    duration: int = 4
) -> str:
    """Generate a video."""
    pass

# ❌ Bad
async def generate_video(prompt_text, model="veo3.1", duration=4):
    """Generate a video."""
    pass
```

#### 2. Docstrings
Use comprehensive docstrings:

```python
# ✅ Good
async def generate_image(prompt: str, model: str = "gen4_image") -> str:
    """
    Generate an image using Gen-4 models.
    
    Args:
        prompt: Text description of the image to generate
        model: Model to use (gen4_image or gen4_image_turbo)
    
    Returns:
        JSON string with task result and image URL
    
    Raises:
        ValueError: If API key is not set
        TimeoutError: If generation times out
    
    Example:
        result = await generate_image("A sunset over mountains")
    """
    pass
```

#### 3. Async/Await
Use async/await for all I/O operations:

```python
# ✅ Good
async def fetch_data(url: str) -> Dict[str, Any]:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

# ❌ Bad
def fetch_data(url: str) -> Dict[str, Any]:
    response = requests.get(url)  # Blocking!
    return response.json()
```

#### 4. Error Handling
Always handle errors gracefully:

```python
# ✅ Good
async def get_task(task_id: str) -> Dict[str, Any]:
    """Get task status."""
    try:
        return await client.get_task(task_id)
    except httpx.HTTPStatusError as e:
        raise Exception(f"API error: {e.response.status_code}")
    except httpx.TimeoutException:
        raise TimeoutError("Request timed out")

# ❌ Bad
async def get_task(task_id: str):
    return await client.get_task(task_id)  # Unhandled errors
```

### Code Organization

- Keep functions focused (single responsibility)
- Use meaningful variable names
- Add comments for complex logic
- Group related functions together
- Maintain consistent naming conventions

### Documentation

When adding features:

1. Update `README.md` if user-facing
2. Add to `docs/FEATURES.md` if new capability
3. Update `docs/ARCHITECTURE.md` if architectural change
4. Add examples to relevant guides

---

## Areas for Contribution

### High Priority

1. **Unit Tests** - Add pytest-based unit tests
2. **Integration Tests** - Test API communication
3. **Logging Enhancement** - Improve debugging capabilities
4. **Error Messages** - Make error messages more helpful

### Medium Priority

5. **Retry Logic** - Add exponential backoff for failures
6. **Caching** - Cache repeated requests
7. **Webhook Support** - Add webhook notifications
8. **Batch Processing** - Process multiple requests efficiently

### Nice to Have

9. **Performance Monitoring** - Add metrics collection
10. **Additional Models** - Support new Runway features
11. **CLI Tool** - Add command-line interface
12. **Examples** - More usage examples

---

## Getting Help

- **Questions?** Open an issue with the `question` label
- **Bug Report?** Open an issue with the `bug` label
- **Feature Request?** Open an issue with the `enhancement` label

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Thank You! 🙏

Your contributions help make this project better for everyone. We appreciate your time and effort!

---

*For more information, see the [main README](README.md) or check the [documentation](docs/).*

