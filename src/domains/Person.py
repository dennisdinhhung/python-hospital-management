class Person():
    def __init__(self, id, name, gender, dob):
        self.id = id
        self.name = name
        self.gender = gender
        self.dob = dob
        self.phone = ""
        self.email = ""

    # get info
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_dob(self):
        return self.dob

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    # set info
    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_dob(self, dob):
        self.dob = dob

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email
