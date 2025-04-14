markdown

Copy
# Task Manager API

A Django-based RESTful API for a task management system, built with Django REST Framework. Users can create tasks, assign tasks to users, and retrieve tasks assigned to a specific user.

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip
- Virtualenv (recommended)
- VSCode (recommended)

### Installation
1. Clone the repository or unzip the project folder:
   ```bash
   git clone https://github.com/mano-achanta/task-manager-api.git
   cd task_manager
Create and activate a virtual environment:
bash

Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
bash

Copy
pip install -r requirements.txt
Apply migrations:
bash

Copy
python manage.py makemigrations
python manage.py migrate
Create a superuser:
bash

Copy
python manage.py createsuperuser
Run the development server:
bash

Copy
python manage.py runserver
API Endpoints
Create Task: POST /api/tasks/
Example Request:
json

Copy
{
    "name": "Complete Project Proposal",
    "description": "Draft the project proposal for client X.",
    "task_type": "URGENT",
    "assigned_user_ids": [1]
}
Example Response (201 Created):
json

Copy
{
    "id": 1,
    "name": "Complete Project Proposal",
    "description": "Draft the project proposal for client X.",
    "created_at": "2025-04-14T10:00:00Z",
    "task_type": "URGENT",
    "completed_at": null,
    "status": "PENDING",
    "assigned_users": [
        {
            "id": 1,
            "username": "user1",
            "name": "John",
            "email": "user1@example.com",
            "mobile": "1234567890",
            "first_name": "John"
        }
    ],
    "assigned_user_ids": [1]
}
Assign Task: POST /api/tasks/<task_id>/assign/
Example Request:
json

Copy
{
    "user_ids": [1, 2]
}
Example Response (200 OK):
json

Copy
{
    "id": 1,
    "name": "Complete Project Proposal",
    "description": "Draft the project proposal for client X.",
    "created_at": "2025-04-14T10:00:00Z",
    "task_type": "URGENT",
    "completed_at": null,
    "status": "PENDING",
    "assigned_users": [
        {
            "id": 1,
            "username": "user1",
            "name": "John",
            "email": "user1@example.com",
            "mobile": "1234567890",
            "first_name": "John"
        },
        {
            "id": 2,
            "username": "user2",
            "name": "Jane",
            "email": "user2@example.com",
            "mobile": "0987654321",
            "first_name": "Jane"
        }
    ],
    "assigned_user_ids": [1, 2]
}
Get User Tasks: GET /api/tasks/user/<user_id>/
Example Request: GET /api/tasks/user/1/
Example Response (200 OK):
json

Copy
[
    {
        "id": 1,
        "name": "Complete Project Proposal",
        "description": "Draft the project proposal for client X.",
        "created_at": "2025-04-14T10:00:00Z",
        "task_type": "URGENT",
        "completed_at": null,
        "status": "PENDING",
        "assigned_users": [
            {
                "id": 1,
                "username": "user1",
                "name": "John",
                "email": "user1@example.com",
                "mobile": "1234567890",
                "first_name": "John"
            },
            {
                "id": 2,
                "username": "user2",
                "name": "Jane",
                "email": "user2@example.com",
                "mobile": "0987654321",
                "first_name": "Jane"
            }
        ]
    }
]
Test Credentials
Superuser: admin / password123 (email: admin@example.com, mobile: 1234567890)
Test Users:
user1 / pass123 (email: user1@example.com, mobile: 1234567890, first_name: John)
user2 / pass123 (email: user2@example.com, mobile: 0987654321, first_name: Jane)
Running Tests
bash

Copy
python manage.py test
Project Structure
manage.py: Django command-line utility.
task_manager/: Project settings and configuration.
tasks/: App containing models, serializers, views, and URLs.
requirements.txt: Project dependencies.
README.md: This file.
.gitignore: Ignored files for Git.
Notes
Uses SQLite by default (no separate installation needed).
Authentication is disabled for simplicity. Enable IsAuthenticated in views.py for production
