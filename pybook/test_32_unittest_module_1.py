"""
A unit test is a smaller test, one that checks that a single part of your code operates in the right way.
A unit test helps you to isolate what is broken in your application and fix it faster.

The unittest module enables us to unit test our code.

https://stackless.readthedocs.io/en/latest/library/unittest.html
"""

import unittest

# Importing the module to be tested.
# The following line is the same as saying:     import 32_unittest_module_1 as unittest_module
unittest_module = __import__('32_unittest_module_1')  # to import a module starting with a digit in its name


# To create test methods, we first need to create a test class that inherits from the 'unittest.TestCase' class
class TestCalc(unittest.TestCase):

    # Then we need to define the test methods. And the test method names are 'required' to start with 'test'.
    # By convention, these methods are named starting with 'test_' followed by the name of the function/method to test
    def test_add(self):         # renaming this to 'testadd' would run the test, but 'add_test' would NOT run it.
        self.assertEqual(unittest_module.add(10, 5), 15)

        # Testing edge cases
        self.assertEqual(unittest_module.add(-1, 1), 0)
        self.assertEqual(unittest_module.add(-1, -1), -2)

    def test_substract(self):
        self.assertEqual(unittest_module.substract(10, 5), 5)
        self.assertEqual(unittest_module.substract(-1, 1), -2)
        self.assertEqual(unittest_module.substract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(unittest_module.multiply(10, 5), 50)
        self.assertEqual(unittest_module.multiply(-1, 1), -1)
        self.assertEqual(unittest_module.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(unittest_module.divide(10, 5), 2)
        self.assertEqual(unittest_module.divide(-1, 1), -1)
        self.assertEqual(unittest_module.divide(-1, -1), 1)

        # First way to test exceptions. Note: arguments are provided separately because our function would actually
        # throw that ValueError, and our test would think that something failed.
        self.assertRaises(ValueError, unittest_module.divide, 10, 0)

        # Second way to test exceptions is using a context manager. This is the preferred way.
        with self.assertRaises(ValueError):
            unittest_module.divide(10, 0)


# To be able to run the tests directly from the editor (instead of running it from command line)
# It is just saying if we run this module directly, then run the code within the conditional.
if __name__ == '__main__':
    unittest.main()






