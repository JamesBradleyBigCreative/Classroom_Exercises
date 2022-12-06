from module1 import *
import pytest
def test_can_add_item_to_cart():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert "apple" in cart.get_items()

def test_max_size():
   cart = ShoppingCart(5)
   for i in range(5):
        cart.add("apple")
   
   with pytest.raises (OverflowError):
        cart.add("apple")



   