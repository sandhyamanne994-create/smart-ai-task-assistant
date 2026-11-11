
import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "app.mcp_server.server"]
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print("Connected to MCP Server!")

            print("\nTesting remove_task tool:")

            delete_result = await session.call_tool(
                "remove_task",
                arguments={
                    "task_id": 5
                }
            )

            print(delete_result.content)

if __name__ == "__main__":
    asyncio.run(main())
