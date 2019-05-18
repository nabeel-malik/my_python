'''
Tuple and dictionary PACKING (with positional and keyword arguments, respectively) is covered in
xx_functions_and_arguments.py

This Python file demonstrates the use of tuple and dictionary UNPACKING alongside each other
'''

def add(a=0,b=0):
    print(a+b)

my_dict = {'a': 5, 'b': 6}      # the key name in the dictionary should be the same as the argument name in the function
my_tup = (3,6)


add(**my_dict)  # Dictionary unpacking: Unpacking multiple keys and their values from a dictionary into a function.
add(*my_tup)    # Tuple unpacking: Unpacking elements from a tuple into a function (positional arguments)
