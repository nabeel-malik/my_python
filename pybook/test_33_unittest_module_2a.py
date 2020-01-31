import unittest
import importlib

# The following line is the same as saying:     from 33_unittest_module_2 import Employee as employee_class
employee_class = getattr(importlib.import_module('33_unittest_module_2'), 'Employee')


print('\n#################################### STAGE 1: REGULAR UNIT TEST SETUP ####################################\n')


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = employee_class('Corey', 'Schafer', 50000)
        emp_2 = employee_class('Sue', 'Smith', 60000)

        self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Sue.Smith@email.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        emp_1 = employee_class('Corey', 'Schafer', 50000)
        emp_2 = employee_class('Sue', 'Smith', 60000)

        self.assertEqual(emp_1.fullname, 'Corey Schafer')
        self.assertEqual(emp_2.fullname, 'Sue Smith')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'John Schafer')
        self.assertEqual(emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        emp_1 = employee_class('Corey', 'Schafer', 50000)
        emp_2 = employee_class('Sue', 'Smith', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
