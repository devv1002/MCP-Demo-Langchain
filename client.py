import math
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"],                  ## Ensure correct absolute path
                "transport":"stdio"
            },
            "weather": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http",
            },
        }
    )

    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools=await client.get_tools()

    print(tools)
    print(len(tools))
    for t in tools:
        print(t.name)

    model=ChatGroq(model="openai/gpt-oss-20b")
    agent=create_react_agent(
        model,tools
    )

    math_response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Use the get_weather tool to tell me the weather in California. Do not answer from your own knowledge."
                }
            ]
        }
    )
    print("Math response:", math_response['messages'][-1].content)

asyncio.run(main())