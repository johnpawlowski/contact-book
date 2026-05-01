def main():
    contacts = {}
    
    while True:
        
        print("""----- Contact Book CLI -----
              1. Add Contact
              2. Remove Contact
              3. Find Contact by Email
              4. List All Contacts
              5. Quit
              """)
        
        choice = int(input("Choose a menu item number: "))

        # add contact
        if choice == 1:
            # capture name, email, address, and phone number from user input
            email = input("Email Address: ")
            if email in contacts:
                print("Contact already exists")
                continue
            name = input("Contact Name: ")
            ### split out into first and last name
            street = input("Address (street): ")
            city = input("Address (city): ")
            country = input("Address (country): ")
            address = Address(street, city, country)
            phone = input("Phone Number: ")
            ### remove non-numerical values from string to get an integer value
            # create new contact record from Contact(Record) class
            new_contact = Contact(name, email, address, phone)
            contacts[email] = new_contact

        # remove contact
        elif choice == 2:
            if not contacts:
                print("No contacts exist.")
            try:
                email = input("Email Address")


        # view contact
        elif choice == 3:
            pass

        # list contacts
        elif choice == 4:
            pass

        # quit program
        elif choice == 5:
            print("Goodbye")
            break

        else:
            print("Invalid selection. Please choose 1-5.")


if __name__ == "__main__":
    main()