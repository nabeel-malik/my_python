import unittest
import importlib

# The following line is the same as saying:     from 33_unittest_module_2 import Employee as employee_class
employee_class = getattr(importlib.import_module('33_unittest_module_2'), 'Employee')


print('\nSTAGE 2: UNITTEST W/ setUp() & tearDown() INSTANCE METHODS AND setUpClass() & tearDownClass() CLASS METHODS\n')
"""
Notice how, in the previous example, we have to create the employee instances before each of the 3 tests with the 
following statements:
        emp_1 = employee_class('Corey', 'Schafer', 50000)
        emp_2 = employee_class('Sue', 'Smith', 60000)
So the statements to create employee instances appear multiple (3) times in our code. Code should always be 
DRY (Don't Repeat Yourself). This is where setUp() and tearDown() methods are useful.

The setUp() INSTANCE METHOD is run before EACH test, and the tearDown() INSTANCE METHOD is run after EACH test, 
i.e. before and after each: test_email(), test_fullname() and test_apply_raise(). So in our specific example, we can 
create employee instances in the setUp() INSTANCE METHOD. In our case we are not using the tearDown() INSTANCE METHOD, 
but it can be useful in cases where, for example, we create some directories during a test, and have to delete them 
before proceeding to the next test.

Similarly, the setUpClass() CLASS METHOD is run before the entire unit test file, and the tearDownClass() CLASS METHOD 
is run after the entire unit test file.

Note: setUp(), tearDown(), setUpClass() and tearDownClass() are built-in methods and have to be named exactly as shown
in the following example.
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


if __name__ == '__main__':
    unittest.main()
