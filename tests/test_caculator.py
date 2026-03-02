import pytest
from app.calculator import add, dev


def test_add():
    assert add(2, 3) == 5


def test_dev():
    assert dev(10, 2) == 5


def test_dev_by_zero():
    with pytest.raises(ValueError):
        dev(10, 0)
