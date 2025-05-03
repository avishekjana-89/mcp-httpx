# HTTPX MCP Server

## 📋 Overview

The HTTPX MCP Server is an implementation of the Model Context Protocol (MCP) that performs REST API operations using the Python `httpx` library. It provides various methods for making HTTP requests, including `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.

<img width="1425" alt="image" src="https://github.com/user-attachments/assets/9d190617-cbbb-40e0-9f9e-cbeaaf2381b8" />

<img width="1426" alt="image" src="https://github.com/user-attachments/assets/557fee9f-929a-4571-9aa2-84b5821d0bc0" />

## 🚀 Quick Start

### Using `uv`:

```bash
git clone https://github.com/avishekjana-89/mcp-httpx.git
cd mcp-httpx
uv pip install .
```

### Using Docker:

```bash
git clone https://github.com/avishekjana-89/mcp-httpx.git
cd mcp-httpx
docker build -t mcp/httpx .
```

## 🛠️ Available Tools

The server provides the following core tools for interacting with web APIs:

### `get_request`
- **Description**: Executes a `GET` request for the specified URL.
- **Arguments**:
  - `url`: A structured URL with scheme, host, and path (e.g., `https://example.com/path?query=value`).
- **Returns**: A dictionary containing the URL, status code, and the response body.

### `post_request`
- **Description**: Executes a `POST` request for the specified URL with a given payload.
- **Arguments**:
  - `url`: A structured URL (e.g., `https://example.com/path`).
  - `data`: The payload to send with the request (e.g., `{"key": "value"}`).
  - `token`: Optional token for authentication.
  - `headers`: Optional HTTP headers as key-value pairs (e.g., `{"Content-Type": "application/json"}`).
- **Returns**: A dictionary containing the URL, status code, and the response body.

### `put_request`
- **Description**: Executes a `PUT` request for the specified URL with a given payload.
- **Arguments**:
  - `url`: A structured URL (e.g., `https://example.com/path`).
  - `data`: The payload to send with the request (e.g., `{"key": "value"}`).
  - `token`: Optional token for authentication.
  - `headers`: Optional HTTP headers as key-value pairs.
- **Returns**: A dictionary containing the URL, status code, and the response body.

### `patch_request`
- **Description**: Executes a `PATCH` request for the specified URL with a given payload.
- **Arguments**:
  - `url`: A structured URL (e.g., `https://example.com/path`).
  - `data`: The payload to send with the request (e.g., `{"key": "value"}`).
  - `token`: Optional token for authentication.
  - `headers`: Optional HTTP headers as key-value pairs.
- **Returns**: A dictionary containing the URL, status code, and the response body.

### `delete_request`
- **Description**: Executes a `DELETE` request for the specified URL.
- **Arguments**:
  - `url`: A structured URL (e.g., `https://example.com/path`).
  - `token`: Optional token for authentication.
  - `headers`: Optional HTTP headers as key-value pairs.
- **Returns**: A dictionary containing the URL, status code, and the response body.

## Usage with Claude Desktop

### Using `uv`

To run the MCP server using `uv`, add the following configuration to your `claude_desktop_config.json`:

```json
"mcpServers": {
  "mcp-httpx": {
    "command": "uv",
    "args": [
      "--directory",
      "parent_of_servers_repo/mcp-httpx/src/mcp-httpx",
      "run",
      "server.py"
    ]
  }
}
```

### Using Docker

To run the MCP server via Docker, add the following configuration to your `claude_desktop_config.json`:

```json
"mcpServers": {
  "mcp-httpx": {
    "command": "docker",
    "args": [
      "run",
      "-i",
      "--rm",
      "--name",
      "mcp-httpx",
      "mcp/httpx"
    ]
  }
}
```

## License

This MCP server is licensed under the MIT License. You are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please refer to the `LICENSE` file in the project repository.
