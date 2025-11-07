# 🏗️ Runway MCP Server - Architecture & Design

## 📐 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Claude / MCP Client                       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ MCP Protocol
                         │
┌────────────────────────▼────────────────────────────────────┐
│                  Runway MCP Server                           │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              FastMCP Framework                        │   │
│  │  - Tool Registration                                  │   │
│  │  - Request Routing                                    │   │
│  │  - Response Formatting                                │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           RunwayAPIClient                             │   │
│  │  - Authentication                                     │   │
│  │  - HTTP Client (httpx)                                │   │
│  │  - Error Handling                                     │   │
│  │  - Task Polling                                       │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Tool Functions                           │   │
│  │  ├── Image Generation                                 │   │
│  │  ├── Video Generation                                 │   │
│  │  ├── Aleph Editing ⭐                                 │   │
│  │  ├── Video Enhancement                                │   │
│  │  └── Task Management                                  │   │
│  └──────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTPS / JSON
                         │
┌────────────────────────▼────────────────────────────────────┐
│              Runway API (api.dev.runwayml.com)              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Endpoints:                                           │   │
│  │  - /v1/images                                         │   │
│  │  - /v1/text_to_video                                  │   │
│  │  - /v1/image_to_video                                 │   │
│  │  - /v1/video_to_video (Aleph)                         │   │
│  │  - /v1/extend_video                                   │   │
│  │  - /v1/upscale                                        │   │
│  │  - /v1/tasks/{id}                                     │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Component Details

### 1. MCP Server Layer

**Purpose:** Interface between Claude and Runway API

**Technology:**
- FastMCP framework
- Python 3.10+ with async/await
- Type hints for safety

**Responsibilities:**
- Expose tools to MCP clients
- Validate inputs
- Format responses
- Error handling

### 2. API Client Layer

**Purpose:** Handle all communication with Runway

**Features:**
```python
class RunwayAPIClient:
    - Authenticated requests
    - Automatic retries
    - Task polling
    - Error parsing
    - Timeout handling
```

**Key Methods:**
- `_request()` - Base HTTP method
- `create_task()` - Start generation
- `get_task()` - Check status
- `wait_for_task()` - Poll until complete

### 3. Tool Functions Layer

**Purpose:** High-level operations exposed to users

**Categories:**
1. **Image Generation**
   - `generate_image_gen4()`

2. **Video Generation**
   - `generate_video_text_to_video()`
   - `generate_video_image_to_video()`
   - `generate_video_first_last_frame()`

3. **Video Editing (Aleph)**
   - `edit_video_with_aleph()` ⭐
   - `restyle_video()`

4. **Enhancement**
   - `extend_video()`
   - `upscale_video_4k()`

5. **Management**
   - `get_task_status()`
   - `cancel_task()`
   - `list_available_models()`
   - `get_api_info()`

## 🔄 Request Flow

### Standard Generation Flow

```
User Request
    ↓
MCP Client → Tool Call
    ↓
Validate Parameters
    ↓
Build API Request
    ↓
Send to Runway API
    ↓
Receive Task ID
    ↓
[If wait_for_completion=True]
    ↓
Poll Task Status (every 5s)
    ↓
Task Complete?
    Yes → Return Result
    No → Continue Polling
    Failed → Return Error
    ↓
Format Response
    ↓
Return to User
```

### Aleph Editing Flow

```
User + Video
    ↓
edit_video_with_aleph()
    ↓
Prepare Video URL + Prompt
    ↓
Optional: Add Reference Image
    ↓
POST /v1/video_to_video
    ↓
Runway Processing (5-8 min)
    - Analyze video
    - Apply edits
    - Maintain consistency
    - Render output
    ↓
Poll for Completion
    ↓
Return Edited Video URL
```

## 📊 Data Flow

### Input Processing

```python
# User provides high-level parameters
{
    "prompt_text": "Description",
    "model": "gen4_turbo",
    "duration": 10
}
    ↓
# Server adds API-specific fields
{
    "promptText": "Description",  # camelCase
    "model": "gen4_turbo",
    "duration": 10,
    "ratio": "1280:768"  # default added
}
    ↓
# Add authentication
{
    "headers": {
        "Authorization": "Bearer rw_...",
        "X-Runway-Version": "2024-11-06"
    },
    "json": {...}
}
```

### Output Processing

```python
# Runway returns
{
    "id": "task_123",
    "status": "SUCCEEDED",
    "output": ["https://cdn.runwayml.com/video.mp4"],
    "createdAt": "2024-11-07T...",
    "progress": 100
}
    ↓
# Server formats for user
{
    "status": "success",
    "video_url": "https://cdn.runwayml.com/video.mp4",
    "task_id": "task_123",
    "model": "gen4_turbo"
}
```

## 🛡️ Error Handling

### Hierarchy

```
Exception
    ↓
ValueError - Invalid parameters
    ↓
httpx.HTTPStatusError - API errors
    ↓
TimeoutError - Generation timeout
    ↓
TaskFailedError - Generation failed
```

### Recovery Strategies

