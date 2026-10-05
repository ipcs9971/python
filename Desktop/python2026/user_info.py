class UserInfo:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_info(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}"