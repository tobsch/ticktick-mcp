# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

TickTick MCP — a Model Context Protocol server that exposes TickTick task management as MCP tools. Built with Python, the `mcp` SDK (FastMCP), and served over SSE via Starlette/Uvicorn.

## Running the Server

```bash
pip install -r requirements.txt
python main.py          # starts SSE server on 0.0.0.0:58321
```

Requires a `.env` file with `TICKTICK_API_KEY=<oauth_access_token>`. The token is obtained via `auth.py` using the `ticktick-py` OAuth2 flow.

## Architecture

- **main.py** — Creates the FastMCP server instance, registers all tools, sets up SSE transport with Starlette routes (`/sse` and `/messages/`), and runs Uvicorn.
- **tools.py** — All MCP tool implementations. Each tool is an async function decorated with `@mcp.tool()` that makes HTTP requests to the TickTick Open API (`https://api.ticktick.com/open/v1`). Uses `httpx.AsyncClient` for all API calls.
- **config.py** — Loads `TICKTICK_API_KEY` from `.env` via `python-decouple` and builds the shared `HEADERS` dict and `TICKTICK_API_BASE` URL.
- **auth.py** — Standalone script to obtain an OAuth access token using `ticktick-py`.

## Adding New Tools

1. Define an async function in `tools.py` with the `@mcp.tool()` decorator.
2. Register it in `main.py` with `mcp.add_tool(your_function)`.

## Key Patterns

- All TickTick API calls use the shared `HEADERS` and `TICKTICK_API_BASE` from `config.py`.
- Tools use `httpx.AsyncClient` as a context manager per-call (no shared client).
- TickTick date format: `"2019-11-13T03:00:00+0000"` — note the `+0000` without colon needs conversion to `+00:00` for Python's `fromisoformat`.
- Most task operations require both `project_id` and `task_id`.
