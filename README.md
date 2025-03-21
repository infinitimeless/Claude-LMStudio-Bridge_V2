# Claude-LMStudio-Bridge

A simple Model Control Protocol (MCP) server that allows Claude to communicate with locally running LLM models via [LM Studio](https://lmstudio.ai/).

## Overview

This bridge enables Claude to send prompts to locally running models in LM Studio and receive their responses. This can be useful for:

- Comparing Claude's responses with other models
- Accessing specialized local models for specific tasks
- Running queries even when you have limited Claude API quota
- Keeping sensitive queries entirely local

## Prerequisites

- Python 3.8+
- [Anthropic Claude](https://www.anthropic.com/claude) with MCP capability
- [LM Studio](https://lmstudio.ai/) running locally
- Local LLM model(s) loaded in LM Studio

## Installation

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

3. Install the required packages (choose one method):
   
   Using requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or directly install dependencies:
   ```bash
   pip install requests "mcp[cli]" openai anthropic-mcp
   ```

## Usage

1. Start LM Studio and load your preferred model.

2. Ensure LM Studio's local server is running (usually on port 1234 by default).

3. Run the bridge server:
   ```bash
   python lmstudio_bridge.py
   ```

4. In Claude's interface, enable the MCP server and point it to your locally running bridge.

5. You can now use the following MCP tools in your conversation with Claude:
   - `health_check`: Check if LM Studio API is accessible
   - `list_models`: Get a list of available models in LM Studio
   - `get_current_model`: Check which model is currently loaded
   - `chat_completion`: Send a prompt to the current model

## Example

Once connected, you can ask Claude to use the local model:

```
Claude, please use the LM Studio bridge to ask the local model: "What's your opinion on quantum computing?"
```

Claude will use the `chat_completion` tool to send the query to your local model and display the response.

## Configuration

By default, the bridge connects to LM Studio at `http://localhost:1234/v1`. If your LM Studio instance is running on a different port, modify the `LMSTUDIO_API_BASE` variable in `lmstudio_bridge.py`.

## Troubleshooting

If you encounter issues with dependencies, try installing them directly:
```bash
pip install requests "mcp[cli]" openai anthropic-mcp
```

For detailed installation instructions and troubleshooting, see the [Installation Guide](docs/installation.md).

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.