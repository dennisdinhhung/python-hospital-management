from domains.Person import Person

class Patient(Person):
    def __init__(self, id, name, gender, dob):
        super().__init__(id, name, gender, dob)
        self.illness = ""
        self.debt = 0

    def get_illness(self):
        return self.illness

    def get_debt(self):
        return self.debt
    
    def set_illness(self, illness: str):
        self.illness = illness

    def set_debt(self, debt):
        self.debt = debt