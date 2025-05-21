class Bun:
    def __init__(self, name, bun_type, price):
        self.name = name
        self.bun_type = bun_type
        self.price = price

    def get_price(self):
        return self.price

    def get_type(self):
        return self.bun_type

    def get_name(self):
        return self.name
