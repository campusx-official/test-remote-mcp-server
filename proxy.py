from fastmcp import FastMCP

# Create a proxy to your remote FastMCP Cloud server
# FastMCP Cloud uses Streamable HTTP (default), so just use the /mcp URL
mcp = FastMCP.as_proxy(
    "https://splendid-gold-dingo.fastmcp.app/mcp",  # Standard FastMCP Cloud URL
    name="Nitish Server Proxy"
)

if __name__ == "__main__":
    # This runs via STDIO, which Claude Desktop can connect to
    mcp.run()