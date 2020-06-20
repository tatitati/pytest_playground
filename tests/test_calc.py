import unittest
import source.calc as calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEquals(result, 15, "should be 15")
