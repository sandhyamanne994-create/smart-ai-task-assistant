
from app.database.db import get_connection, create_table

# Ensure the database table exists
create_table()


# Feature 1: Create a new task with priority
def create_task(task_name: str, priority: str = "Medium"):

    allowed_priorities = ["High", "Medium", "Low"]

    if priority not in allowed_priorities:
        return {"error": "Invalid priority"}

    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO tasks (task, completed, priority)
        VALUES (?, ?, ?)
        """,
        (task_name, False, priority)
    )

    task_id = cursor.lastrowid
    connection.commit()

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    return dict(task)


# Feature 2: Get all tasks
def get_tasks():

    connection = get_connection()

    rows = connection.execute(
        "SELECT * FROM tasks ORDER BY id"
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]


# Feature 3: Complete a task
def complete_task(task_id: int):

    connection = get_connection()

    cursor = connection.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return {"error": "Task not found"}

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    connection.close()

    return dict(task)


# Feature 4: Delete a task
def delete_task(task_id: int):

    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    if cursor.rowcount == 0:
        return {"error": "Task not found"}

    return {"message": "Task deleted successfully"}
