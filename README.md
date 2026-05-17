# Python MCP Server

A Python-based Model Context Protocol (MCP) server implementation.

## Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Configuration

1. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   ```

2. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

3. **Install MCP dependencies:**
   ```bash
   .venv/bin/pip install "mcp[cli]"
   ```

4. **Install project dependencies:**
   ```bash
   .venv/bin/pip install psutil
   ```

## VS Code Integration

To add this MCP server to VS Code:

1. Open the Command Palette: `Ctrl + Shift + P`
2. Search for and select: **MCP: Open User Configuration**
3. Add your server configuration to the MCP servers section
4. Restart VS Code for changes to take effect

## Running the Server

```bash
.venv/bin/python server.py
```

## Project Structure

```
.
├── server.py          # Main server implementation
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Dependencies

- **mcp**: Model Context Protocol framework
- **psutil**: System and process utilities
