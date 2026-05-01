import datetime
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
        pass

    def __str__(self):
        pass

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
        print(f"{'Name':<20}{'Email':<20}{'Phone':<20}{'Created At':<20}")
        for contact in self._contacts.values():
            created = contact.created_at.strftime("%Y-%m-%d %H:%M")
            print(f"{contact.name:<20}{contact.email:<20}{contact.phone:<20}{created:<20}")
    
    def remove(self, email):
        if email not in self._contacts:
            raise ContactNotFoundError(email)
        del self._contacts[email]

class ContactBookError(Exception):
    pass
class DuplicateContactError(ContactBookError):
    def __init__(self, email):
        super().__init__(f"Contact with the email '{email}' already exists")
class ContactNotFoundError(ContactBookError):
    def __init__(self, query):
        super().__init__(f"No contact found matching '{query}'")

class Record:
    def __init__(self):
        self.created_at = datetime.datetime.now()

    def summary(self):
        raise NotImplementedError("Subclasses must implement summary()")

class Contact(Record):
    def __init__(self, name, email, address, phone):
        super().__init__()
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
        return f"""
        ----- Contact Card -----
        Name:       {self.name}
        Email:      {self.email}
        Address:    {self.address!s}
        Phone:      {self.phone}
        Created:    {self.created_at}
        """        
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email: {value}")
        self._email = value.lower()