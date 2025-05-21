import pytest
from src.bun import Bun
from src.ingredient import Ingredient
from src.database import Database

@pytest.fixture
def bun():
    return Bun("Булка кунжутная", "bun", 2.0)

@pytest.fixture
def ingredient():
    return Ingredient("Соус сырный", "sauce", 0.5)

@pytest.fixture
def db(bun, ingredient):
    db = Database()
    db.add_bun(bun)
    db.add_ingredient(ingredient)
    return db

def test_database_get_all_buns(db, bun):
    assert db.get_all_buns() == [bun]

def test_database_get_all_ingredients(db, ingredient):
    assert db.get_all_ingredients() == [ingredient]
