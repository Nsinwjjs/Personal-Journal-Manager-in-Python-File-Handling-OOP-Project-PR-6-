# ======================================
# PR-6 File Operator
# Personal Journal Manager using OOP
# ======================================

from datetime import datetime
import os


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # -------------------------------
    # Add a new journal entry
    # -------------------------------
    def add_entry(self):
        try:
            entry = input("Enter your journal entry:\n")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a") as file:
                file.write(f"[{timestamp}]\n{entry}\n\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Permission denied while writing to the file.")
        except Exception as e:
            print("Error:", e)

    # -------------------------------
    # View all journal entries
    # -------------------------------
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                if content.strip() == "":
                    print("Journal is empty.")
                else:
                    print("\n--- All Journal Entries ---")
                    print(content)

        except FileNotFoundError:
            print("Journal file does not exist.")
        except Exception as e:
            print("Error:", e)

    # -------------------------------
    # Search for an entry
    # -------------------------------
    def search_entry(self):
        try:
            keyword = input("Enter keyword or date to search: ")

            with open(self.filename, "r") as file:
                entries = file.read()

                if keyword.lower() in entries.lower():
                    print("\n--- Matching Entries ---")
                    for block in entries.split("\n\n"):
                        if keyword.lower() in block.lower():
                            print(block)
                            print("-" * 30)
                else:
                    print("No matching entry found.")

        except FileNotFoundError:
            print("Journal file not found.")
        except Exception as e:
            print("Error:", e)

    # -------------------------------
    # Delete all journal entries
    # -------------------------------
    def delete_entries(self):
        try:
            confirm = input("Are you sure you want to delete all entries? (yes/no): ")

            if confirm.lower() == "yes":
                if os.path.exists(self.filename):
                    os.remove(self.filename)
                    print("All journal entries deleted successfully.")
                else:
                    print("Journal file does not exist.")
            else:
                print("Delete operation cancelled.")

        except PermissionError:
            print("Permission denied while deleting the file.")
        except Exception as e:
            print("Error:", e)


# ======================================
# Menu Driven Interface
# ======================================
def main_menu():
    journal = JournalManager()

    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            journal.add_entry()

        elif choice == "2":
            journal.view_entries()

        elif choice == "3":
            journal.search_entry()

        elif choice == "4":
            journal.delete_entries()

        elif choice == "5":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")



