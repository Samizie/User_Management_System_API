

# User Management System API

## Overview
The **User Management System API** is a RESTful API built with Django and Django REST Framework. It provides functionalities for creating, retrieving, updating, and deleting users. This API is designed to handle user data securely and efficiently, supporting standard CRUD operations.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [Accessing the Application](#accessing_the_application)
- [API Endpoints](#api-endpoints)
  - [User Management](#user-management)
- [Testing](#testing)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Features
- Create a new user
- Retrieve a list of users
- Retrieve user details by ID or username
- Update user information
- Delete a user
- Error handling for common issues

## Technologies
- **Django**: Web framework
- **Django REST Framework**: Toolkit for building Web APIs
- **SQLite**: Default database: SQLite
- **Pytest**: Testing framework: Unittest
- **Swaggerdocs**: OpenAPI documentation

## Getting Started

### Prerequisites
Ensure you have the following installed on your local machine:
- Python 3.8 or higher
- Django 4.x
- Virtualenv (optional but recommended)

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Samizie/User_Management_System_API.git
   cd User_Management_System_API
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

### Running the Application on Local
To run the development server, use:
```bash
python manage.py runserver
```
The API will be accessible at `http://127.0.0.1:8000/`.


### Accessing the Application
To use, check password in supruser.txt file:


### Documentation
swaggerdocs file needs authentication (superusr.txt file)
Access swaggerdocs implementation on `Samilincoln.pythonanywhere.com/swagger/`

## API Endpoints
API is live on `Samilincoln.pythonanywhere.com`

### User Management

- **List Users**
  - `GET /users/`
  - Retrieves a list of all users.

- **Create User**
  - `POST /users/create/`
  - Creates a new user with the required fields (e.g., username, email, password).

- **Retrieve User by ID**
  - `GET /user/<id>/`
  - Retrieves details of a user by their ID.

- **Retrieve User by Username**
  - `GET /user/?username=<username>`
  - Retrieves details of a user by their username.

- **Update User**
  - `PUT /user/update/<id>/`
  - pass new name into request body
  .Updates user name

- **Delete User**
  - `DELETE /user/delete/<id>/`
  - Deletes a user by their ID.

### Example JSON for Creating/Updating User:
```json
{
  "id": 1,
  "name": "John",
}
```

## Testing
To run tests, use the following command:
```bash
python manage.py test
```
This will run all unit tests and ensure that your application behaves as expected.

## Error Handling
The API provides detailed error messages for incorrect input or failed operations. Common errors include:
- **400 Bad Request**: Invalid input data.
- **404 Not Found**: Resource not found.
- **500 Internal Server Error**: An unexpected error occurred.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
