class Burger:
    def __init__(self):
        self.bun = None
        self.ingredients = []

    def add_bun(self, bun):
        self.bun = bun

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_total_price(self):
        if not self.bun:
            return sum(i.get_price() for i in self.ingredients)
        return 2 * self.bun.get_price() + sum(i.get_price() for i in self.ingredients)

    def get_ingredients_names(self):
        return [i.get_name() for i in self.ingredients]
