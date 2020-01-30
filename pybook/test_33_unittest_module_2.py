import unittest

# The following line is the same as saying:     from 33_unittest_module_2 import Employee as employee_class
employee_class = __import__('33_unittest_module_2', fromlist=['Employee'])


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = employee_class('Corey', 'Schafer', 50000)

