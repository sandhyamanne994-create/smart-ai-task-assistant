def suggest_subtasks(task_name: str):
    """Suggest smaller tasks using simple Python rules."""

    task = task_name.lower().strip()

    if not task:
        return ["Please enter a task name."]

    if any(word in task for word in ["hackathon", "project", "app"]):
        return [
            "Review project requirements",
            "Plan the main features",
            "Build and test the code",
            "Prepare a project demo"
        ]

    elif any(word in task for word in ["study", "exam", "homework"]):
        return [
            "Review the topics",
            "Create a study plan",
            "Practice important questions",
            "Review your answers"
        ]

    elif any(word in task for word in ["presentation", "report"]):
        return [
            "Collect the required information",
            "Create an outline",
            "Prepare the content",
            "Review and finalize the work"
        ]

    else:
        return [
            "Break the task into smaller steps",
            "Complete the first step",
            "Review your progress",
            "Finish and verify the task"
        ]