class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


    # overriding the str function
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email:{self.email}"