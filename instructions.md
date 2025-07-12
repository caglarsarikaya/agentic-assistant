Below is a step-by-step guide to creating an agentic assistant system with short-term and long-term memory, session management using MongoDB, and dynamic routing via LangChain. This guide includes a detailed folder structure and setup process without any code, as requested. The system will handle various queries (e.g., direct LLM responses, web searches, calendar interactions) based on your needs.

---

### Folder Structure
Here’s the recommended folder structure for the project:

```
agentic-assistant/
│
├── app/
│   ├── main.py                     # FastAPI entrypoint
│   ├── api/
│   │   └── routes.py              # API routes (e.g., POST /v1/agent/execute)
│   ├── agents/
│   │   ├── base.py                # BaseAgent with memory and session helpers
│   │   ├── peer_agent.py          # PeerAgent: LLM-based planner and router
│   │   ├── llm_agent.py           # LLM-only agent for direct responses
│   │   ├── search_agent.py        # Web search agent (e.g., Serper.dev)
│   │   └── calendar_agent.py      # Google Calendar integration agent
│   ├── memory/
│   │   ├── short_memory.py        # In-memory storage for current session
│   │   └── long_memory.py         # MongoDB-based long-term memory storage
│   ├── schemas/
│   │   ├── request.py             # Models for requests (e.g., TaskRequest)
│   │   ├── response.py            # Models for responses (e.g., TaskResponse)
│   │   └── memory.py              # Schema for memory storage in MongoDB
│   ├── core/
│   │   ├── config.py              # Configuration (API keys, env vars)
│   │   ├── tools.py               # Shared utilities (logging, retry, etc.)
│   │   └── llm.py                 # LangChain LLM configuration
│   └── services/
│       └── planner.py            # LLM-based planner for routing tasks
│
├── tests/
│   ├── test_routing.py            # Tests for PeerAgent routing
│   ├── test_search.py             # Tests for SearchAgent
│   ├── test_calendar.py           # Tests for CalendarAgent
│   └── test_endpoints.py          # Integration tests for API endpoints
│
├── .env                           # Environment variables (API keys, DB URI)
├── Dockerfile                     # Docker configuration for the app
├── docker-compose.yml             # Docker Compose for FastAPI + MongoDB
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation and setup instructions
```

---

### Step-by-Step Guide

#### **Step 1: Project Initialization**
- Create a root directory named `agentic-assistant`.
- Inside it, create an `app` directory with the following subdirectories: `api`, `agents`, `memory`, `schemas`, `core`, and `services`.
- Create a `tests` directory at the root level.
- Add the files listed in the folder structure above (e.g., `app/main.py`, `app/api/routes.py`, etc.). Leave them empty or add minimal comments describing their purpose for now.

#### **Step 2: Environment Setup**
- Set up a virtual environment to isolate project dependencies.
- Install essential Python packages such as FastAPI, Uvicorn, LangChain, OpenAI, PyMongo, and Pydantic.
- Create a `requirements.txt` file to list all installed dependencies for easy replication.

#### **Step 3: Configuration**
- Create a `.env` file in the root directory to store sensitive information like API keys and database URIs (e.g., OpenAI key, MongoDB URI, Google Calendar credentials).
- In `app/core/config.py`, prepare to load these environment variables so they can be accessed throughout the application.

#### **Step 4: Schemas**
- In `app/schemas/request.py`, define the structure for incoming requests (e.g., a model with fields like `session_id` and `task`).
- In `app/schemas/response.py`, define the structure for API responses (e.g., a model with fields like `agent_type`, `success`, and `result`).
- In `app/schemas/memory.py`, define the structure for storing memory data in MongoDB (e.g., session history with timestamps).

#### **Step 5: Memory Management**
- In `app/memory/short_memory.py`, set up a mechanism to store session-specific data in memory (e.g., a dictionary tied to a `session_id`).
- In `app/memory/long_memory.py`, prepare to handle long-term memory storage and retrieval using MongoDB, linking data to session IDs.

#### **Step 6: Agents**
- In `app/agents/base.py`, establish a foundation for all agents with shared functionality, such as accessing memory.
- In `app/agents/peer_agent.py`, create the `PeerAgent` to analyze tasks using an LLM and route them to the appropriate agents.
- In `app/agents/llm_agent.py`, set up the `LLMAgent` for direct responses to queries without external tools.
- In `app/agents/search_agent.py`, prepare the `SearchAgent` to fetch real-time information from a web search API (e.g., Serper.dev).
- In `app/agents/calendar_agent.py`, configure the `CalendarAgent` to manage Google Calendar interactions (e.g., adding events).

#### **Step 7: Services**
- In `app/services/planner.py`, develop the planning logic for the `PeerAgent` to determine which agents to use and in what order, based on the task.

#### **Step 8: API Routes**
- In `app/api/routes.py`, define the API endpoints. Create a primary endpoint (e.g., POST `/v1/agent/execute`) that:
  - Accepts a `session_id` and `task`.
  - Retrieves relevant memory data.
  - Routes the task through the `PeerAgent`.
  - Returns the result.

#### **Step 9: Core Utilities**
- In `app/core/tools.py`, include reusable utilities like logging or retry logic for robustness.
- In `app/core/llm.py`, configure the LLM integration (e.g., LangChain setup with model and API key details).

#### **Step 10: FastAPI Application**
- In `app/main.py`, initialize the FastAPI app:
  - Link the routes defined in `app/api/routes.py`.
  - Set up any startup tasks, like connecting to MongoDB.

#### **Step 11: Testing**
- In the `tests` directory, prepare unit tests for each agent (e.g., `test_routing.py` for `PeerAgent`, `test_search.py` for `SearchAgent`).
- Add integration tests in `test_endpoints.py` to verify the API endpoints work end-to-end.

#### **Step 12: Dockerization**
- Create a `Dockerfile` in the root directory to package the FastAPI application.
- In `docker-compose.yml`, define services for the FastAPI app and MongoDB, ensuring they can connect.

#### **Step 13: Documentation**
- In `README.md`, write:
  - Instructions for setting up the environment and installing dependencies.
  - Steps to run the app locally or with Docker.
  - Examples of how to interact with the API.

---

This guide provides a clear roadmap to set up your agentic assistant system. Each step focuses on a specific component, ensuring the project is well-organized and functional without requiring code at this stage. Let me know if you need more details!