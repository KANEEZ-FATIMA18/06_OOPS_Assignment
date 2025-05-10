class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  


emp = Employee("John")
dept = Department("HR", emp)
print(dept.employee.name)
