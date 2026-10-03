<h1 align="center">📔 Personal Journal Manager</h1>

<p align="center">
  <b>A Python File Handling and Object-Oriented Programming Project</b>
</p>

<p align="center">
  A beginner-friendly console application for creating, viewing,
  searching, and deleting journal entries using Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14.6-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Project-Console%20Application-green" alt="Project Type">
  <img src="https://img.shields.io/badge/Concept-File%20Handling-orange" alt="Main Concept">
  <img src="https://img.shields.io/badge/OOP-Python-purple" alt="OOP">
</p>

---

# 📌 Project Information

| Item | Details |
|------|---------|
| 📛 Project Name | Personal Journal Manager |
| 🐍 Language | Python |
| 🔢 Python Version | 3.14.6 |
| 💻 Project Type | Console Application |
| 📂 Main Concept | File Handling |
| 🧠 Additional Concepts | OOP, Exception Handling, Loops, Conditional Statements |
| 📁 Module Used | `os` |
| 🕒 Module Used | `datetime` |
| 📄 Data File | `journal.txt` |
| 🐍 Main Python File | `File_operator.py` |
| 👩‍💻 Author | Krisha Savaliya |

---

# 📖 About the Project

**Personal Journal Manager** is a console-based Python application
created to manage personal journal entries using Python File Handling.

The program allows users to store their journal entries in a text file
named `journal.txt`.

Every journal entry contains:

- The current date
- The current time
- The journal text entered by the user

The application provides a simple menu through which users can:

1. Add a new journal entry
2. View all journal entries
3. Search for a journal entry
4. Delete all journal entries
5. Exit the application

This project is designed to provide practical experience with
**Python File Handling, Object-Oriented Programming, Exception Handling,
File Paths, Date and Time Handling, Loops, Conditional Statements,
and User Input**.

---

# 🎯 Project Objective

The main objective of this project is to understand how Python can be
used to store and manage data using files.

The project demonstrates how to:

- Create a text file
- Open a file
- Read data from a file
- Append data to a file
- Clear file contents
- Search data stored inside a file
- Handle file-related errors
- Work with file paths
- Generate the current date and time
- Organize functionality using a Python class
- Build a menu-driven console application

---

# ✨ Features

## ➕ 1. Add a New Journal Entry

The user can add a new journal entry by selecting option `1`.

The program:

1. Asks the user to enter a journal entry.
2. Gets the current date and time.
3. Creates `journal.txt` if it does not already exist.
4. Opens the file in append mode.
5. Saves the date and journal entry.
6. Displays a success message.

Example:

