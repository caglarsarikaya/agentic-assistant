# Agentic Assistant

A multi-agent system with memory and task routing capabilities built with FastAPI and LangChain.

## Features

- **Multi-Agent Architecture**: Different specialized agents for various tasks
- **Memory Management**: Short-term session memory and long-term MongoDB storage
- **Task Routing**: LLM-based planner for intelligent task distribution
- **Web Search**: Integration with Serper.dev for web search capabilities
- **Calendar Integration**: Google Calendar integration for scheduling tasks

## Project Structure

```
agentic-assistant/
├── app/
│   ├── main.py                     # FastAPI entrypoint
│   ├── api/
│   │   └── routes.py              # API routes
│   ├── agents/
│   │   ├── base.py                # BaseAgent with memory and session helpers
│   │   ├── peer_agent.py          # PeerAgent: LLM-based planner and router
│   │   ├── llm_agent.py           # LLM-only agent for direct responses
│   │   ├── search_agent.py        # Web search agent
│   │   └── calendar_agent.py      # Google Calendar integration agent
│   ├── memory/
│   │   ├── short_memory.py        # In-memory storage for current session
│   │   └── long_memory.py         # MongoDB-based long-term memory storage
│   ├── schemas/
│   │   ├── request.py             # Models for requests
│   │   ├── response.py            # Models for responses
│   │   └── memory.py              # Schema for memory storage in MongoDB
│   ├── core/
│   │   ├── config.py              # Configuration (API keys, env vars)
│   │   ├── tools.py               # Shared utilities (logging, retry, etc.)
│   │   └── llm.py                 # LangChain LLM configuration
│   └── services/
│       └── planner.py            # LLM-based planner for routing tasks
├── tests/
│   ├── test_routing.py            # Tests for PeerAgent routing
│   ├── test_search.py             # Tests for SearchAgent
│   ├── test_calendar.py           # Tests for CalendarAgent
│   └── test_endpoints.py          # Integration tests for API endpoints
├── .env                           # Environment variables (API keys, DB URI)
├── Dockerfile                     # Docker configuration for the app
├── docker-compose.yml             # Docker Compose for FastAPI + MongoDB
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation and setup instructions
```

## Setup Instructions

### Prerequisites

- Python 3.11+
- MongoDB
- OpenAI API key
- Serper.dev API key (optional)
- Google Calendar API credentials (optional)

### Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and configure your API keys
6. Start MongoDB
7. Run the application: `python -m app.main`

### Docker Setup

1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

## API Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `POST /v1/agent/execute` - Execute agent tasks

## Development

- Run tests: `pytest`
- Format code: `black .`
- Lint code: `flake8`

## TODO

- [ ] Implement base agent class
- [ ] Implement peer agent routing
- [ ] Implement search agent
- [ ] Implement calendar agent
- [ ] Implement memory management
- [ ] Implement API endpoints
- [ ] Add comprehensive tests
- [ ] Add documentation 