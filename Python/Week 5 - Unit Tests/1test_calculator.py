
import pytest
from calculator import square

# # Manual Testing
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(4) == 16
#     assert square(-2) == 4
#     assert square(0) == 0

# Looping through the numbers is also an option:    

def test_square_positive():
    for i in range(2,10):
        assert square(i) == i * i

def test_square_negative():
    for i in range(-4,-1):
        assert square(i) == i * i

def test_square_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square('cat')