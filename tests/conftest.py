"""Test configuration for Email Campaign Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "email-campaign-agent", "category": "Marketing"}
