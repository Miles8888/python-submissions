import pytest

from employee import Employee

@pytest.fixture
def michael():
    """Fixture to create an example employee."""
    return Employee('michael', 'woods', 75000)

def test_wage_increase(michael):
    """Test whether raising the default wage by its default amount works properly."""
    michael.give_raise()
    assert michael.salary == 80000

def test_wage_increase_custom(michael):
    """Test whether raising the default wage by a custom amount works properly."""
    michael.give_raise(15000)
    assert michael.salary == 90000