'''  
Patching Objects in Unit Tests
<>
You’re writing unit tests and need to apply patches to selected objects in order to make
assertions about how they were used in the test (e.g., assertions about being called with
certain parameters, access to selected attributes, etc.).


The unittest.mock.patch() function can be used to help with this problem. It’s a little
unusual, but patch() can be used as a decorator, a context manager, or stand-alone. For
example, here’s an example of how it’s used as a decorator:
'''

# from unittest.mock import patch 
# import example 

# @patch('example.func')
# def test1(x, mock_func):
#     example.func(x)
#     mock_func.assert_called_with(x)  

''''  
Testing for Exceptional Conditions in Unit Tests 

<> to write unit test that cleanly tests if an exception is raised.
To test for exceptions, use the assertRaises() method
'''
import unittest

# A simple function to illustrate 
def parse_int(s):
    return int(s)

class TestConversion(unittest.TestCase):
    def test_bid_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')

        
