import pytest
from src.burger import Burger
from src.bun import Bun
from src.ingredient import Ingredient

@pytest.fixture
def bun():
    return Bun("Булка кунжутная", "bun", 100)

@pytest.fixture
def ing1():
    return Ingredient("Мясо", "main", 300)

@pytest.fixture
def ing2():
    return Ingredient("Салат", "vegetable", 50)

@pytest.fixture
def burger(bun, ing1, ing2):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    return burger

def test_set_buns_sets_correct_bun(bun):
    burger = Burger()
    burger.set_buns(bun)
    assert burger.buns == bun

def test_add_ingredient_appends_to_list(ing1):
    burger = Burger()
    burger.add_ingredient(ing1)
    assert burger.ingredients == [ing1]

def test_remove_ingredient_removes_correctly(ing1, ing2):
    burger = Burger()
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.remove_ingredient(0)
    assert burger.ingredients == [ing2]

def test_move_ingredient_changes_order(ing1, ing2):
    burger = Burger()
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ing2, ing1]

def test_get_total_price_with_bun_and_ingredients(burger):
    assert burger.get_total_price() == 2 * 100 + 300 + 50  # 550

def test_get_ingredients_names(burger):
    assert burger.get_ingredients_names() == ["Мясо", "Салат"]

def test_get_receipt_contains_bun_and_ingredients(burger):
    receipt = burger.get_receipt()
    assert "Булка кунжутная" in receipt
    assert "Мясо" in receipt
    assert "Салат" in receipt
    assert "Price: 550" in receipt
