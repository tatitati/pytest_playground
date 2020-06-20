import unittest
from functools import partial
import source.calc as calc

def myFun1(*params):  
    initialText=""
    for arg in params:  
        initialText += arg + "!!"

    return initialText
    
def myFun2(name, *params):  
    initialText=name
    for arg in params:  
        initialText += arg + "!!"

    return initialText


class TestArgv(unittest.TestCase):
    
    def test_basic1(self):
        result = myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')  
        self.assertEqual(result, "Hello!!Welcome!!to!!GeeksforGeeks!!")

    def test_basic2(self):
        result = myFun2('Francisco', 'Hello', 'Welcome', 'to', 'GeeksforGeeks')  
        self.assertEqual(result, "FranciscoHello!!Welcome!!to!!GeeksforGeeks!!")
        
