import httpx

from mcp.server import FastMCP

mcp = FastMCP("mcp-httpx")
CONTENT_TYPE = "application/json"


def success_response(message, status_code=None, response_text=None):
    result = [message]
    if status_code:
        result.append(f"Status: {status_code}")
    if response_text:
        result.append(f"Response: {response_text[:1000]}{'...' if len(response_text) > 1000 else ''}")
    return {"content": result, "isError": False}


def error_response(message):
    return {"content": [message], "isError": True}


@mcp.tool(description='Executes a GET request for the specified URL')
async def get_request(url: str) -> dict | None:
    """
    Perform GET request for given url

    Args:
        url: url is a structured representation of a web address with components like scheme, host, and path
        ( e.g. "https://example.com/path?query=value")

    Returns:
        Dictionary containing url, status code and response body.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            return success_response(
                f"GET request to {url}",
                response.status_code,
                response.text
            )
        except Exception as e:
            return error_response(f"GET request failed: {str(e)}")


@mcp.tool(description='Executes a POST request for the specified URL with a given payload')
async def post_request(url: str, data: dict, token: str = "", headers: dict = {}) -> dict | None:
    """
    Perform POST request for given url and payload

    Args:
        url: url is a structured representation of a web address with components like scheme, host, and path
        ( e.g. "https://example.com/path")
        data: data refers to payload, the request body data( e.g. {"key": "value"})
        token: Optional token to be used for authentication
        headers: Optional headers are case-insensitive key-value pairs that represent HTTP header fields in requests and
        responses, allowing you to set metadata like content type, authentication credentials, and other protocol information(e.g. {"my-custom-header": "header"})

    Returns:
        Dictionary containing url, status code and response body.
    """
    # Prepare headers
    request_headers = {"Content-Type": CONTENT_TYPE}

    # Add token if provided
    if token:
        request_headers["Authorization"] = f"Bearer {token}"

    if headers:
        request_headers.update(headers)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=data, headers=request_headers)
            return success_response(
                f"POST request to {url}",
                response.status_code,
                response.text
            )
        except Exception as e:
            return error_response(f"POST request failed: {str(e)}")


@mcp.tool(description='Executes a PUT request for the specified URL with a given payload')
async def put_request(url: str, data: dict, token: str = "", headers: dict = {}) -> dict | None:
    """
    Perform PUT request for given url and payload

    Args:
        url: url is a structured representation of a web address with components like scheme, host, and path
        ( e.g. "https://example.com/path")
        data: data refers to payload, the request body data( e.g. {"key": "value"})
        token: Optional token to be used for authentication
        headers: Optional headers are case-insensitive key-value pairs that represent HTTP header fields in requests and
        responses, allowing you to set metadata like content type, authentication credentials, and other protocol information(e.g. {"my-custom-header": "header"})

    Returns:
        Dictionary containing url, status code and response body.
    """

    request_headers = {"Content-Type": CONTENT_TYPE}
    if token:
        request_headers["Authorization"] = f"Bearer {token}"
    if headers:
        request_headers.update(headers)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.put(url, json=data, headers=request_headers)
            return success_response(
                f"PUT request to {url}",
                response.status_code,
                response.text
            )
        except Exception as e:
            return error_response(f"PUT request failed: {str(e)}")


@mcp.tool(description='Executes a PATCH request for the specified URL with a given payload')
async def patch_request(url: str, data: dict, token: str = "", headers: dict = {}) -> dict | None:
    """
    Perform PATCH request for given url and payload

    Args:
        url: url is a structured representation of a web address with components like scheme, host, and path
        ( e.g. "https://example.com/path")
        data: data refers to payload, the request body data( e.g. {"key": "value"})
        token: Optional token to be used for authentication
        headers: Optional headers are case-insensitive key-value pairs that represent HTTP header fields in requests and
        responses, allowing you to set metadata like content type, authentication credentials, and other protocol information(e.g. {"my-custom-header": "header"})

    Returns:
        Dictionary containing url, status code and response body.
    """

    request_headers = {"Content-Type": CONTENT_TYPE}
    if token:
        request_headers["Authorization"] = f"Bearer {token}"
    if headers:
        request_headers.update(headers)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.patch(url, json=data, headers=request_headers)
            return success_response(
                f"PATCH request to {url}",
                response.status_code,
                response.text
            )
        except Exception as e:
            return error_response(f"PATCH request failed: {str(e)}")


@mcp.tool(description='Executes a DELETE request for the specified URL')
async def delete_request(url: str, token: str = "", headers: dict = {}) -> dict | None:
    """
    Perform DELETE request for given url

    Args:
        url: url is a structured representation of a web address with components like scheme, host, and path
        ( e.g. "https://example.com/path")
        token: Optional token to be used for authentication
        headers: Optional headers are case-insensitive key-value pairs that represent HTTP header fields in requests and
        responses, allowing you to set metadata like content type, authentication credentials, and other protocol information(e.g. {"my-custom-header": "header"})

    Returns:
        Dictionary containing url, status code and response body.
    """

    request_headers = {}
    if token:
        request_headers["Authorization"] = f"Bearer {token}"
    if headers:
        request_headers.update(headers)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url, headers=request_headers)
            return success_response(
                f"DELETE request to {url}",
                response.status_code,
                response.text
            )
        except Exception as e:
            return error_response(f"DELETE request failed: {str(e)}")


def main():
    import asyncio
    asyncio.run(mcp.run_stdio_async())


if __name__ == "__main__":
    main()
