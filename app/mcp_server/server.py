from mcp.server.fastmcp import FastMCP

from app.tools.task_tool import (
    create_task,
    get_tasks,
    complete_task,
    delete_task
)

# Create MCP Server
mcp = FastMCP("Smart AI Task Assistant")


@mcp.tool()
def add_task(task_name: str):
    """Create a new task."""
    return create_task(task_name)


@mcp.tool()
def list_tasks():
    """Get all tasks."""
    return get_tasks()


@mcp.tool()
def finish_task(task_id: int):
    """Mark a task as completed."""
    return complete_task(task_id)


@mcp.tool()
def remove_task(task_id: int):
    """Delete a task."""
    return delete_task(task_id)


if __name__ == "__main__":
    mcp.run()