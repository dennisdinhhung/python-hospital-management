from domains.Employee import Employee

class Doctor(Employee):
    def __init__(self, id, name, gender, dob):
        super().__init__(id, name, gender, dob)
        self.isMedical = True

    def IsMedical(self):
        return self.isMedical