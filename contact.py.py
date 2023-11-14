import json

contacts = {}

def add_contact():
    name = input("Enter the contact name here: ")
    number = input("Enter the contact number here: ")

    contacts[name] = number

    print(f"Contact {name} added successfully!")

def search_contact():
    name = input("Enter the name to search: ")

    if name in contacts:
        print(f"Contact found: {name} - {contacts[name]}")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("Add. Add Contact")
        print("Search. Search Contact")
        print("Exit. Exit")

        choice = input("Enter your choice (Add/Search/Exit): ")

        if choice == 'Add':
            add_contact()
        elif choice == 'Search':
            search_contact()
        elif choice == 'Exit':
            print("Exiting ")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
















