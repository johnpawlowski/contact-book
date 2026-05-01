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

class Record:
    def __init__(self, created_at):
        self.created_at = created_at

    def summary(self):
        raise NotImplementedError("Subclasses must implement summary()")

class Contact(Record):
    def __init__(self, name, email, address, phone, created_at):
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