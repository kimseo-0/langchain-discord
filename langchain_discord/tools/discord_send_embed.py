"""Discord tool for sending embed (card-style) messages."""

import asyncio
import logging
from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from pydantic import BaseModel, Field

from .discord_base_tool import DiscordBaseTool

logger = logging.getLogger(__name__)


class DiscordSendEmbedSchema(BaseModel):
    """Input schema for sending embed messages."""

    channel_id: str = Field(..., description="Numeric string representing the Discord channel ID.")
    title: str = Field(..., description="Title text of the embed message.")
    description: str = Field(..., description="Main description/body text of the embed message.")
    color: Optional[int] = Field(0x5865F2, description="Hex color code for embed border (default: Discord blurple).")


class DiscordSendEmbedMessage(DiscordBaseTool):  # type: ignore[override]
    """Tool for sending embed (card) messages to Discord channels via REST API."""

    name: str = "discord_embed_sender"
    description: str = (
        "Sends a card-style embed message to a Discord channel. "
        "Supports title, description, and optional color customization."
    )
    args_schema: Type[BaseModel] = DiscordSendEmbedSchema

    def _validate_inputs(self, channel_id: str, title: str, description: str) -> Optional[str]:
        if not channel_id.isdigit():
            return "Error: Invalid channel ID format - must be numeric"
        if not title.strip():
            return "Error: Title cannot be empty"
        if not description.strip():
            return "Error: Description cannot be empty"
        return None

    def _run(
        self,
        channel_id: str,
        title: str,
        description: str,
        color: int = 0x5865F2,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Synchronous version."""
        err = self._validate_inputs(channel_id, title, description)
        if err:
            return err
        try:
            asyncio.get_running_loop()
            return "Error: Cannot call sync _run() inside a running event loop. Use the async version."
        except RuntimeError:
            try:
                result = asyncio.run(
                    self.client.send_embed_message(int(channel_id), title, description, color)
                )
                return "Embed result: " + result
            except Exception as e:
                logger.error(f"Error in sync embed send: {e}")
                return f"Error sending embed message: {e}"

    async def _arun(
        self,
        channel_id: str,
        title: str,
        description: str,
        color: int = 0x5865F2,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Async version."""
        err = self._validate_inputs(channel_id, title, description)
        if err:
            return err
        try:
            result = await self.client.send_embed_message(int(channel_id), title, description, color)
            return "Embed result: " + result
        except Exception as e:
            logger.error(f"Error in async embed send: {e}")
            return f"Error sending embed message: {e}"
