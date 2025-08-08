import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Load environment variables from .env file
load_dotenv()

llm = ChatOpenAI()
stdio_server_params = StdioServerParameters(
    command= "python",
    args= ["/Users/tenzinyounten/Documents/AI/mcp-servers/langchain-mcp/langchain-mcp-adapter/servers/math_server.py"],
    env= {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
    }
)

# Check if the environment variable is loaded
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print(f"OPENAI_API_KEY loaded successfully: {api_key}")


async def main():
    print("Hello from langchain-mcp-adapter!")
    
if __name__ == "__main__":
    asyncio.run(main())
