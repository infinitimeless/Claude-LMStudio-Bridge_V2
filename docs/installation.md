# Installation Guide

This guide will help you set up the Claude-LMStudio-Bridge and connect it to both LM Studio and Claude.

## Prerequisites

Before you begin, make sure you have:

1. **Python 3.8+** installed on your system
2. **LM Studio** downloaded and installed from [lmstudio.ai](https://lmstudio.ai/)
3. **Claude account** with MCP capability (requires Claude Pro subscription)

## Step 1: Install LM Studio

1. Download and install LM Studio from [lmstudio.ai](https://lmstudio.ai/)
2. Launch LM Studio
3. Download at least one model from the Models tab

## Step 2: Set Up the Bridge

1. Clone this repository:
   ```bash
   git clone https://github.com/infinitimeless/Claude-LMStudio-Bridge_V2.git
   cd Claude-LMStudio-Bridge_V2
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

   Or install the dependencies directly:
   ```bash
   pip install requests "mcp[cli]" openai anthropic-mcp
   ```

## Step 3: Start LM Studio Server

1. Open LM Studio
2. Load your preferred model
3. Make sure the local server is running (typically on port 1234)
   - Check the "Local Server" tab in LM Studio
   - The server URL should show as http://localhost:1234

## Step 4: Run the Bridge

1. With your virtual environment activated, run:
   ```bash
   python lmstudio_bridge.py
   ```

2. The bridge will start and wait for connections from Claude

## Step 5: Connect Claude to the Bridge

1. In your conversation with Claude, enable the MCP tool
2. Install the bridge as an MCP server
3. Use the tools provided by the bridge:
   - `health_check`: Verify LM Studio is running
   - `list_models`: See available models
   - `get_current_model`: Check which model is currently active
   - `chat_completion`: Send prompts to the local model

## Troubleshooting

### Common Issues

1. **"Error connecting to LM Studio API"**
   - Make sure LM Studio is running
   - Check that the local server is enabled in LM Studio
   - Verify the port number (default is 1234)

2. **"No response generated" or timeouts**
   - The model might be too large for your hardware
   - Try a smaller model
   - Reduce the max_tokens parameter

3. **Bridge installation fails**
   - Ensure you have the correct version of Python installed
   - Try updating pip: `pip install --upgrade pip`
   - Make sure all dependencies are installed correctly
   - If you encounter dependency issues, try the direct installation method:
     ```bash
     pip install requests "mcp[cli]" openai anthropic-mcp
     ```

### Getting Help

If you encounter issues not covered here, please open an issue on the GitHub repository with:
- Your system information
- The exact error message
- Steps to reproduce the issue