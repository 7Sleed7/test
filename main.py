import pytest
from calculator import Сalculator

cal = Сalculator()

def test_addition():
    assert cal.add(5, 7) == 12

def test_subtraction():
    assert cal.subtract(1, 11) == -10

def test_multiplication():
    assert cal.multiply(7, 8) == 56

def test_division():
    assert cal.divide(12, 4) == 3
    assert cal.divide(2, 0) == "Error: division by zero"

def test_exponentiation():
    assert cal.exponentiation(2, 5) == 32
    assert cal.exponentiation(0, -2) == "Error: 0 cannot be raised to a negative power"


