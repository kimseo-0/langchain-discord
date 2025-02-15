# test_discord_read_messages.py

from typing import Type

import pytest
from langchain_tests.unit_tests import ToolsUnitTests

from langchain_discord.tools.discord_read_messages import DiscordReadMessages


@pytest.fixture(autouse=True)
def fake_token(monkeypatch):
    """
    Set a fake DISCORD_BOT_TOKEN so `login()` does not raise ValueError.
    This fixture runs once per test function because monkeypatch is function-scoped.
    """
    monkeypatch.setenv("DISCORD_BOT_TOKEN", "FAKE_TOKEN_FOR_TESTS")


class TestDiscordReadMessagesUnit(ToolsUnitTests):
    @property
    def tool_constructor(self) -> Type[DiscordReadMessages]:
        return DiscordReadMessages

    @property
    def tool_constructor_params(self) -> dict:
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        return {"channel_id": "1234567890", "limit": 5}
