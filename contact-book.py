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

        if choice == 1:
            # capture name, email, address, and phone number from user input
            ## name = input("Contact Name")
            ### split out into first and last name
            ## email = input("Email Address")
            ## address = Address(street, city, country)
            ## phone = input("Phone Number")
            ### remove non-numerical values from string to get an integer value
            # check if email address already exists in keys, if not...
            # create new contact record from Contact(Record) class
            ## new_contact = Contact(name, email, Address(), phone)


        elif choice == 2:
            if not contacts:

            try:
                #find if contact already exists by email
                contact =

        elif choice == 3:
            pass

        elif choice == 4:
            pass

        elif choice == 5:
            print("Goodbye")
            break

        else:
            print("Invalid selection. Please choose 1-5.")


if __name__ == "__main__":
    main()