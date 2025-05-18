import pytest
from src.bun import Bun

@pytest.mark.parametrize("name, bun_type, price", [
    ("Чёрная булка", "black", 100),
    ("Белая булка", "white", 80),
])
def test_bun_attributes(name, bun_type, price):
    bun = Bun(name, bun_type, price)
    assert bun.get_name() == name
    assert bun.get_type() == bun_type
    assert bun.get_price() == price
