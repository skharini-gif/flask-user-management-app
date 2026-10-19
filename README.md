# Flask User Management App

A simple, beginner-friendly User Management Application built using Python Flask, HTML templates, and SQLite.

## About the Project

This project demonstrates basic CRUD operations using Flask and an SQLite database. It allows users to manage user records through a simple web interface.

## Features

* **Add User:** Add new user records to the database.
* **View Users:** Display stored user records.
* **Delete User:** Remove user records from the database.
* **SQLite Database:** Store user information persistently.
* **HTML Templates:** Display a simple and user-friendly interface.

## Technologies Used

* Python
* Flask
* HTML
* SQLite
* Jinja2 Templates

## Project Structure

```text
flask-user-management-app/
├── app.py
├── templates/
├── static/
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/flask-user-management-app.git
cd flask-user-management-app
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Your Browser

Visit:

```text
http://127.0.0.1:5000/
```

## Learning Objectives

This project helps beginners understand:

* Flask application basics and routing.
* Rendering HTML templates.
* Connecting Flask with an SQLite database.
* Performing database operations.
* Building a simple web application using Python.

## Future Improvements

* Add user update functionality.
* Add form validation.
* Improve the user interface with CSS.
* Implement authentication and authorization.

## License

This project is available for educational and learning purposes.
