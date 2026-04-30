def main():
    
    while True:
        
        print("""----- Contact Book CLI -----
              1. Add Contact
              2. Remove Contact
              3. Find Contact by Email
              4. List All Contacts
              5. Quit
              """)
        
        choice = int(input("Choose a menu item number: "))

        if choice in (1, 2):
            pass

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