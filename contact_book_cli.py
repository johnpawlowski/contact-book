import contact_book as cb

Address = cb.Address
Contact = cb.Contact
ContactBook = cb.ContactBook

def main():
    contacts = ContactBook()
    
    while True:
        
        print("""----- Contact Book CLI -----
    1. Add Contact
    2. Remove Contact
    3. Find Contact by Email
    4. List All Contacts
    5. Quit""")
        
        choice = int(input("Choose a menu item number: ").strip())

        # add contact
        if choice == 1:
            email = input("Email Address: ").strip()
            try:
                if email in contacts.contacts:
                    raise cb.DuplicateContactError(email)
            except cb.DuplicateContactError as e:
                print(f"{e}")
                continue
            name = input("Contact Name: ").strip()
            ### split out into first and last name
            street = input("Address (street): ").strip()
            city = input("Address (city): ").strip()
            country = input("Address (country): ").strip()
            address = Address(street, city, country)
            phone = input("Phone Number: ").strip()
            ### remove non-numerical values from string to get an integer value
            new_contact = Contact(name, email, address, phone)
            contacts.add(new_contact)

        # remove contact
        elif choice == 2:
            if not contacts.contacts:
                print("No contacts exist.")
                continue
            to_remove = input("Enter the email of the contact to remove: ").strip().lower()
            contacts.remove(to_remove)

        # view contact
        elif choice == 3:
            if not contacts.contacts:
                print("No contacts exist.")
                continue
            contact_email = input("Enter the contact email: ").strip()
            to_view = contacts.contacts[contact_email]
            print(to_view.summary())

        # list contacts
        elif choice == 4:
            if not contacts.contacts:
                print("No contacts exist.")
                continue
            contacts.list()

        # quit program
        elif choice == 5:
            print("Goodbye")
            break

        else:
            print("Invalid selection. Please choose 1-5.")


if __name__ == "__main__":
    main()