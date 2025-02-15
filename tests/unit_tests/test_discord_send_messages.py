# test_discord_send_messages.py

from typing import Type

import pytest
from langchain_tests.unit_tests import ToolsUnitTests

from langchain_discord.tools.discord_send_messages import DiscordSendMessage


@pytest.fixture(autouse=True)
def fake_token(monkeypatch):
    """
    Automatically apply a fake DISCORD_BOT_TOKEN environment variable
    for each test function. That way, login() won't raise ValueError.
    """
    monkeypatch.setenv("DISCORD_BOT_TOKEN", "FAKE_TOKEN_FOR_TESTS")


class TestDiscordSendMessageUnit(ToolsUnitTests):
    @property
    def tool_constructor(self) -> Type[DiscordSendMessage]:
        """
        Return the SendMessage tool class.
        """
        return DiscordSendMessage

    @property
    def tool_constructor_params(self) -> dict:
        """
        Return any constructor arguments for DiscordSendMessage.
        If none are required, return an empty dict.
        """
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        """
        Return the example args for invoking the tool:
          - message: str
          - channel_id: str
        """
        return {
            "message": "Hello from unittests!",
            "channel_id": "1234567890"
        }
