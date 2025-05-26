from fastmcp import FastMCP


mcp = FastMCP(
    name="binance-mcp-server",
    version="1.0.0",
    description="MCP server for Binance"
)


@mcp.tool("ping")
def ping_tool():
    """
    Ping tool to check if the server is running.
    """
    return "pong"


if __name__ == "__main__":
    mcp.run(transport="stdio")