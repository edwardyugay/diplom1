from unittest.mock import Mock
from src.database import Database

def test_database_add_and_get_buns_ingredients():
    db = Database()
    bun = Mock()
    ing = Mock()

    db.add_bun(bun)
    db.add_ingredient(ing)

    assert db.get_all_buns() == [bun]
    assert db.get_all_ingredients() == [ing]
