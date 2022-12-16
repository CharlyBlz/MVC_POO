class Contacto(object):
    # Dunder method--> __init__
    def __init__(self, last_name, first_name, email, phone):
        self._last_name = last_name
        self._first_name = first_name
        self._email = email
        self._phone = phone
    # Getter de last name
    @property 
    def last_name(self):
        return self._last_name
    # Setter de last name
    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    # Getter de first name
    @property 
    def first_name(self):
        return self._first_name
    # Setter de first name
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    # Getter de email
    @property 
    def email(self):
        return self._email
    # Setter de email
    @email.setter
    def email(self, value):
        self._email = value
    
    # Getter de phone
    @property 
    def phone(self):
        return self._phone
    # Setter de phone
    @phone.setter
    def phone(self, value):
        self._phone = value