```text
Enter your journal entry: Today I learned Python File Handling.
Journal entry added successfully!<h1 align="center">📔 Personal Journal Manager</h1>

<p align="center">
  <b>A Python File Handling and Object-Oriented Programming Project</b>
</p>

<p align="center">
  A beginner-friendly console application for creating, storing,
  viewing, searching, and managing personal journal entries using Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14.6-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Project-Console%20Application-green" alt="Project Type">
  <img src="https://img.shields.io/badge/File%20Handling-Yes-orange" alt="File Handling">
  <img src="https://img.shields.io/badge/OOP-Yes-purple" alt="OOP">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Project Status">
</p>

---

## 📌 Project Information

| Item | Details |
|------|---------|
| 📛 Project Name | Personal Journal Manager |
| 🐍 Programming Language | Python |
| 🔢 Python Version | 3.14.6 |
| 💻 Project Type | Console Application |
| 📂 Main Concept | File Handling |
| 🧠 Programming Concept | Object-Oriented Programming |
| 🛡️ Error Handling | Exception Handling |
| 📁 File System Module | `os` |
| 🕒 Date and Time Module | `datetime` |
| 📄 Data Storage | `journal.txt` |
| 🐍 Main Python File | `File_operator.py` |
| 👩‍💻 Author | Krisha Savaliya |
| 📊 Project Status | Completed |

---

# 📖 About the Project

**Personal Journal Manager** is a Python-based console application
developed to practice and demonstrate Python File Handling concepts.

The application allows users to maintain personal journal entries
inside a text file named `journal.txt`.

Instead of storing journal entries only while the program is running,
the application stores them permanently in a text file. This means
the saved entries can be accessed again whenever the program is run.

Each journal entry contains:

- 📅 Date
- 🕒 Time
- 📝 Journal text

The application provides a simple menu-driven interface that allows
the user to perform different operations on the journal file.

---

# 🎯 Project Purpose

The main purpose of this project is to gain practical knowledge of
Python File Handling and Object-Oriented Programming.

Through this project, the following concepts are practiced:

- Creating files
- Reading files
- Writing to files
- Appending data
- Clearing file contents
- Searching file data
- Managing file paths
- Handling file-related exceptions
- Working with date and time
- Creating classes and objects
- Using constructors and instance variables
- Creating menu-driven console applications

---

# ✨ Key Features

## ➕ Add a New Journal Entry

Users can add a new journal entry by selecting option `1`.

The program automatically:

1. Accepts journal text from the user.
2. Gets the current date and time.
3. Creates `journal.txt` if required.
4. Opens the file in append mode.
5. Stores the date and journal text.
6. Displays a success message.

Example:

```text
Enter your journal entry: Today I learned Python File Handling.
Journal entry added successfully!
```

---

## 📖 View All Journal Entries

Users can select option `2` to view all saved entries.

The program:

1. Opens the file in read mode.
2. Reads the complete file.
3. Checks whether data exists.
4. Displays all journal entries.

If the file is empty:

```text
No journal entries found.
```

---

## 🔍 Search for a Journal Entry

Users can search for a journal entry using a keyword or date.

For example:

```text
Enter a keyword or date to search: Python
```

The program reads the journal file and checks whether the entered
keyword exists in:

- The entry date
- The journal text

If a match is found, the entry is displayed.

If no match is found:

```text
No entries were found for the keyword: Python
```

---

## 🗑️ Delete All Journal Entries

Users can delete all stored journal entries using option `4`.

Before deleting the data, the program asks for confirmation:

```text
Are you sure you want to delete all entries? (yes/no):
```

If the user enters:

```text
yes
```

the file contents are cleared.

If the user enters:

```text
no
```

the existing journal entries remain unchanged.

---

## 🚪 Exit the Application

Option `5` is used to exit the program.

The program displays:

```text
Thank you for using File Operator. Goodbye!
```

and stops the main menu loop.

---

# 🧠 Python Concepts Covered

This project covers several important Python programming concepts.

---

## 1. 📦 Object-Oriented Programming

The project uses Object-Oriented Programming to organize
journal-related functionality.

The main class is:

```python
class JournalManager:
```

The class contains all the operations required to manage
journal entries.

### Class Methods

```text
__init__()
create_file()
add_entry()
view_entry()
search_entry()
delete_entry()
```

Using a class makes the program more organized and easier to maintain.

---

## 2. 🏗️ Constructor

The project uses the `__init__()` constructor:

```python
def __init__(self, file_name="journal.txt"):
```

The constructor is automatically called when the object is created.

Example:

```python
journal = JournalManager()
```

The constructor initializes the journal file path.

---

## 3. 🔐 Instance Variable

The project uses:

```python
self.file_name
```

as an instance variable.

It stores the complete path of the journal file.

The variable is available to all methods inside the
`JournalManager` class.

---

# 📂 File Handling

File Handling is the primary concept of this project.

Python's built-in `open()` function is used to work with
the `journal.txt` file.

The project demonstrates four important file modes.

| Mode | Purpose | Used For |
|------|---------|----------|
| `x` | Create a new file | Creating the journal file |
| `a` | Append data | Adding journal entries |
| `r` | Read data | Viewing and searching entries |
| `w` | Write and clear data | Deleting all entries |

---

## 📄 `x` Mode

The program creates the journal file using:

```python
with open(self.file_name, "x"):
    pass
```

The `x` mode creates a new file.

If the file already exists, Python raises:

```text
FileExistsError
```

The program handles this exception so that execution can continue.

---

## ➕ `a` Mode

The program uses append mode to add journal entries:

```python
with open(self.file_name, "a") as journal_file:
```

Append mode places new data at the end of the file.

Existing entries are not removed.

---

## 📖 `r` Mode

The program uses read mode to retrieve saved entries:

```python
with open(self.file_name, "r") as journal_file:
```

For viewing all entries, the program uses:

```python
journal_data = journal_file.read()
```

For searching entries, it uses:

```python
journal_lines = journal_file.readlines()
```

---

## 🗑️ `w` Mode

The program uses write mode when deleting all entries:

```python
with open(self.file_name, "w") as journal_file:
    pass
