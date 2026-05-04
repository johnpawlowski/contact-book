import datetime
import json
from tabulate import tabulate # type: ignore
class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(street={self.street}, city={self.city}, country={self.country})"
    
    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

class ContactBook:
    def __init__(self):
        self._contacts = {}

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self._contacts!r})"

    def __str__(self):
        return f"ContactBook with {len(self._contacts)} contact(s)."

    @property
    def contacts(self):
        return self._contacts

    def add(self, contact):
        if contact.email in self._contacts:
            raise DuplicateContactError(contact.email)
        self._contacts[contact.email] = contact

    def find(self, email):
        if email not in self._contacts:
            raise ContactNotFoundError(email)
        return self._contacts[email]
    
    def list(self):
        headers = ["Name", "Email", "Phone", "Created At"]
        rows = [[contact.name, contact.email, contact.phone, contact.created_at.strftime("%Y-%m-%d %H:%M")] for contact in self._contacts.values()]
        print(tabulate(rows, headers, colalign=("left", "left", "left", "left"), tablefmt = "outline"))
        # print(f"{'Name':<25}|{'Email':<40}|{'Phone':<20}|{'Created At':<15}")
        # print("-------------------------|----------------------------------------|--------------------|---------------")
        # for contact in self._contacts.values():
        #     created = contact.created_at.strftime("%Y-%m-%d %H:%M")
        #     print(f"{contact.name:<25}|{contact.email:<40}|{contact.phone:<20}|{created:<15}")
    
    def remove(self, email):
        if email not in self._contacts:
            raise ContactNotFoundError(email)
        del self._contacts[email]

    def save(self):
        save_state = {
            email: {"name":contact.name, 
                    "email": contact.email, 
                    "address": {"street": contact.address.street, 
                                "city": contact.address.city, 
                                "country": contact.address.country}, 
                    "phone": contact.phone, 
                    "created_at": contact.created_at.isoformat()}
            for email, contact in self._contacts.items()
            }
        with open("save_state.json", "w") as f:
            json.dump(save_state, f, indent=2)

    def load(self):
        try:
            with open("save_state.json", "r") as f:
                load_state = json.load(f)
        except FileNotFoundError:
            return {}
        if not load_state:
            return {}
        else:
            self._contacts = {email: Contact(data['name'], 
                                   data['email'], 
                                   Address(data['address']['street'], 
                                           data['address']['city'], 
                                           data['address']['country']), 
                                   data['phone'],
                                   datetime.datetime.fromisoformat(data['created_at'])) 
                    for email, data in load_state.items()}

class ContactBookError(Exception):
    pass
class DuplicateContactError(ContactBookError):
    def __init__(self, email):
        super().__init__(f"Contact with the email '{email}' already exists")
class ContactNotFoundError(ContactBookError):
    def __init__(self, query):
        super().__init__(f"No contact found matching '{query}'")

class Record:
    def __init__(self, created_at=None):
        self.created_at = created_at if created_at is not None else datetime.datetime.now()

    def summary(self):
        raise NotImplementedError("Subclasses must implement summary()")

class Contact(Record):
    def __init__(self, name, email, address, phone, created_at=None):
        super().__init__(created_at)
        self.name = name
        self._email = None
        self.email = email
        self.address = address
        self.phone = phone

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(name={self.name}, email={self.email}, address={self.address!r}, phone={self.phone}, created_at={self.created_at})"
    
    def __str__(self):
        return f"""
        {self.name}
        {self.email}
        {self.address!s}
        {self.phone}
        {self.created_at}"""

    def summary(self):
        created = self.created_at.strftime("%Y-%m-%d %H:%M")
        return f"""
        ----- Contact Card -----
        Name:       {self.name}
        Email:      {self.email}
        Address:    {self.address!s}
        Phone:      {self.phone}
        Created:    {created}
        """        
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError(f"Invalid email: {value}")
        self._email = value.lower()