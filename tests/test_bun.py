import pytest
from src.bun import Bun

@pytest.mark.parametrize("name, bun_type, price", [
    ("Чёрная булка", "black", 100),
    ("Белая булка", "white", 80),
])

@pytest.fixture
def sample_bun():
    return Bun("Классическая булка", "bun", 2.5)

def test_bun_get_name(sample_bun):
    assert sample_bun.get_name() == "Классическая булка"

def test_bun_get_type(sample_bun):
    assert sample_bun.get_type() == "bun"

def test_bun_get_price(sample_bun):
    assert sample_bun.get_price() == 2.5

