import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from app.task_suggestions import suggest_subtasks

from app.tools.task_tool import (
    create_task,
    get_tasks,
    complete_task,
    delete_task
)

# Page Configuration
st.set_page_config(
    page_title="Smart AI Task Assistant",
    page_icon="🤖",
    layout="centered"
)

# Application Title
st.title("🤖 Smart AI Task Assistant")
st.write("Welcome! Manage your daily tasks easily.")

# Dashboard Summary
st.divider()
st.subheader("📊 Task Dashboard")

# Get all tasks from SQLite Database
dashboard_tasks = get_tasks()

# Calculate task counts
total_tasks = len(dashboard_tasks)

completed_tasks = sum(
    1 for task in dashboard_tasks
    if task["completed"]
)

pending_tasks = total_tasks - completed_tasks

# Calculate progress
if total_tasks > 0:
    progress = completed_tasks / total_tasks
else:
    progress = 0.0

# Display Dashboard Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Tasks", total_tasks)
col2.metric("Pending Tasks", pending_tasks)
col3.metric("Completed Tasks", completed_tasks)

# Display Progress Bar
st.write("### 📈 Overall Progress")

st.progress(progress)

st.caption(f"{progress:.0%} Tasks Completed")

st.divider()

# Feature 1: Add Task
st.header("➕ Add New Task")

task_name = st.text_input(
    "Enter your task",
    placeholder="Example: Complete Python homework"
)

task_priority = st.selectbox(
    "Select Task Priority",
    ["High", "Medium", "Low"],
    index=1
)

if st.button("Add Task"):
    if task_name.strip():
        result = create_task(task_name.strip(), task_priority)
        st.success("Task added successfully!")
        st.rerun()
    else:
        st.warning("Please enter a task name.")

st.divider()
st.divider()
st.header("✨ AI Task Suggestions")

suggestion_task = st.text_input(
    "Enter a task to get suggestions",
    placeholder="Example: Prepare for Hackathon",
    key="suggestion_task"
)

if st.button("Generate Suggestions"):
    if suggestion_task.strip():
        suggestions = suggest_subtasks(suggestion_task)

        st.write("### Suggested Steps")

        for index, suggestion in enumerate(suggestions, start=1):
            st.write(f"{index}. {suggestion}")
    else:
        st.warning("Please enter a task first.")

st.divider()

# Feature 2: View Tasks
st.header("📋 My Tasks")

tasks = get_tasks()
# Sort tasks by priority
priority_order = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}

tasks = sorted(
    tasks,
    key=lambda task: priority_order.get(
        task["priority"], 2
    )
)

if tasks:
    for task in tasks:
        task_id = task["id"]
        task_text = task["task"]
        completed = task["completed"]
        priority = task["priority"]

        st.write(f"**Task ID:** {task_id}")
        st.write(f"**Task:** {task_text}")
        st.write(f"**Priority:** {priority}")

        if completed:
            st.success("Status: Completed")
        else:
            st.info("Status: Pending")

        # Feature 3: Complete Task
        if not completed:
            if st.button("Complete Task", key=f"complete_{task_id}"):
                complete_task(task_id)
                st.success("Task completed!")
                st.rerun()

        # Feature 4: Delete Task
        if st.button("Delete Task", key=f"delete_{task_id}"):
            delete_task(task_id)
            st.success("Task deleted!")
            st.rerun()

        st.divider()
else:
    st.info("No tasks available. Add your first task above!")

# Footer
st.caption("Built with Python, Streamlit and SQLite")
