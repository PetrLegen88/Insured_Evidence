class Insured:
    """
    The Insured class represents an insured person.

    Parameters:
    - name: a string with the first name
    - surname: a string with the last name
    - phone_number: a string with the phone number
    - age: a string with the age
    """

    def __init__(self, name: str, surname: str, phone_number: str, age: str):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.age = age
