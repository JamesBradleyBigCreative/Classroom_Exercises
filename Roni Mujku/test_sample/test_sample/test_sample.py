from module1 import func
import pytest

class A():
    def __init__(self):
        self.name = ""
        self.list = []
        self.limit = 5
    
    def ADD(self,x):
        if len(self.list) == self.limit:
            raise OverflowError("cannot add more items")
        self.list.append(x)

    def Get_Total(self):
        pass
        

def test_answer():
    assert func(4) == 5

def test_A():
    string = "AAAAAAA"
    string += "A"

def test_Adding():
    Temp = A()
    for i in range(5):
        Temp.ADD("placeholder")
    with pytest.raises(OverflowError):
        for i in range(1):
            Temp.ADD("placeholder")
    print(Temp.list)

def test_get_total():
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    cart = A()
    cart.add("apple")
    cart.add("orange")
  
    pass