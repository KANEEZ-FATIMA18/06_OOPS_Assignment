class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

Student1 = Student('Kaneez Fatima', 92)
Student2 = Student('Ali', 85)  


Student1.display()
Student2.display()