import contact_book as cb

Address = cb.Address
Contact = cb.Contact
ContactBook = cb.ContactBook

def main():
    contacts = ContactBook()
    contacts.load()
    
    while True:
        
        print("""----- Contact Book CLI -----
    1. Add Contact
    2. Update Contact
    3. Remove Contact
    4. Find Contact by Email
    5. List All Contacts
    6. Quit""")
        
        choice = input("Choose a menu item number: ").strip()

        # add contact
        if choice == "1":
            email = input("Email Address: ").strip()
            if email in contacts.contacts:
                print(f"{cb.DuplicateContactError(email)}")
                continue
            name = input("Contact Name: ").strip()
            street = input("Address (street): ").strip()
            city = input("Address (city): ").strip()
            country = input("Address (country): ").strip()
            address = Address(street, city, country)
            phone = input("Phone Number: ").strip()
            new_contact = Contact(name, email, address, phone)
            contacts.add(new_contact)
            contacts.save()
        
        if choice == "2":
            email = input("Enter the email of the contact to update: ").strip().lower()
            if email not in contacts.contacts:
                print(f"{cb.ContactNotFoundError(email)}")
                continue
            key = input("Enter the field to update: ").strip().lower()
            if key == "address":
                street = input("New Address (street): ").strip()
                city = input("New Address (city): ").strip()
                country = input("New Address (country): ").strip()
                new_value = Address(street, city, country)
            else:
                new_value = input(f"New {key}: ").strip()
            try:
                contacts.update(email, key, new_value)
                contacts.save()
                print(f"Contact updated.")
            except ValueError as e:
                print(f"Error: {e}")

        # remove contact
        elif choice == "3":
            if not contacts.contacts:
                print("No contacts exist.")
                continue
            try:
                to_remove = input("Enter the email of the contact to remove: ").strip().lower()
                contacts.remove(to_remove)
                contacts.save()
            except cb.ContactNotFoundError as e:
                print(f"{e}")

        # view contact
        elif choice == "4":
            if not contacts.contacts:
                print("No contacts exist.")
                continue
            contact_email = input("Enter the contact email: ").strip()
            try:
                to_view = contacts.find(contact_email)
                print(to_view.summary())
            except cb.ContactNotFoundError as e:
                print(f"{e}")

        # list contacts
        elif choice == "5":
            if not contacts.contacts:
                print("No contacts exist.")
                continue
            contacts.list()

        # quit program
        elif choice == "6":
            print("Goodbye")
            break

        else:
            print("Invalid selection. Please choose 1-6.")


if __name__ == "__main__":
    main()