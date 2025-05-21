import pytest
from src.burger import Burger
from src.bun import Bun
from src.ingredient import Ingredient

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    return Bun("Булка", "bun", 2.0)

@pytest.fixture
def ingredient1():
    return Ingredient("Сыр", "main", 1.0)

@pytest.fixture
def ingredient2():
    return Ingredient("Соус", "sauce", 0.5)

def test_add_and_remove_ingredient(burger, ingredient1):
    burger.add_ingredient(ingredient1)
    assert burger.ingredients == [ingredient1]
    burger.remove_ingredient(0)
    assert burger.ingredients == []

def test_move_ingredient(burger, ingredient1, ingredient2):
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ingredient2, ingredient1]
