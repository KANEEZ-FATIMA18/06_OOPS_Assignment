class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name # Public attribute
        self.salary = salary # protected attribute
        self.__ssn = ssn  # Private attribute

    def get_ssn(self):
        return self.__ssn

    def set_salary(self, new_salary):
        if new_salary > 0:
          self.salary = new_salary  

        else:
            print("Invalid salary. Salary must be positive.")


    def display(self):
        print(f"Name: {self.name}") # Public attribute
        print(f"Salary: {self.salary}") # Protected attribute
        print(f"SSN: {self.__ssn}") # Private attribute

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department # Public attribute

    def show_manager_info(self):
        print(f"Manager Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self.salary}")
        print(f"Accessing SSN via getter command: {self.get_ssn()}")


m = Manager("Ali", 50000, "123-45-6789", "HR")
m.show_manager_info()

m.set_salary(60000)
print(f"Updated Salary: {m.salary}")

# print(m.__ssn)
print("Private SSN via managed:", m.get_ssn())