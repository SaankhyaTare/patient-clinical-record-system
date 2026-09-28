# Patient Clinical Record Management System

Introduction

Patient Clinical Record Management System This project is implemented in Python programming language. The main aim of this project is to create a system where we can store and manage patient information and reports for the respective patient.

This system will allow the user to add new patients, search for patients, and store medical records, see the medical history, produce reports, and incorporate a simple clinical reference feature.

The project uses Python and SQLite.

Features

- Adding new patients

- Viewing all patients

- Searching patients

- Adding medical records

- Viewing medical history

- Clinical reference using symptoms

- Generating patient reports

- Dashboard displaying basic statistics

- Input validation

- SQLite database

- Automated testing

Modules

# 1. Patient Management

This module is used to insert, view and search patient information.

# 2. Medical Records

This module records the symptoms, notes and observations and dates of visits of the patients.

# 3. Clinical Reference

This module aligns the entered symptoms against the reference data and displays the potential matches.

# 4. Report Generation

It generates a text report with the report patient data and the medical history.

# 5. Validation

This module verifies basic input like age, gender, phone number, names etc.

# 6. Database

This module builds and owns the tables in the SQLite database.

Technologies Used

- Python

- SQLite

- unittest

- VS Code

- Git and GitHub

Project Structure

Vithyarthi project/
│
├── main.py
├── database.py
├── reference.py
├── validation.py
├── reports.py
├── README.md
├── statement.md
├── .gitignore
├── patients.db
│
└── tests/
    ├── __init__.py
    └── test_reference.py