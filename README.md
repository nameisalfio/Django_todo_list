# Django-Based Task Management Application

## Overview

This document outlines the structure and functionality of a web-based task management system, commonly known as a "Todo List." This application has been developed using the Django framework for Python, with SQLite serving as the database for task storage. The system allows users to create, view, update, delete, and reorder tasks through a user-friendly web interface.

## Directory Structure

```bash
Django_todo_list
├── README.md
└── todo_list
    |
    ├── db.sqlite3
    ├── manage.py
    ├── static
    │   ├── css
    │   │   └── style.css
    │   ├── favicon.ico
    │   ├── img
    │   │   └── mission.png
    │   └── js
    │       └── script.js
    ├── tasks
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── templates
    │   ├── about.html
    │   ├── base.html
    │   ├── task_confirm_delete.html
    │   ├── task_detail.html
    │   ├── task_form.html
    │   └── tasks_list.html
    └── todo_list
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── views.py
        └── wsgi.py

    12 directories, 56 files
```


## Key Components

- `manage.py`: The command-line utility for interacting with the Django project.
- `static/`: Contains static assets like CSS files, JavaScript, and images.
  - `css/style.css`: Defines the application's visual styling.
  - `js/script.js`: Contains JavaScript code for interactive features, including drag and drop functionality.
  - `img/mission.png`: An image used in the application.
- `templates/`: Contains HTML templates for rendering the application's UI.
  - `about.html`: Page displaying information about the application.
  - `base.html`: Base template that other templates extend.
  - `task_confirm_delete.html`: Template for confirming task deletion.
  - `task_detail.html`: Page showing detailed information for individual tasks.
  - `task_form.html`: Form for creating or editing tasks.
  - `tasks_list.html`: Displays the main task list.
- `tasks/`: Contains application-specific code.
  - `models.py`: Defines the data models for tasks.
  - `views.py`: Contains view functions for handling requests and responses.
  - `urls.py`: Maps URL paths to views.
- `todo_list/`: Project-specific settings and configuration.
  - `settings.py`: Contains settings for the Django project.
  - `urls.py`: Maps URL paths to views across the entire project.
  - `wsgi.py`: Entry point for WSGI-compatible web servers.

## Prerequisites

Ensure you have Python (version 3.6 or higher) and pip installed on your system.

## Setup Instructions

1. Clone the repository:

```bash
git clone git@github.com/todo_list.git
cd Django_todo_list
```

2. Set up a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations to set up the database:

```bash
python manage.py migrate
```

5. Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

## Running the Application

To start the application, execute these commands in your terminal:

```bash
python manage.py runserver
```


Once running, you can access the application at <http://127.0.0.1:8000>.

## Key Features

1. **Create Tasks**: Use the form on the main page to add new tasks.
2. **View Task Details**: Click on a task to view more detailed information.
3. **Update Task Status**: Toggle between "Completed" and "Incomplete" states using the status button.
4. **Delete Tasks**: Remove tasks from the list with a confirmation prompt.
5. **Reorder Tasks**: Drag and drop tasks to rearrange their order in the list.

## Drag and Drop Functionality

The application includes a drag and drop mechanism for reordering tasks:

- Click and hold on a task to begin dragging.
- Move the task to the desired position in the list.
- Release to drop the task in its new position.
- The new order is automatically saved and persisted in the database.

This feature enhances the user experience by providing a more intuitive way to manage task priorities and organization.

## Contributing

I welcome contributions to this project. If you'd like to suggest improvements or report issues, please submit a pull request or open an issue through the appropriate channels.

## Conclusion

This Task Management Application, built on the Django framework, offers a robust solution for organizing personal or professional tasks. Its intuitive interface, powerful backend, and drag and drop functionality provide a seamless experience for managing and prioritizing daily activities. I encourage you to explore the full capabilities of this application and welcome your feedback for continuous improvement.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
