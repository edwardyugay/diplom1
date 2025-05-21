class Burger:
    def __init__(self):
        self.buns = None
        self.ingredients = []

    def set_buns(self, bun):
        self.buns = bun

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index):
        if 0 <= index < len(self.ingredients):
            self.ingredients.pop(index)

    def move_ingredient(self, from_index, to_index):
        if (
            0 <= from_index < len(self.ingredients)
            and 0 <= to_index < len(self.ingredients)
        ):
            item = self.ingredients.pop(from_index)
            self.ingredients.insert(to_index, item)

    def get_total_price(self):
        if not self.buns:
            return sum(ing.get_price() for ing in self.ingredients)
        return self.buns.get_price() * 2 + sum(ing.get_price() for ing in self.ingredients)

    def get_receipt(self):
        receipt = f"(==== {self.buns.get_name()} ====)\n"
        for ing in self.ingredients:
            receipt += f"= {ing.get_type()} {ing.get_name()} =\n"
        receipt += f"(==== {self.buns.get_name()} ====)\n"
        receipt += f"Price: {self.get_total_price()}\n"
        return receipt
