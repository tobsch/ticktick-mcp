ARG BUILD_FROM
FROM ${BUILD_FROM}

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

COPY main.py config.py tools.py ./
COPY run.sh /

RUN chmod a+x /run.sh

CMD ["/run.sh"]

LABEL \
    io.hass.name="TickTick MCP" \
    io.hass.description="Model Context Protocol server for TickTick task management" \
    io.hass.version="1.0.0" \
    io.hass.type="addon"
