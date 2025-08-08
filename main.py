import asyncio
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Check if the environment variable is loaded
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print(f"OPENAI_API_KEY loaded successfully: {api_key}")
else:
    print("OPENAI_API_KEY not found. Please check your .env file.")
    print("Make sure you have a .env file in your project root with:")
    print("OPENAI_API_KEY=your_actual_api_key_here")

async def main():
    print("Hello from langchain-mcp-adapter!")
    
if __name__ == "__main__":
    asyncio.run(main())
