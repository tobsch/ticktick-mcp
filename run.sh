#!/usr/bin/with-contenv bashio

export TICKTICK_API_KEY="$(bashio::config 'ticktick_api_key')"
export MCP_PORT="$(bashio::config 'port')"
export TIMEZONE="$(bashio::config 'timezone')"

bashio::log.info "Starting TickTick MCP server on port ${MCP_PORT}..."

exec python3 /app/main.py
