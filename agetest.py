import pytest
from age_deter_test.age import *

def test_categ_by_age():
    assert categ_by_age(5) == "gyerek"