class Room():
    def __init__(self, id, type, price):
        self.id = id
        self.type = type
        self.price = price
        # self.stock = 0
        self.description = ""

    # Get Methods
    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_price(self):
         return self.price

    def get_description(self):
        return self.description

    # Set Methods:
    def set_id(self, id):
        self.id = id

    def set_type(self, type):
        self.type = type

    def set_price(self, price):
         self.price = price

    # def set_stock(self, stock):
    #     self.stock = stock

    def set_description(self, description):
        self.description = description