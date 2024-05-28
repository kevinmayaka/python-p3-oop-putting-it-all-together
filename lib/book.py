#!/usr/bin/env python3

import io
import sys

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count  # This uses the setter method

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

# Testing the Book class to ensure it passes the provided tests
def run_tests():
    # Test case 1: has title and page_count
    book1 = Book("And Then There Were None", 272)
    assert(book1.page_count == 272)
    assert(book1.title == "And Then There Were None")

    # Test case 2: requires int page_count
    book2 = Book("And Then There Were None", 272)
    captured_out = io.StringIO()
    sys.stdout = captured_out
    book2.page_count = "not an integer"
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "page_count must be an integer\n"

    # Test case 3: can turn page
    book3 = Book("The World According to Garp", 69)
    captured_out = io.StringIO()
    sys.stdout = captured_out
    book3.turn_page()
    sys.stdout = sys.__stdout__
    assert(captured_out.getvalue() == "Flipping the page...wow, you read fast!\n")

    print("All tests passed!")

# Running the tests
run_tests()
