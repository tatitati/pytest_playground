

import unittest
import source.calc as calc

def fun1(name: str, age: int) -> str:    
    return name + str(age)

def fun2(name: str, age) -> str:    
    return name + str(age)    


class TestCalc(unittest.TestCase):

    def test_basic(self):
        result1 = fun1("whatever", 5)
        result2 = fun2("whatever", 5)
        
        self.assertEqual(result1, "whatever5", "should be 15")
        self.assertEqual(result2, "whatever5", "should be 15")
        
