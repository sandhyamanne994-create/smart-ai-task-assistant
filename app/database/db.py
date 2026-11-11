import sqlite3

DATABASE_NAME = "tasks.db"

def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = get_connection()

    # Create tasks table if it does not exist
    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN DEFAULT 0
        )
    """)

    # Check existing columns
    columns = [
        row["name"]
        for row in connection.execute(
            "PRAGMA table_info(tasks)"
        ).fetchall()
    ]

    # Add priority column without deleting old tasks
    if "priority" not in columns:
        connection.execute("""
            ALTER TABLE tasks
            ADD COLUMN priority TEXT DEFAULT 'Medium'
        """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_table()
    print("Database updated successfully!")