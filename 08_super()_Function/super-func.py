class Person:
    def __init__(self , name):
        self.name = name
        print(f"Person's name is: {self.name}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher' Subject: {self.subject}")

t = Teacher("Kaneez Fatima", "Information Technology")