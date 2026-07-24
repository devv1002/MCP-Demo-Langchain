from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int,b:int) -> int:
    """_summary_
    Add to numbers
    """
    return a + b