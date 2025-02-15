# langchain-discord

This package contains the LangChain integration with Discord

## Installation

```bash
pip install -U langchain-discord
```

And you should configure credentials by setting the following environment variables:

* TODO: fill this out

## Chat Models

`ChatDiscord` class exposes chat models from Discord.

```python
from langchain_discord import ChatDiscord

llm = ChatDiscord()
llm.invoke("Sing a ballad of LangChain.")
```

## Embeddings

`DiscordEmbeddings` class exposes embeddings from Discord.

```python
from langchain_discord import DiscordEmbeddings

embeddings = DiscordEmbeddings()
embeddings.embed_query("What is the meaning of life?")
```

## LLMs
`DiscordLLM` class exposes LLMs from Discord.

```python
from langchain_discord import DiscordLLM

llm = DiscordLLM()
llm.invoke("The meaning of life is")
```
