from main import valid_addition
from main import valid_substraction
from main import valid_multiplication
from main import valid_division


def test_valid_addition():
    
    assert valid_addition("1 + 1 =") == True


def test_valid_substraction():
    
    assert valid_substraction("1 - 1 =") == True


def test_valid_multiplication():
    
    assert valid_multiplication("1 x 1 =") == True


def test_valid_division():
    
    assert valid_division("1 / 1 =") == True