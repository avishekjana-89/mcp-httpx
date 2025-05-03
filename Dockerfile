# Stage 1: Build with uv
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS uv

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Use bind mounts for lockfile and config
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev --no-editable

ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-editable

# Stage 2: Slim runtime
FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy dependencies and virtual environment from build stage
COPY --from=uv /root/.local /root/.local
COPY --from=uv /app/.venv /app/.venv
COPY --from=uv /usr/local/bin/uv /usr/local/bin/uv

# Make sure app user exists if needed (optional)
# RUN useradd -ms /bin/bash app

# Set up environment
ENV PATH="/app/.venv/bin:/root/.local/bin:/usr/local/bin:$PATH"

# Copy project source code
COPY . /app/mcp-httpx

ENTRYPOINT ["uv", "--directory", "./mcp-httpx/src/mcp-httpx", "run", "server.py"]
