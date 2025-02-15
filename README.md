# langchain-discord

This package provides Discord tools and a toolkit for use with LangChain. It includes:

- **`DiscordReadMessages`**: Read messages from a given Discord channel.
- **`DiscordSendMessage`**: Send messages to a given Discord channel.
- **`DiscordToolkit`**: A convenient toolkit that bundles these tools.

---

## Installation

```bash
pip install -U langchain-discord
```

---

## Environment Variable

Export your bot token so the tools can authenticate with the Discord API:

```bash
export DISCORD_BOT_TOKEN="your-discord-bot-token"
```

If this environment variable is not set, the tools will raise a `ValueError` when instantiated.

---

## Usage

### Direct Tool Usage

```python
from langchain_discord.tools.discord_read_messages import DiscordReadMessages
from langchain_discord.tools.discord_send_messages import DiscordSendMessage

# Create instances of each tool
read_tool = DiscordReadMessages()
send_tool = DiscordSendMessage()

# Read the last 5 messages from channel 1234567890
read_result = read_tool({"channel_id": "1234567890", "limit": 5})
print(read_result)

# Send a message to the same channel
send_result = send_tool({"channel_id": "1234567890", "message": "Hello from Python!"})
print(send_result)
```

### Using the Toolkit

You can also use `DiscordToolkit` to automatically gather both tools:

```python
from langchain_discord.toolkits import DiscordToolkit

toolkit = DiscordToolkit()
tools = toolkit.get_tools()

# tools[0] should be DiscordReadMessages, tools[1] is DiscordSendMessage
read_tool = tools[0]
send_tool = tools[1]

# Example usage
print(read_tool({"channel_id": "1234567890", "limit": 5}))
print(send_tool({"channel_id": "1234567890", "message": "Hello from toolkit!"}))
```

---

## Tests

If you have a tests folder (e.g. `tests/unit_tests/`), you can run them (assuming Pytest) with:

```bash
pytest --maxfail=1 --disable-warnings -q
```

Make sure your `DISCORD_BOT_TOKEN` is set or your tests are mocked so they don’t require a real token.

---

## License

[MIT License](./LICENSE)

---

## Further Documentation

- For more details, see the docstrings in:
  - [`discord_read_messages.py`](./langchain_discord/tools/discord_read_messages.py)
  - [`discord_send_messages.py`](./langchain_discord/tools/discord_send_messages.py)
  - [`toolkits.py`](./langchain_discord/toolkits.py) for `DiscordToolkit`

- Official Discord Developer Docs: <https://discord.com/developers/docs/intro>
- [LangChain GitHub](https://github.com/hwchase17/langchain) for general LangChain usage and tooling.