```

Opening a file in `w` mode clears its existing contents.

The file itself is not removed.

---

# 🤝 Using `with open()`

The project uses the `with open()` statement for file operations.

Example:

```python
with open(self.file_name, "r") as journal_file:
```

The `with` statement provides automatic file management.

After the block finishes, Python automatically closes the file.

This is safer and cleaner than manually opening and closing files.

---

# 🛡️ Exception Handling

Exception Handling is used throughout the project to handle
common file-related problems.

The general structure is:

```python
try:
    # File operation
except:
    # Error handling
```

The project handles three important exceptions.

---

## ⚠️ FileExistsError

This exception occurs when the program tries to create a file
that already exists.

The program handles it in `create_file()`.

```python
except FileExistsError:
    pass
```

---

## ❌ FileNotFoundError

This exception occurs when the program tries to access a file
that does not exist.

For example, while viewing entries:

```python
except FileNotFoundError:
    print("The journal file does not exist.")
```

---

## 🚫 PermissionError

This exception occurs when the program does not have permission
to access the journal file.

Example:

```python
except PermissionError:
    print("Error: You do not have permission to read.")
```

This prevents the application from terminating unexpectedly.

---

# 📁 `os` Module

The project uses Python's built-in `os` module.

```python
import os
```

The `os` module is used for file and directory path management.

---

## `os.path.abspath()`

The program uses:

```python
os.path.abspath(__file__)
```

This gets the absolute path of the current Python file.

---

## `os.path.dirname()`

The program uses:

```python
os.path.dirname(os.path.abspath(__file__))
```

This gets the directory where `File_operator.py` is located.

---

## `os.path.join()`

The program combines the directory path and file name using:

```python
os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    file_name
)
```

This creates the complete path to:

```text
journal.txt
```

### Why is this useful?

It ensures that the journal file is created in the same directory
as the Python program instead of depending on the terminal's
current working directory.

---

# 🕒 `datetime` Module

The project uses the built-in `datetime` module.

```python
from datetime import datetime
```

The current date and time are obtained using:

```python
datetime.now()
```

The value is formatted using:

```python
strftime("%Y-%m-%d %H:%M:%S")
```

Example:

```text
2026-10-03 21:15:30
```

The final journal entry is stored as:

```text
[2026-10-03 21:15:30]
Today I learned Python File Handling.
```

---

# 🔁 Loops

The project uses both `while` and `for` loops.

---

## `while` Loop

The main menu uses:

```python
while True:
```

This keeps displaying the menu until the user chooses option `5`.

The loop is stopped using:

```python
break
```

---

## `for` Loop

The search operation uses:

```python
for current_line in journal_lines:
```

The loop processes the journal data line by line.

It helps the program identify:

- Entry date
- Entry text
- Matching keywords

---

# 🔀 Conditional Statements

The project uses:

```text
if
elif
else
```

Conditional statements are used to:

- Process menu choices
- Check whether journal data exists
- Check search results
- Confirm deletion
- Handle invalid options

Example:

```python
if menu_choice == "1":
    journal.add_entry()

elif menu_choice == "2":
    journal.view_entry()

elif menu_choice == "3":
    journal.search_entry()

elif menu_choice == "4":
    journal.delete_entry()

elif menu_choice == "5":
    break

else:
    print("Invalid option.")
```

---

# ⌨️ User Input

The application uses Python's `input()` function to interact
with the user.

User input is collected for:

### Menu Selection

```python
menu_choice = input("User Input:\n")
```

### Journal Entry

```python
journal_title = input("Enter your journal entry: ")
```

### Search Keyword

```python
search_keyword = input(
    "Enter a keyword or date to search: "
)
```

### Delete Confirmation

```python
delete_confirmation = input(
    "Are you sure you want to delete all entries? (yes/no): "
)
```

---

# 🔍 Search Function Logic

The search method reads all lines from the journal file:

```python
journal_lines = journal_file.readlines()
```

The program then processes each line:

```python
for current_line in journal_lines:
```

The first line represents the entry date.

The second line represents the journal text.

The program checks:

```python
if (
    search_keyword in entry_date
    or search_keyword in entry_title
):
```

If the keyword exists in either location, the entry is displayed.

The variable:

```python
entry_found
```

keeps track of whether a matching entry was found.

---

# 🧹 Delete Function Logic

The delete operation does not remove the `journal.txt` file.

Instead, it opens the file using write mode:

```python
with open(self.file_name, "w") as journal_file:
    pass
