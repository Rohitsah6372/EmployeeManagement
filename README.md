# Employee Management

## Introduction
**Employee Management** is a Django-based web application that helps manage employee records, including their details, roles, and departments.

## Features
- Employee registration and management
- Role-based access control
- Database integration with SQLite
- RESTful API support
- Admin panel for easy management

## Tech Stack
- **Backend:** Python, Django
- **Database:** SQLite
- **Tools:** Django ORM, Django Admin

## Installation

### Prerequisites
- Python 3
- pip (Python package manager)

### Steps to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/EmployeeManagement.git
   cd EmployeeManagement
   ```

2. Create a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```sh
   python manage.py migrate
   ```

5. Start the Django development server:
   ```sh
   python manage.py runserver
   ```

6. Access the application at:
   ```
   http://127.0.0.1:8000/
   ```

## API Endpoints
| Method | Endpoint          | Description               |
|--------|------------------|---------------------------|
| GET    | /employees       | Get all employees        |
| POST   | /employees/add   | Add a new employee       |
| GET    | /employees/{id}  | Get employee details     |
| PUT    | /employees/{id}  | Update employee details  |
| DELETE | /employees/{id}  | Delete an employee       |

## Contributing
Feel free to contribute by submitting a pull request.

