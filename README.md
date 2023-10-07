# Django To-do app
A to-do app using the Django framework.

![App demonstration in gif](https://github.com/cyber-kevin/django-to-do/blob/main/app-demonstration.gif)

This README provides instructions on how to set up and initialize the project.

## Prerequisites

Before getting started, make sure you have the following prerequisites installed on your system:

- Python 3
- pip

## Installation

1. Clone the repository to your local machine:
```
https://github.com/cyber-kevin/django-to-do.git
```

2. Navigate to the project directory:
```
cd django-to-do/
```

3. Create a virtual environment (optional but recommended):
```
python -m venv venv
```

4. Activate the virtual environment:

  - On macOS and Linux:
  ```
  source venv/bin/activate
  ```
  - On Windows (Command Prompt):
  ```
  venv\Scripts\activate
  ```

5. Install project dependencies from the `requirements.txt` file:
```
pip install -r requirements.txt
```

## Database Migration

This project uses Django's built-in database migration system to manage the database schema. To apply initial migrations and set up the database, run the following commands:
```
python manage.py makemigrations
python manage.py migrate
```

## Running the Project

To run the Django project locally, use the following command:
```
python manage.py runserver
```

This will start the development server, and you can access the project by opening a web browser and navigating to `http://localhost:8000/tasks`. The project should now be up and running.