```

Opening the file in `w` mode clears its contents.

Therefore:

### Before Delete

```text
journal.txt

[2026-10-03 21:15:30]
Today I learned Python.

[2026-10-03 21:20:45]
I practiced File Handling.
```

### After Delete

```text
journal.txt

(empty)
```

The file still exists, but all journal entries have been removed.

---

# 📊 Important Variables

| Variable | Purpose |
|----------|---------|
| `file_name` | Stores the journal file name |
| `self.file_name` | Stores the complete journal file path |
| `journal_title` | Stores the journal text entered by the user |
| `entry_date` | Stores the current date and time |
| `journal_file` | Represents the opened journal file |
| `journal_data` | Stores the complete file data |
| `search_keyword` | Stores the search keyword |
| `journal_lines` | Stores all lines read from the file |
| `entry_found` | Tracks whether a matching entry was found |
| `entry_title` | Stores the journal text |
| `delete_confirmation` | Stores the user's delete confirmation |
| `menu_choice` | Stores the selected menu option |
| `current_line` | Stores the current line during the search |

---

# 🔄 Program Workflow

```text
                         START
                           │
                           ▼
                Create JournalManager
                       Object
                           │
                           ▼
                  Display Main Menu
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
      Add Entry        View Entries     Search Entry
          │                │                │
          ▼                ▼                ▼
      Save Data         Read File       Search File
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                    Delete Entries
                           │
                           ▼
                        Exit
```

---

# 📋 Application Menu

When the application starts:

```text
Welcome to File Operator...
Please select an option
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
User Input:
```

---

# 📁 Project Structure

```text
Personal-Journal-Manager/
│
├── File_operator.py
├── journal.txt
├── output.png
└── README.md
```

### 📄 File Description

| File | Description |
|------|-------------|
| `File_operator.py` | Main Python source code |
| `journal.txt` | Stores all journal entries |
| `output.png` | Screenshot of the application output |
| `README.md` | Project documentation |

> **Note:** `journal.txt` is created automatically when the first
> journal entry is added.

---

# ⚙️ Requirements

Before running the project, make sure you have:

- Python 3.14.6 or a compatible Python 3 version
- Visual Studio Code or another Python-supported editor
- Terminal or Command Prompt

No external Python packages are required.

The project uses only Python's built-in modules:

```text
os
datetime
```

---


# 📝 How to Use

## 1️⃣ Add a New Entry

Select:

```text
1
```

Enter your journal entry:

```text
Enter your journal entry: Today I learned Python.
```

Output:

```text
Journal entry added successfully!
```

---

## 2️⃣ View All Entries

Select:

```text
2
```

Example:

```text
Your Journal Entries:
-------------------------------
[2026-10-03 21:15:30]
Today I learned Python.
```

---

## 3️⃣ Search for an Entry

Select:

```text
3
```

Enter:

```text
Enter a keyword or date to search: Python
```

Example output:

```text
Matching Entries:
-------------------------------
[2026-10-03 21:15:30]

Today I learned Python.
```

---

## 4️⃣ Delete All Entries

Select:

```text
4
```

Confirm:

```text
Are you sure you want to delete all entries? (yes/no): yes
```

Output:

```text
All journal entries have been deleted.
```

---

## 5️⃣ Exit

Select:

```text
5
```

Output:

```text
Thank you for using File Operator. Goodbye!
```

---

# 📄 Journal File Format

The `journal.txt` file stores entries in this format:

```text
[2026-10-03 21:15:30]
Today I learned Python File Handling.

[2026-10-03 21:20:45]
I practiced Exception Handling.

[2026-10-03 21:25:10]
I worked on my Personal Journal Manager project.
```

Each entry contains:

1. Date and time
2. Journal text

---

# 🧪 Example Complete Session

```text
Welcome to File Operator...
Please select an option
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
User Input:
1

Enter your journal entry: Today I learned Python File Handling.
Journal entry added successfully!

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
Today I learned Python File Handling.

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

Today I learned Python File Handling.

