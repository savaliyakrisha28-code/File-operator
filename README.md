# 📔 Personal Journal Manager

<p align="center">
  <b>A Python File Handling Project</b>
</p>

<p align="center">
  A simple console-based Personal Journal Manager built using Python.
  It allows users to add, view, search, and delete journal entries
  using file handling concepts.
</p>

---

## 📌 Project Information

| Item | Details |
|------|---------|
| Project Name | Personal Journal Manager |
| Language | Python |
| Python Version | 3.14.6 |
| Project Type | Console Application |
| Main Concept | File Handling |
| File Used | `journal.txt` |
| Author | Krisha Savaliya |

---

## 📖 About the Project

The **Personal Journal Manager** is a beginner-friendly Python console application
designed to manage personal journal entries.

The application stores journal entries in a text file named `journal.txt`.
Each entry contains a date and time along with the journal text.

The project demonstrates how Python can be used to create, read, write,
search, and manage data stored in a text file.

---

## ✨ Features

- ➕ Add a new journal entry
- 📖 View all journal entries
- 🔍 Search entries using a keyword or date
- 🗑️ Delete all journal entries
- 📅 Automatically records the current date and time
- 📁 Automatically creates the journal file when required
- ⚠️ Handles common file-related exceptions
- 🖥️ Simple and user-friendly console menu

---

## 🧠 Python Concepts Used

This project demonstrates the following Python concepts:

### 1. Classes and Objects

The `JournalManager` class is used to organize all journal-related operations.

### 2. Constructor

The `__init__()` method initializes the journal file name.

### 3. File Handling

Python file handling is used to store and retrieve journal entries.

The following file modes are used:

- `x` → Create a new file
- `a` → Add new content to the file
- `r` → Read data from the file
- `w` → Clear existing file content

### 4. `with open()`

The `with open()` statement is used to safely open and close files.

### 5. Exception Handling

The project handles common file-related exceptions such as:

- `FileExistsError`
- `FileNotFoundError`
- `PermissionError`

### 6. Date and Time

The `datetime` module is used to automatically store the date and time
when a journal entry is created.

### 7. Conditional Statements

`if`, `elif`, and `else` statements are used to process menu choices
and user input.

### 8. Loops

A `while` loop keeps the main menu running until the user selects the Exit option.

---

## 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── journal_manager.py
├── journal.txt
├── output.png
└── README.md