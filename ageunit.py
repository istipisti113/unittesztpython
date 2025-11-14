import unittest
from age_deter_test.age import *

class TestAgeCategorisation(unittest.TestCase):
    def test_categ_by_age(self):
        self.assertEqual(categ_by_age(5), "gyerek")