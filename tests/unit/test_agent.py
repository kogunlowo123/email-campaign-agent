"""Email Campaign Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_design_campaign():
    """Test Design an email campaign with template and content."""
    tools = AgentTools()
    result = await tools.design_campaign(campaign_name="test", template="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_personalize_emails():
    """Test Personalize email content with dynamic merge fields."""
    tools = AgentTools()
    result = await tools.personalize_emails(template="test", merge_fields="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_manage_subscribers():
    """Test Manage subscriber list (add, remove, segment)."""
    tools = AgentTools()
    result = await tools.manage_subscribers(action="test", list_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_optimize_send_time():
    """Test Calculate optimal send time by segment and timezone."""
    tools = AgentTools()
    result = await tools.optimize_send_time(segment="test", historical_data=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.email_campaign_agent_agent import EmailCampaignAgentAgent
    agent = EmailCampaignAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