1. **Invalid Input**
   - Validate before sending
   - Return clear error message
   - Suggest corrections

2. **Network Errors**
   - Automatic retry (httpx)
   - Exponential backoff
   - User notification

3. **Task Failures**
   - Parse failure reason
   - Return diagnostic info
   - Suggest alternatives

4. **Timeouts**
   - Configurable wait time
   - Status check available
   - Task continues server-side

## 🔐 Security

### API Key Management

```
Environment Variable
    ↓
Never logged or exposed
    ↓
Stored in memory only
    ↓
Sent in Authorization header
    ↓
HTTPS encrypted
```

### Best Practices

- ✅ Environment variables only
- ✅ No hardcoded keys
- ✅ No logging of credentials
- ✅ HTTPS for all requests
- ✅ No key in responses

## ⚡ Performance

### Async Architecture

```python
async def generate_video(...):
    # Non-blocking
    task = await client.create_task(...)
    
    if wait_for_completion:
        # Efficient polling
        while not complete:
            await asyncio.sleep(5)
            status = await client.get_task(...)
    
    return result
```

### Optimizations

1. **Connection Pooling**
   - httpx AsyncClient
   - Reuse connections
   - Efficient requests

2. **Smart Polling**
   - 5-second intervals
   - Configurable timing
   - Early termination

3. **Batch Operations**
   - Multiple tasks
   - Parallel processing
   - Efficient resource use

## 📈 Scalability

### Current Limits

- API rate limits per plan
- Concurrent task limits
- Processing queue depth

### Scaling Strategies

1. **Horizontal**
   - Multiple server instances
   - Load balancing
   - Queue management

2. **Vertical**
   - Higher tier plans
   - More concurrent requests
   - Priority processing

3. **Caching**
   - Store common results
   - Reduce regeneration
   - Faster responses

## 🔌 Integration Points

### MCP Client Integration

```json
{
  "mcpServers": {
    "runway": {
      "command": "python",
      "args": ["runway_mcp_server.py"],
      "env": {
        "RUNWAY_API_KEY": "..."
      }
    }
  }
}
```

### Direct Python Integration

```python
from runway_mcp_server import generate_video_text_to_video

result = await generate_video_text_to_video(
    prompt_text="...",
    model="gen4_turbo"
)
```

### API Integration

```python
# Server exposes standard MCP protocol
# Compatible with any MCP client
# Standard tool calling interface
```

## 🧪 Testing Strategy

### Unit Tests
- Individual tool functions
- Parameter validation
- Error handling

### Integration Tests
- API communication
- Task polling
- End-to-end flows

### Manual Testing
- Example scripts
- Real API calls
- Production scenarios

## 📦 Deployment

### Requirements

```
Python 3.10+
    ↓
pip install -r requirements.txt
    ↓
export RUNWAY_API_KEY="..."
    ↓
python runway_mcp_server.py
```

### Production Considerations

1. **Process Management**
   - systemd service
   - Process monitoring
   - Auto-restart

2. **Logging**
   - Structured logs
   - Error tracking
   - Performance metrics

3. **Monitoring**
   - Health checks
   - Task tracking
   - Error rates

## 🎯 Design Principles

### 1. Simplicity
- Clear function names
- Intuitive parameters
- Sensible defaults

### 2. Reliability
- Robust error handling
- Graceful degradation
- Clear error messages

### 3. Flexibility
- Optional parameters
- Multiple models
- Configurable behavior

### 4. Performance
- Async operations
- Efficient polling
- Resource optimization

### 5. Documentation
- Comprehensive docs
- Code examples
- Best practices

## 🔮 Future Architecture

### Planned Enhancements

1. **Caching Layer**
   ```
   Request → Cache Check → API Call
   ```

2. **Webhook Support**
   ```
   Task Complete → Webhook → Notification
   ```

3. **Batch Processing**
   ```
   Multiple Requests → Queue → Process → Results
   ```

4. **State Management**
   ```
   Project Context → Multi-Step Workflows
   ```

## 📚 Technical Stack

### Core Technologies
- **Python 3.10+** - Language
- **FastMCP** - MCP framework
- **httpx** - HTTP client
- **asyncio** - Async operations

### API Integration
- **REST API** - HTTP/JSON
- **Bearer Auth** - API keys
- **Polling** - Task status
- **Webhooks** - Future support

### Type System
- **Type hints** - Full coverage
- **Literal types** - Enums
- **Optional types** - Flexibility
- **Generic types** - Reusability

## 🎓 Learning Resources

### Understanding the Code

1. **Start:** `runway_mcp_server.py`
2. **Read:** Tool functions
3. **Study:** RunwayAPIClient
4. **Explore:** Error handling
5. **Test:** example_usage.py

### Key Concepts

- **MCP Protocol** - Tool interfaces
- **Async/Await** - Non-blocking I/O
- **REST APIs** - HTTP communication
- **Task Polling** - Status checking
- **Type Safety** - Error prevention

---

**This architecture enables professional-grade video generation through a clean, scalable, and maintainable design. 🏗️**
