import pylint

"""
The built-in exceptions in Python 3.7 can be viewed here: https://docs.python.org/3.7/library/exceptions.html
"""

print('\n############################### 1. try, except, else, finally - EXAMPLE 1 ###############################\n')

try:
    with open('work_directory/errors_and_exceptions_handling/testfile.txt', 'r') as f:
        f.write('This is a test line.')

except TypeError:
    print('There was a type error!')

except OSError: # we will get and OSError because we opened the file in read mode, but are attempting to write to it.
    print('There was an OS error')

except:                             # PEP8 recommends not to use bare 'except'
    print('All other exceptions.')

else:
    print('No error was raised.')

finally:
    print('I always run.')

print('\n######################## 2. try, except, else, finally WITH while True - EXAMPLE 2 ########################\n')
"""
This example shows how can we take user input, check it for errors/exceptions, and continue to ask for input until 
the expected input is provided. 'while True' is commonly used for this.
"""

while True:
    try:
        user_input = int(input('Please provide an integer: '))
    except ValueError:
        print('Invalid entry!')
        continue                    # 'continue' is not needed here, but is added just to make the logic clear.
    else:
        print('Thank you. The integer provided is', user_input)
        break                       # will break out of the 'while True' loop
