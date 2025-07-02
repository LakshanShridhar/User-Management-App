# User-Management-App

A User Management API with secure sign-up, login, password change, and profile editing functionality. Built using RESTful endpoints and backed by a SQL database. Includes unit tests and follows a professional Git branching workflow with pull requests.

## Project Structure

User-Management-App/
├── .gitignore
├── LICENSE
├── README.md
├── change_password.py
├── database.py
├── login.py
├── profile_edit.py
├── requirements.txt
├── signup.py
├── test_change_password.py
├── test_login.py
├── test_profile_edit.py
├── test_signup.py
└── users.db

## Features

- User Signup with email verification and hashed passwords
- User Login with credential validation
- Change Password functionality with current password verification
- Profile Editing for updating user information
- Secure password hashing using bcrypt
- SQLite database backend with SQLAlchemy ORM
- Comprehensive unit tests for all endpoints
- Clean and professional Git workflow with feature branches and pull requests

## Getting Started

1. Clone the repository:

   git clone https://github.com/LakshanShridhar/User-Management-App.git
   cd User-Management-App

2. Install dependencies:

   pip install -r requirements.txt

3. Run the FastAPI app:

   uvicorn main:app --reload

4. Run tests:

   pytest

## API Endpoints

Endpoint            Method   Description
------------------  -------  ---------------------------------
/signup             POST     Create a new user account
/login              POST     User login
/change-password    POST     Change user password
/profile-edit       POST     Edit user profile information

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.
