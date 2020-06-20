

import unittest
import source.calc as calc

def fun1(name: str, age: int) -> str:    
    return name + str(age)


class TestCalc(unittest.TestCase):

    def test_basic(self):
        result = fun1("whatever", 5)
        self.assertEqual(result, "whatever5", "should be 15")
        
