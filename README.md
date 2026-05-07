# Contact Book CLI

> Managing multiple contacts with persistent state. For educational purposes only.

## What it does
A command-line contact management application that lets users create and manage multiple contacts. Contact state persists between sessions via a local JSON save file - useful as a foundation for any application requiring stateful object management.


## Features
- Add, update, remove, and find contacts
- Full contact details including address (via composition)
- Tabulated contact listing
- Contact state persists across sessions via JSON

## Setup
1. Clone the repository
2. Install Python 3.12
3. Create a virtual environment: `python3.12 -m venv .venv`
4. Activate it: `source .venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## Run
```
python3.12 contact_book_cli.py
```

## Example Output
```
----- Contact Book CLI -----
    1. Add Contact
    2. Update Contact
    3. Remove Contact
    4. Find Contact by Email
    5. List All Contacts
    6. Quit
Choose a menu item number: 
```
```
Choose a menu item number: 1
Email Address: example@email.com
Contact Name: Test Contact
Address (street): 1234 Sample Dr
Address (city): Tester
Address (country): USA
Phone Number: 5555555555
```
```
Choose a menu item number: 4
Enter the contact email: example@email.com

        ----- Contact Card -----
        Name:       Test Contact
        Email:      example@email.com
        Address:    1234 Sample Dr, Tester, USA
        Phone:      5555555555
        Created:    2026-05-07 09:51
```
```
Choose a menu item number: 5
+--------------+--------------------+------------+------------------+
| Name         | Email              | Phone      | Created At       |
+==============+====================+============+==================+
| Test Contact | example@email.com  | 5555555555 | 2026-05-07 09:51 |
| Tester 2     | tester2@email.com  | 1234567890 | 2026-05-07 09:54 |
| Tester 3     | example@tester.com | 9876543210 | 2026-05-07 09:55 |
+--------------+--------------------+------------+------------------+
```

## What I learned
Built on existing OOP fundamentals with several new concepts: inheritance to consolidate shared attributes across subclasses, composition for modeling "has a" relationships (a Contact has an Address), @property decorators to expose methods as clean attribute-style access, and custom exception classes for descriptive error handling. Also implemented JSON serialization and deserialization for persistent state across sessions.