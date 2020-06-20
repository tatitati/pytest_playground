import unittest
from functools import partial
import source.calc as calc

def myFun1(**kwargs):  
    initialText = ""
    for key, value in kwargs.items(): 
        initialText += key + "=>" +  value

    return initialText

def myFun2(name, **kwargs):  
    initialText = name
    for key, value in kwargs.items(): 
        initialText += key + "=>" +  value

    return initialText
    

class TestKwargs(unittest.TestCase):
    
    def test_basic1(self):
        result1 = myFun1(first ='Geeks', mid ='for', last='Geeks')          
        self.assertEqual(result1, "first=>Geeksmid=>forlast=>Geeks")

        mykwargs = {"first":'Geeks', "mid":'for', "last": 'Geeks'}
        result2 = myFun1(**mykwargs)          
        self.assertEqual(result2, "first=>Geeksmid=>forlast=>Geeks")


    def test_basic2(self):
        result = myFun2('francisco', first ='Geeks', mid ='for', last='Geeks')          
        self.assertEqual(result, "franciscofirst=>Geeksmid=>forlast=>Geeks")

        
        
