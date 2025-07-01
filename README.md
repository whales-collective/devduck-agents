# DevDuck agents

A multi-agent system for Go programming assistance built with Google Agent Development Kit (ADK). This project features a coordinating agent (DevDuck) that manages two specialized sub-agents (Bob and Cerebras) for different programming tasks.

<!--
This ADK project is composed by 3 agents:

- Devduck (the main agent), using Docker Model Runner
- Bob, a Golang expert, using Docker Model Runner
- Cerebras, a Golang Expert, using the Cerebras API
-->

## Architecture

The system consists of three main agents:

### 🦆 DevDuck (Main Agent)
- **Role**: Main development assistant and project coordinator
- **Model**: Qwen3 (unsloth/qwen3-gguf:4B-UD-Q4_K_XL)
- **Capabilities**: Routes requests to appropriate sub-agents based on user needs

### 👨‍💻 Bob Agent
- **Role**: General development tasks and project coordination
- **Model**: Qwen2.5 (ai/qwen2.5:latest)
- **Specialization**: Go programming expert for understanding code, explaining concepts, and generating code snippets

### 🧠 Cerebras Agent
- **Role**: Advanced computational tasks and complex problem-solving
- **Model**: Llama-4 Scout (llama-4-scout-17b-16e-instruct)
- **Provider**: Cerebras API
- **Specialization**: Go programming expert for complex problem-solving scenarios

## Features

- **Multi-agent coordination**: Routing between specialized agents
- **Go programming expertise**: All agents specialize in Go/Golang development
- **FastAPI web interface**: RESTful API with web interface support
- **Docker containerization**: Easy deployment with Docker Compose
- **Flexible model configuration**: Support for multiple LLM providers (local and cloud)

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Cerebras API key (for Cerebras agent)

### Configuration

1. **You need a Cerebras API Key**: https://cloud.cerebras.ai/
2. Create a `/agents/.env` file with the following content:

```env
CEREBRAS_API_KEY=<your_cerebras_api_key>
```

### ✋ All the prompts are define in the 🐙 compose file

### Start the services

```bash
cd agents
docker compose up
# if you updated the code, use --build
```

The application will be available at [http://0.0.0.0:8000](http://0.0.0.0:8000)


### Usage

The agents can be accessed through the web interface or API endpoints.

> Activate Token Streaming

**You can try this**:
```text
Hello I'm Phil

Bob generate a gloang hello world program

Add a human struct with a hello method

Cerebras can you analyse and comment this code

Can you generate the tests
```
> ✋ For a public demo, stay simple, the above examples are working.

#### Routing Requests

- **General requests**: Handled by DevDuck, who routes to appropriate sub-agents
- **Specific agent requests**: 
  - "I want to speak with Bob" → Routes to Bob agent
  - "I want to speak with Cerebras" → Routes to Cerebras agent
