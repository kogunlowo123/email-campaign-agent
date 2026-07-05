# Email Campaign Agent

[![CI](https://github.com/kogunlowo123/email-campaign-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/email-campaign-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Marketing | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Email campaign agent that designs email sequences, personalizes content with merge fields, manages subscriber lists, optimizes send times, and analyzes campaign performance.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `design_campaign` | Design an email campaign with template and content |
| `personalize_emails` | Personalize email content with dynamic merge fields |
| `manage_subscribers` | Manage subscriber list (add, remove, segment) |
| `optimize_send_time` | Calculate optimal send time by segment and timezone |
| `analyze_campaign` | Analyze email campaign performance (open rate, CTR, conversions) |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/email-campaign/create` | Create or generate |
| `POST` | `/api/v1/email-campaign/analyze` | Analyze performance |
| `POST` | `/api/v1/email-campaign/optimize` | Optimize |
| `POST` | `/api/v1/email-campaign/schedule` | Schedule |
| `POST` | `/api/v1/email-campaign/report` | Generate report |

## Features

- Email
- Campaign
- Analytics
- Optimization

## Integrations

- Hubspot Marketing
- Marketo
- Mailchimp
- Google Analytics
- Meta Ads

## Architecture

```
email-campaign-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── email_campaign_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Marketing Platform + LLM + Analytics**

---

Built as part of the Enterprise AI Agent Platform.
