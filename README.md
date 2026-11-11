
# Smart AI Task Assistant

A smart task management application built with Python, FastAPI, Streamlit, SQLite, and Model Context Protocol (MCP).

## Project Overview

Smart AI Task Assistant helps users organize and manage their daily tasks. Users can create, view, complete, and delete tasks, assign priorities, track progress, and get suggestions to break larger tasks into smaller steps.

## Features

- Add, view, complete, and delete tasks
- Assign High, Medium, and Low priorities
- Sort tasks by priority
- Track task progress using a dashboard
- Get rule-based task suggestions
- Store tasks using SQLite
- Expose task operations through MCP tools
- FastAPI backend
- Streamlit user interface

## Technology Stack

- Python
- FastAPI
- Streamlit
- SQLite
- Model Context Protocol (MCP)
- Git and GitHub

## Project Structure

```text
smart-ai-task-assistant/
├── app/
│   ├── agent/
│   ├── database/
│   ├── mcp_server/
│   ├── tools/
│   ├── main.py
│   ├── streamlit_app.py
│   └── task_suggestions.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sandhyamanne994-create/smart-ai-task-assistant.git
```

2. Open the project folder:

```bash
cd smart-ai-task-assistant
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate it on Windows:

```cmd
.venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app/streamlit_app.py
```

Open the local URL displayed in your terminal.

## Run the FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## MCP Tools

The MCP server provides these task tools:

- `add_task`
- `list_tasks`
- `finish_task`
- `remove_task`

## Task Suggestions

The current task suggestion feature uses Python keyword-based rules to suggest smaller steps for common tasks such as projects, studying, and presentations.

## Future Improvements

- Integrate an LLM for more natural AI-powered task suggestions
- Add user authentication
- Add task deadlines and reminders
- Improve task recommendations

## Security

API keys and environment files should never be committed to GitHub. Local environment files and database files are excluded using `.gitignore`.

## Author

Created as a hackathon capstone project.
