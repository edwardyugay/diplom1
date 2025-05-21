import pytest
from src.ingredient import Ingredient

@pytest.fixture
def sample_ingredient():
    return Ingredient("Соус барбекю", "sauce", 1.0)

def test_ingredient_get_name(sample_ingredient):
    assert sample_ingredient.get_name() == "Соус барбекю"

def test_ingredient_get_category(sample_ingredient):
    assert sample_ingredient.get_category() == "sauce"

def test_ingredient_get_price(sample_ingredient):
    assert sample_ingredient.get_price() == 1.0
