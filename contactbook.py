# Contact Book Application (File-Based)

import json

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Search contact by name
def search_contact(contacts):
    name = input("Enter name to search: ").lower()
    found = False

    for contact in contacts:
        if name in contact["name"].lower():
            print(f"Found -> Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True

    if not found:
        print("Contact not found.")

# Update contact
def update_contact(contacts):
    name = input("Enter name to update: ").lower()

    for contact in contacts:
        if name == contact["name"].lower():
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")
            save_contacts(contacts)
            print("Contact updated!")
            return

    print("Contact not found.")

# Delete contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if name == contact["name"].lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted!")
            return

    print("Contact not found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Run the program
main()