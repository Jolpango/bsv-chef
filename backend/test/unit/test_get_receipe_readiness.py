import pytest
import unittest.mock as mock

from src.controllers.receipecontroller import ReceipeController
from src.static.diets import Diet
from src.util.calculator import calculate_readiness

def load_receipes(self):
    return []

def calc():
    return 1.0

@pytest.mark.unit
def test_not_complies_dietary_restrictions():
    mock_dao = mock.MagicMock()
    with (mock.patch.object(ReceipeController, "load_receipes", new = load_receipes)):
        sut = ReceipeController(mock_dao)
        recipe = { "diets": ["vegetarian"] }
        readiness = sut.get_receipe_readiness(recipe, None, diet=Diet.VEGAN)
        assert readiness is None
    assert True

@pytest.mark.unit
@mock.patch("src.util.calculator.calculate_readiness", autospec=True)
def test_complies_valid_readiness(mock_calculate):
    mock_calculate.return_value = 1.0
    mock_dao = mock.MagicMock()
    with (mock.patch.object(ReceipeController, "load_receipes", new = load_receipes)):
        sut = ReceipeController(mock_dao)
        recipe = { "diets": ["vegan"], "ingredients": [] }
        readiness = sut.get_receipe_readiness(recipe, None, diet=Diet.VEGAN)
        assert readiness == 1

# add your test case implementation here
@pytest.mark.unit
@mock.patch("src.util.calculator.calculate_readiness", autospec=True)
def test_low_readiness(mock_calculate):
    mock_calculate.return_value = 0.05
    mock_dao = mock.MagicMock()
    with (mock.patch.object(ReceipeController, "load_receipes", new = load_receipes)):
        sut = ReceipeController(mock_dao)
        recipe = { "diets": ["vegan"], "ingredients": [] }
        readiness = sut.get_receipe_readiness(recipe, None, diet=Diet.VEGAN)
        assert readiness is None
