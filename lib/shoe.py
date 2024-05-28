#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size  # This uses the setter method
        self.condition = None

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

# Testing the Shoe class to ensure it passes the provided tests
def run_tests():
    import io
    import sys

    class TestShoe:
        '''Shoe in shoe.py'''

        def test_has_brand_and_size(self):
            '''has the brand and size passed to __init__, and values can be set to new instance.'''
            stan_smith = Shoe("Adidas", 9)
            assert(stan_smith.brand == "Adidas")
            assert(stan_smith.size == 9)

        def test_requires_int_size(self):
            '''prints "size must be an integer" if size is not an integer.'''
            stan_smith = Shoe("Adidas", 9)
            captured_out = io.StringIO()
            sys.stdout = captured_out
            stan_smith.size = "not an integer"
            sys.stdout = sys.__stdout__
            assert captured_out.getvalue() == "size must be an integer\n"

        def test_can_cobble(self):
            '''says that the shoe has been repaired.'''
            stan_smith = Shoe("Adidas", 9)
            captured_out = io.StringIO()
            sys.stdout = captured_out
            stan_smith.cobble()
            sys.stdout = sys.__stdout__
            assert(captured_out.getvalue() == "Your shoe is as good as new!\n")
        
        def test_cobble_makes_new(self):
            '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
            stan_smith = Shoe("Adidas", 9)
            stan_smith.cobble()
            assert(stan_smith.condition == "New")

    test_shoe = TestShoe()
    test_shoe.test_has_brand_and_size()
    test_shoe.test_requires_int_size()
    test_shoe.test_can_cobble()
    test_shoe.test_cobble_makes_new()
    print("All tests passed!")

# Running the tests
run_tests()
