from unittest.mock import Mock
from src.burger import Burger

def test_burger_total_price_with_bun_and_ingredients():
    bun = Mock(get_price=lambda: 100, get_name=lambda: "Булка")
    meat = Mock(get_price=lambda: 300, get_name=lambda: "Мясо")
    salad = Mock(get_price=lambda: 50, get_name=lambda: "Салат")

    burger = Burger()
    burger.add_bun(bun)
    burger.add_ingredient(meat)
    burger.add_ingredient(salad)

    assert burger.get_total_price() == 2 * 100 + 300 + 50
    assert burger.get_ingredients_names() == ["Мясо", "Салат"]
