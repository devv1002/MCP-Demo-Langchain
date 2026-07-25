from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")           # Naam h server ka bss

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the weather location."""
    return "It's always raining in California"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")