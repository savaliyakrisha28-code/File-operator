````markdown
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
````

### File Description

| File                 | Description                      |
| -------------------- | -------------------------------- |
| `journal_manager.py` | Main Python program              |
| `journal.txt`        | Stores journal entries           |
| `output.png`         | Screenshot of the program output |
| `README.md`          | Project documentation            |

> **Note:** The `journal.txt` file is created automatically by the program
> if it does not already exist.

---

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.14.6 or a compatible Python 3 version
* A code editor such as Visual Studio Code
* A terminal or command prompt

No external Python libraries are required.

The project uses the built-in Python `datetime` module.

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Open the Project Folder

```bash
cd Personal-Journal-Manager
```

### Step 3: Run the Python Program

```bash
python journal_manager.py
```

---

## 📝 How to Use

After running the program, a menu will be displayed.

```text
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

### 1️⃣ Add a New Entry

Select option `1` and enter your journal entry.

The program automatically stores:

* Date
* Time
* Journal entry

The entry is saved in `journal.txt`.

### 2️⃣ View All Entries

Select option `2` to display all saved journal entries.

### 3️⃣ Search for an Entry

Select option `3` and enter a keyword or date.

The program searches the stored entries and displays matching entries.

### 4️⃣ Delete All Entries

Select option `4`.

The program asks for confirmation before deleting all journal entries.

Enter:

```text
yes
```

to delete all entries.

Enter:

```text
no
```

to keep the entries.

### 5️⃣ Exit

Select option `5` to close the application.

---

## 📄 Journal File Format

Journal entries are stored in the following format:

```text
[2026-10-03 21:15:30]
Today I learned Python file handling.

[2026-10-03 21:20:45]
I worked on my Personal Journal Manager project.
```

Each journal entry contains:

1. Date and time
2. Journal text

---

## 🛡️ Exception Handling

The application includes exception handling to prevent common file-related
errors from stopping the program unexpectedly.

### FileExistsError

Handled when the journal file already exists.

### FileNotFoundError

Handled when the journal file cannot be found while reading or searching.

### PermissionError

Handled when the program does not have permission to create, read,
write, or modify the journal file.

---

## 🎯 Learning Objectives

By completing this project, you can practice:

* Python classes and objects
* Constructors
* File handling
* File modes
* Reading and writing text files
* Exception handling
* The `datetime` module
* User input
* Conditional statements
* `while` loops
* Basic console application development

---

## 🔮 Future Improvements

The project can be extended with additional features such as:

* ✏️ Edit an existing journal entry
* 🔐 Password protection
* 📅 Search entries by a specific date
* 🏷️ Add categories or tags
* 📊 Display the total number of entries
* 🗂️ Store entries in separate files
* 🎨 Create a graphical user interface
* 💾 Add backup and restore functionality


# 🖥️ Output

## Welcome Screen

```text
Welcome to Personal Journal Manager...
Please select an option
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
User Input:
```

## ➕ Add a New Entry

```text
Please select an option
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
User Input:
1

Enter your journal entry: Today I learned Python file handling.
Journal entry added successfully!
```

## 📖 View All Entries

```text
Please select an option
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
User Input:
2

Your Journal Entries:
-------------------------------
[2026-10-03 21:15:30]
Today I learned Python file handling.
```

## 🔍 Search for an Entry

```text
Please select an option
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
User Input:
3

Enter a keyword or date to search: Python

Matching Entries:
-------------------------------
[2026-10-03 21:15:30]

Today I learned Python file handling.
```

## 🗑️ Delete All Entries

```text
Please select an option
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
User Input:
4

Are you sure you want to delete all entries? (yes/no): yes
All journal entries have been deleted.
```

## 🚪 Exit

```text
Please select an option
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
User Input:
5

Thank you for using Journal Manager. Goodbye!
```

---

<p align="center">
  <b>Made with using Python</b>
</p>

<p align="center">
  <b>© Krisha Savaliya</b>
</p>
```
