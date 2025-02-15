"""Discord base tool."""

from langchain_core.tools import BaseTool
from pydantic import Field

from .discord_client import DiscordClientWrapper, login


class DiscordBaseTool(BaseTool):  # type: ignore[override]
    """Base class for Discord tools."""

    client: DiscordClientWrapper = Field(default_factory=login)
    """The Discord client wrapper."""