Please select an option
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
User Input:
5

Thank you for using File Operator. Goodbye!
```

---

# ⚠️ Error Handling Examples

## Invalid Menu Option

```text
User Input:
8

Invalid option. Please select a valid option from the menu.
```

---

## File Not Found

```text
Journal file does not exist.
```

---

## Permission Error

```text
Error: You do not have permission to read the journal file.
```

---

## Empty Journal

```text
No journal entries found.
```

---

# 🎯 Learning Objectives

By completing this project, you can practice:

### Python Fundamentals

- Variables
- Strings
- User input
- `if`, `elif`, and `else`
- `for` loops
- `while` loops
- `break`
- Formatted strings

### Object-Oriented Programming

- Classes
- Objects
- Constructors
- `self`
- Instance variables
- Instance methods

### File Handling

- File creation
- File reading
- File writing
- File appending
- File content clearing
- File modes
- `read()`
- `readlines()`
- `write()`
- `with open()`

### Exception Handling

- `try`
- `except`
- `FileExistsError`
- `FileNotFoundError`
- `PermissionError`

### Built-in Modules

- `os`
- `datetime`

### Application Development

- Menu-driven application
- User interaction
- Data persistence
- Search functionality
- Confirmation handling
- Error handling

---

# 📌 Advantages

The project has several advantages:

- ✅ Beginner-friendly
- ✅ Simple console interface
- ✅ Uses permanent text-file storage
- ✅ Demonstrates real File Handling
- ✅ Uses Object-Oriented Programming
- ✅ Includes Exception Handling
- ✅ Automatically records date and time
- ✅ Uses file paths correctly
- ✅ Does not require external libraries
- ✅ Easy to understand and extend

---

# ⚠️ Current Limitations

The current version has some limitations:

- It cannot edit an existing journal entry.
- It can delete all entries but cannot delete a single entry.
- It does not use a database.
- It does not have a graphical user interface.
- It does not provide password protection.
- Search uses simple text matching.
- Journal entries are stored in a plain text file.
- There is no automatic backup system.

---

# 🔮 Future Improvements

The project can be extended with:

- ✏️ Edit an existing entry
- 🗑️ Delete a single entry
- 🔐 Password protection
- 🏷️ Categories and tags
- 📅 Advanced date-based search
- 🔎 Case-insensitive search
- 📊 Entry count
- 💾 Backup and restore
- 📤 Export journal entries
- 🗄️ JSON file storage
- 🗃️ Database integration
- 🎨 Graphical User Interface
- 🌙 Dark mode
- 📱 Mobile-friendly interface

---

# 🧩 Possible Future Architecture

A future version could be organized like this:

```text
Personal-Journal-Manager/
│
├── File_operator.py
├── journal.txt
├── output.png
├── README.md
│
├── data/
│   └── journal_backup.txt
│
└── assets/
    └── screenshots/
```

This structure can help organize data and screenshots
as the project becomes larger.

---

# 📚 Summary

The **Personal Journal Manager** is a practical Python project
that demonstrates how a console application can use File Handling
to store and manage real data.

The project combines:

```text
Python
   │
   ├── Object-Oriented Programming
   │
   ├── File Handling
   │
   ├── Exception Handling
   │
   ├── os Module
   │
   ├── datetime Module
   │
   ├── Loops
   │
   ├── Conditional Statements
   │
   └── User Input
```

It provides a strong foundation for building more advanced
file-based Python applications.

---

# 👩‍💻 Author

**Krisha Savaliya**

Python Learner | OOP & File Handling Project

---

# 🐍 Python Version

**Python 3.14.6**

---

# 📜 License

This project is created for learning and educational purposes.

You are free to use, study, and modify the project for educational purposes.

---

# 🖥️ Output

## 🏠 Welcome Screen

```text
Welcome to File Operator...
Please select an option
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
User Input:
```

---

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

Enter your journal entry: Today I learned Python File Handling.
Journal entry added successfully!
```

---

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
Today I learned Python File Handling.
```

---

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

Today I learned Python File Handling.
```

---

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

---

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

Thank you for using File Operator. Goodbye!
```

---

<p align="center">
  <b>📔 Personal Journal Manager</b>
</p>

<p align="center">
  Built with Python 🐍 | File Handling 📂 | OOP 🧠
</p>