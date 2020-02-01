import unittest
from unittest.mock import patch
import importlib

# The following line is the same as saying:     from 33_unittest_module_2 import Employee as employee_class
employee_class = getattr(importlib.import_module('33_unittest_module_2'), 'Employee')


print('\n################# STAGE 3: USING patch() FROM unittest.mock WHEN USING EXTERNAL SERVICES #################\n')
"""
The information from the website, that the monthly_schedule() method gets, is something we want to 'mock', because we 
do not want the success of our test to depend on the website being operational.
The only things we care about for this test are that:
    - the get() method is called with the correct URL, and
    - our code behaves correctly whether the response is okay or not okay.

unittest.mock provides a powerful mechanism for mocking objects, called patch(), which looks up an object in a given 
module and replaces that object with a Mock object.
Usually, you use patch() as a decorator or a context manager to provide a scope in which you will mock the target 
object. In this example, we will use patch() as a context manager. See: def test_monthly_schedule()

unittest.mock library is something that we can study in more detail, but it is not used a whole lot in regular 
programming, and therefore, can be studied in more detail as and when the need arises.
"""


class TestEmployee(unittest.TestCase):

    # setUpClass() CLASS METHOD
    @classmethod
    def setUpClass(cls):
        print('\nsetUpClass()')

    # tearDownClass() CLASS METHOD
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass()')

    # setUp() INSTANCE METHOD
    def setUp(self):
        print('\nsetUp()')
        # Creating instances. Note: how the instances have to be setup as instance 'attributes', i.e. self.XXX
        self.emp_1 = employee_class('Corey', 'Schafer', 50000)
        self.emp_2 = employee_class('Sue', 'Smith', 60000)

    # tearDown() INSTANCE METHOD
    def tearDown(self):
        print('tearDown()\n')

    def test_email(self):
        print('test_email()')

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname()')

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise()')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):

        # patch() being run as a context manager
        with patch('33_unittest_module_2.requests.get') as mocked_get:      # note: module imported as path string"

            """ To check the SUCCESSFUL case """

            # Creating a mock object for requests.get in XX_unittest_module_2.py
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            # Running monthly_schedule() method just so we can test it
            schedule = self.emp_1.monthly_schedule('May')

            # The actual tests
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success!')

            """ To check the UNSUCCESSFUL case """

            # Creating a mock object for requests.get in XX_unittest_module_2.py
            mocked_get.return_value.ok = False
            # mocked_get.return_value.text = 'Success!'     # note: not needed as return comes from monthly_schedule()

            # Running monthly_schedule() method just like we are testing it
            schedule = self.emp_2.monthly_schedule('June')

            # The actual tests
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad response!')


if __name__ == '__main__':
    unittest.main()
