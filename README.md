# User-Management-App

A User Management API with secure sign-up, login, password change, and profile editing functionality. Built using RESTful endpoints and backed by a SQL database. Includes unit tests and follows a professional Git branching workflow with pull requests.

## Project Structure

| File/Folder            | Description                |
|-----------------------|----------------------------|
| User-Management-App/   | Root project directory     |
| .gitignore            | Git ignore rules           |
| LICENSE               | Project license            |
| README.md             | Project readme             |
| change_password.py    | Change password script      |
| database.py           | Database connection/script |
| login.py              | User login script          |
| profile_edit.py       | Profile editing script     |
| requirements.txt      | Python dependencies list   |
| signup.py             | User signup script         |
| test_change_password.py | Tests for change password  |
| test_login.py         | Tests for login functionality |
| test_profile_edit.py  | Tests for profile editing  |
| test_signup.py        | Tests for signup           |
| users.db              | SQLite database file       |

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

| Endpoint         | Method | Description                   |
|------------------|--------|-------------------------------|
| /signup          | POST   | Create a new user account      |
| /login           | POST   | User login                    |
| /change-password | POST   | Change user password          |
| /profile-edit    | POST   | Edit user profile information |

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.
