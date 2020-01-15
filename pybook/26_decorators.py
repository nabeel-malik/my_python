"""
A DECORATOR is a function that takes in another function as an argument, adds some functionality to it ('decorates' it),
and returns it, without altering the source code of the original function that was passed in.

The function that 'decorates' is the DECORATOR FUNCTION
The function being 'decorated' (i.e. passed in as an argument to the DECORATOR FUNCTION) is the DECORATED FUNCTION.

"""

print('\n#################################### 1. THE SIMPLEST DECORATOR EXAMPLE ####################################\n')


# Decorator function
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))  # added functionality
        return original_function()
    return wrapper_function


# Function to be passed as an argument, DECORATED FUNCTION
def display():
    print('display function ran!')


decorated_display = decorator_function(display)   # decorated_display is now equal to the function wrapper_function.
decorated_display()


print('\n################################# 2. SYNTAX USED FOR DECORATORS IN PYTHON #################################\n')
"""
The following syntax is functionally the same as used in the section above, but it is easier to read, and commonly used 
for decorators in Python.
"""


# Decorator function
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))     # added functionality
        return original_function()
    return wrapper_function


@decorator_function         # this is the same as saying:   display = decorator_function(display)
def display():
    print('display function ran!')

# The following 2 lines of code are no longer needed with the use of @decorator_function above.
# decorated_display = decorator_function(display)
# decorated_display()


display()                   # would run the display() function with the added functionality from wrapper_function()


print('\n################################# 3. DECORATED FUNCTION WITH ARGUMENTS #################################\n')
"""
If the DECORATED FUNCTION takes in some arguments, the DECORATOR FUNCTION from the previous sections would not work,
and would have to be modified such that the wrapper_function() is able to take in arguments.
"""


# Decorator function
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))     # added functionality
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function         # this is the same as saying:   display = decorator_function(display)
def display():
    print('display function ran!')


@decorator_function
def display_info(name, age):
    print('display info ran with arguments {} and {}'.format(name, age))


display()                   # would run the display() function with the added functionality from wrapper_function()
display_info('John', 25)
