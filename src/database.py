class Database:
    def __init__(self):
        self.buns = []
        self.ingredients = []

    def add_bun(self, bun):
        self.buns.append(bun)

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_all_buns(self):
        return self.buns

    def get_all_ingredients(self):
        return self.ingredients
