import unittest
from functools import partial
import source.calc as calc

class TestPartials(unittest.TestCase):
    def test_basic(self):
        # create a new function that multiplies by 2
        mypartial = partial(calc.multiply,2)
        result = mypartial(4)

        self.assertEquals(result, 8, "should be 8")
