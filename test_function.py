import pytest
from function import subtract_two_numbers

def test_subtract_two_numbers():
    assert subtract_two_numbers(4, 2) == 2
    assert subtract_two_numbers(1, 3) == -2
    assert subtract_two_numbers(4.2, 2.1) == 2.1





