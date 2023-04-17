class Room():
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        # self.stock = 0
        self.description = ""

    # Get Methods
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
         return self.price

    # def get_stock(self):
    #     return self.stock

    def get_description(self):
        return self.description

    # Set Methods:
    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
         self.price = price

    # def set_stock(self, stock):
    #     self.stock = stock

    def set_description(self, description):
        self.description = description