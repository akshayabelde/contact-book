# Define the contact list as a dictionary
contact_list = {}

# Function to add a new contact
def add_contact(name, phone_number):
    if name in contact_list:
        print("Contact already exists. Use 'update contact' to change the phone number.")
    else:
        contact_list[name] = phone_number
        print("Contact added successfully.")

# Function to view the contact list
def view_contacts():
    if not contact_list:
        print("The contact list is empty.")
    else:
        print("Contact List:")
        for name, phone_number in contact_list.items():
            print(f"{name}: {phone_number}")

# Function to search for a contact
def search_contact(name):
    if name in contact_list:
        print(f"{name}: {contact_list[name]}")
    else:
        print("Contact not found.")

# Function to update an existing contact
def update_contact(name, new_phone_number):
    if name in contact_list:
        contact_list[name] = new_phone_number
        print("Contact updated successfully.")
    else:
        print("Contact not found. Use 'add contact' to add a new contact.")

# Function to delete a contact
def delete_contact(name):
    if name in contact_list:
        del contact_list[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

# Main function to run the contact list management program
def main():
    while True:
        print("\n--- Contact List Management ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            add_contact(name, phone_number)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            name = input("Enter the name to search: ")
            search_contact(name)
        elif choice == "4":
            name = input("Enter the name to update: ")
            new_phone_number = input("Enter the new phone number: ")
            update_contact(name, new_phone_number)
        elif choice == "5":
            name = input("Enter the name to delete: ")
            delete_contact(name)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
