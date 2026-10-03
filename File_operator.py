import os
from datetime import datetime


class JournalManager:

    # Initialize the journal file path
    def __init__(self, file_name="journal.txt"):
        self.file_name = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            file_name
        )

    # Create the journal file if it does not already exist
    def create_file(self):
        try:
            with open(self.file_name, "x"):
                pass

        except FileExistsError:
            pass

        except PermissionError:
            print("You do not have permission to create the journal file.")

    # Add a new journal entry
    def add_entry(self):
        try:
            journal_title = input("Enter your journal entry: ")

            entry_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.create_file()

            with open(self.file_name, "a") as journal_file:
                journal_file.write(f"[{entry_date}]\n")
                journal_file.write(f"{journal_title}\n")

            print("Journal entry added successfully!")

        except PermissionError:
            print("Error: You do not have permission to write.")

    # View all journal entries
    def view_entry(self):
        try:
            with open(self.file_name, "r") as journal_file:
                journal_data = journal_file.read()

                if journal_data:
                    print("Your Journal Entries:")
                    print("-------------------------------")
                    print(journal_data)
                else:
                    print("No journal entries found.")

        except FileNotFoundError:
            print(
                "The journal file does not exist. "
                "Please add a new entry first."
            )

        except PermissionError:
            print("Error: You do not have permission to read.")

    # Search for a journal entry using a keyword or date
    def search_entry(self):
        try:
            search_keyword = input(
                "Enter a keyword or date to search: "
            )

            with open(self.file_name, "r") as journal_file:
                journal_lines = journal_file.readlines()

            entry_found = False
            entry_date = ""
            entry_title = ""

            for current_line in journal_lines:
                if entry_date == "":
                    entry_date = current_line
                else:
                    entry_title = current_line

                    if (
                        search_keyword in entry_date
                        or search_keyword in entry_title
                    ):
                        print("\nMatching Entries:")
                        print("-------------------------------")
                        print(entry_date)
                        print(entry_title)
                        entry_found = True

                    entry_date = ""
                    entry_title = ""

            if not entry_found:
                print(
                    "No entries were found for the keyword:",
                    search_keyword
                )

        except FileNotFoundError:
            print("Journal file does not exist.")

        except PermissionError:
            print(
                "Error: You do not have permission "
                "to read the journal file."
            )

    # Delete all journal entries
    def delete_entry(self):
        try:
            delete_confirmation = input(
                "Are you sure you want to delete all entries? (yes/no): "
            )

            if delete_confirmation == "yes":
                with open(self.file_name, "w") as journal_file:
                    pass

                print("All journal entries have been deleted.")

            elif delete_confirmation == "no":
                print("No journal entries to delete.")

        except FileNotFoundError:
            print("Journal file does not exist.")

        except PermissionError:
            print("You do not have permission to delete entries.")


# Create the JournalManager object
journal = JournalManager()


# Main menu for the File Operator
print("Welcome to File Operator...")

while True:
    print("Please select an option")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    # Get the user's menu choice
    menu_choice = input("User Input:\n")

    if menu_choice == "1":
        journal.add_entry()

    elif menu_choice == "2":
        journal.view_entry()

    elif menu_choice == "3":
        journal.search_entry()

    elif menu_choice == "4":
        journal.delete_entry()

    elif menu_choice == "5":
        print("Thank you for using File Operator. Goodbye!")
        break

    else:
        print(
            "Invalid option. "
            "Please select a valid option from the menu."
        )