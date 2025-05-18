import pytest
from src.ingredient import Ingredient

@pytest.mark.parametrize("name, category, price", [
    ("Мясо", "main", 300),
    ("Салат", "vegetable", 50),
])
def test_ingredient_attributes(name, category, price):
    ing = Ingredient(name, category, price)
    assert ing.get_name() == name
    assert ing.get_category() == category
    assert ing.get_price() == price
