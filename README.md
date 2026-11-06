# Student Management System

## Project Overview
The Student Management System is a Full-Stack Web Application developed using Python Flask, HTML, CSS, and SQLite.

This application helps users manage student information easily through a simple and user-friendly interface.

## Technologies Used
- Python
- Flask
- HTML5
- CSS3
- SQLite
- Visual Studio Code

## Features
- Add new student records
- View all student details
- Update student information
- Delete student records
- Search students by name, email, or course
- Store student information in an SQLite database

## Project Structure

```text
Student_Management_System/
│
├── app.py
├── requirements.txt
├── .gitignore
├── students.db
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

Note: `students.db` is generated automatically when the application runs and is excluded from GitHub.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Student_Management_System.git
```

### 2. Open the project folder

```bash
cd Student_Management_System
```

### 3. Install dependencies

```bash
py -m pip install -r requirements.txt
```

### 4. Run the application

```bash
py app.py
```

### 5. Open in browser

```text
http://127.0.0.1:5000
```

## Database
SQLite is used to store student information permanently. The database table contains:

- Student ID
- Student Name
- Email Address
- Course

## Project Objective
The main objective of this project is to develop a simple full-stack web application and understand Python backend development, frontend integration, database connectivity, and CRUD operations.

## Author
Developed as part of Task 3 – Full-Stack App with Python.

## License
This project is created for educational purposes.