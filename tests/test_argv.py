import unittest
from functools import partial
import source.calc as calc

def myFun(*params):  
    initialText=""
    for arg in params:  
        initialText += arg + "!!"

    return initialText
    

class TestArgv(unittest.TestCase):
    
    def test_basic(self):
        result = myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')  
        self.assertEqual(result, "Hello!!Welcome!!to!!GeeksforGeeks!!")
        
