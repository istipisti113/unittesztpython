import pytest
from calc import *

def test_sum():
    assert sum(3,5) == 8
def test_div():
    assert div(15,5) == 3
def test_mul():
    assert mul(3,5) == 15
def test_sub():
    assert sub(5,3) == 2
    