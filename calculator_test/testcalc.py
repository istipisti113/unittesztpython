import pytest
from calc import *

def test_sum():
    assert sum(3,5) == 8
    assert div(15,5) == 3
    assert mul(3,5) == 15
    assert sub(5,3) == 2
    print("helyes")
    