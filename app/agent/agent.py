from app.tools.task_tool import (
    create_task,
    get_tasks,
    complete_task,
    delete_task
)


class TaskAgent:

    def __init__(self):
        print("Smart AI Task Assistant Agent Started!")

    def process_command(self, command: str):

        command = command.lower().strip()

        if command.startswith("add "):
            task_name = command[4:]
            return create_task(task_name)

        elif command == "list":
            return get_tasks()

        elif command.startswith("complete "):
            task_id = int(command[9:])
            return complete_task(task_id)

        elif command.startswith("delete "):
            task_id = int(command[7:])
            return delete_task(task_id)

        else:
            return {
                "message": "Sorry, I don't understand that command."
            }


if __name__ == "__main__":

    agent = TaskAgent()

    result = agent.process_command("delete 3")

    print(result)