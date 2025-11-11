import pytest
from fuel import get_fraction


def test_valid_fractions():
    """Test valid fractions that return percentages"""
    assert get_fraction("1/4") == "25%"
    assert get_fraction("1/2") == "50%"
    assert get_fraction("3/4") == "75%"


def test_empty_fuel():
    """Test fractions that return 'E' (empty, <= 1%)"""
    assert get_fraction("1/100") == "E"


def test_full_fuel():
    """Test fractions that return 'F' (full, >= 99%)"""
    assert get_fraction("99/100") == "F"


def test_numerator_greater_than_denominator():
    """Test when numerator > denominator, should return None"""
    assert get_fraction("5/4") == None
    assert get_fraction("10/3") == None


def test_invalid_format():
    """Test invalid format (not a fraction), should return None"""
    assert get_fraction("5") == None
    assert get_fraction("1-4") == None
    assert get_fraction("1/2/3") == None


def test_non_numerical_values():
    """Test non-numerical input, should raise ValueError"""
    with pytest.raises(ValueError):
        get_fraction("a/b")
    with pytest.raises(ValueError):
        get_fraction("1/a")
    with pytest.raises(ValueError):
        get_fraction("a/4")


def test_division_by_zero():
    """Test division by zero, should raise ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        get_fraction("1/0")
    with pytest.raises(ZeroDivisionError):
        get_fraction("5/0")