import os
import click
from dotenv import load_dotenv
from binance_mcp_server.server import mcp


@click.command()
@click.option("--api-key", required=True, help="Binance API key")
@click.option("--api-secret", required=True, help="Binance API secret")
def main(api_key, api_secret):
    """Launch the MetaTrader MCP STDIO server."""
    load_dotenv()

    os.environ["api_key"] = str(api_key)
    os.environ["api_secret"] = api_secret

    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()