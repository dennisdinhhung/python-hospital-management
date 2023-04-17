from domains.Person import Person

class Employee(Person):
    def __init__(self, id, name, gender, dob):
        super().__init__(id, name, gender, dob)
        self.salary = 0
        self.department = ""

    def get_salary(self):
        return self.salary

    def get_dept(self):
        return self.department

    def set_salary(self, salary):
        self.salary = salary

    def set_dept(self, dept):
        self.department = dept