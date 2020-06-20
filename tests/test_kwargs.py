import unittest
from functools import partial
import source.calc as calc

class TestKwargs(unittest.TestCase):
    def test_basic(self):
        # create a new function that multiplies by 2
        mypartial = partial(calc.multiply,2)
        result = mypartial(4)

        self.assertEqual(result, 8, "should be 8")
