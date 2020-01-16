"""
A DECORATOR can be implemented in Python in the form of a DECORATOR FUNCTION or a DECORATED CLASS.

A DECORATOR is a function or class that takes in another function as an argument, adds some functionality to it
('decorates' it), and returns it, without altering the source code of the original function that was passed in.

The function/class that 'decorates' is a DECORATOR FUNCTION/CLASS
The function being 'decorated' (i.e. passed in as an argument to the DECORATOR FUNCTION/CLASS) is a DECORATED FUNCTION.

"""

print('\n############################### 1. THE SIMPLEST DECORATOR FUNCTION EXAMPLE ###############################\n')


# DECORATOR FUNCTION
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))  # added functionality
        return original_function()
    return wrapper_function                     # notice that wrapper_function 'object' is returned, and not its result


# DECORATED FUNCTION (Function to be passed as an argument)
def display():
    print('display() ran!')


decorated_display = decorator_function(display)   # decorated_display is now equal to the function wrapper_function.
decorated_display()


print('\n############################ 2. SYNTAX USED FOR DECORATOR FUNCTIONS IN PYTHON ############################\n')
"""
The following syntax is functionally the same as used in the section above, but it is easier to read, and commonly used 
for decorators in Python.

The following is a DECORATOR FUNCTION example. An example for the syntax of a DECORATOR CLASS is in section 4.
"""


# DECORATOR FUNCTION
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))     # added functionality
        return original_function()
    return wrapper_function


@decorator_function     # this is the same as: 'display = decorator_function(display)' placed AFTER display() definition
def display():
    print('display() ran!')

# The following 2 lines of code are no longer needed with the use of @decorator_function above.
# decorated_display = decorator_function(display)
# decorated_display()


display()                   # would run the display() function with the added functionality from wrapper_function()


print('\n################################# 3. DECORATED FUNCTION WITH ARGUMENTS #################################\n')
"""
If the DECORATED FUNCTION takes in some arguments, the DECORATOR FUNCTION from the previous sections would not work,
and would have to be modified such that the wrapper_function() is able to take arguments.
"""


# DECORATOR FUNCTION
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))     # added functionality
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function     # this is the same as: 'display = decorator_function(display)' placed AFTER display() definition
def display():
    print('display() ran!')


@decorator_function
def display_info(name, age):
    print('display_info() ran with arguments {} and {}!'.format(name, age))


display()                   # would run the display() function with the added functionality from wrapper_function()
display_info('John', 25)


print('\n############################# 4. SYNTAX USED FOR DECORATOR CLASSES IN PYTHON #############################\n')
"""
Here we will present the code for a DECORATOR CLASS with exactly the same functionality as the DECORATOR FUNCTION in 
Section 3 above.
DECORATOR FUNCTIONS are used more commonly than DECORATOR CLASSES, but it is important to know the syntax difference.
"""


# DECORATOR CLASS
class DecoratorClass(object):               # not sure why 'object' is added in (). Removing it works fine as well.
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))  # added functionality
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display():
    print('display() ran!')


@DecoratorClass
def display_info(name, age):
    print('display_info() ran with arguments {} and {}!'.format(name, age))


display()                   # would run the display() function with the added functionality from call method
display_info('John', 25)


print('\n############################## 5. LOGGING USE-CASE FOR DECORATOR FUNCTIONS ##############################\n')
"""
The logging module is used to log how many times a particular function has been run, and with what arguments.
To log any of the functions we use in our program, decorators alongwith the logging module can be used as an elegant
solution.

Notice how, in the following example, the decorator allows us to maintain our added functionality in one location, and
apply it at multiple locations anywhere in our codebase.
"""


# DECORATOR FUNCTION
def my_logger(orig_func):

    import logging
    logging.basicConfig(filename='work_directory/decorators/{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'. format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    print('display_info() ran with arguments {} and {}!'.format(name, age))


display_info('John', 25)
display_info('Hans', 30)
display_info('Layla', 33)


print('\n############################## 6. TIMING USE-CASE FOR DECORATOR FUNCTIONS ##############################\n')
"""
DECORATORS can also be used to time how long it takes to run functions, without altering their original code.
"""

import time


# DECORATOR FUNCTION
def my_timer(orig_func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = orig_func(*args, **kwargs)     # display_info() runs here
        t2 = time.perf_counter()
        print('{} ran in {} seconds'.format(orig_func.__name__, t2-t1))
        return result           # this line can be commented out since orig_func(*args, **kwargs) has already been run

    return wrapper


@my_timer
def display_info(name, age):
    time.sleep(2)           # time delay added just to take 2 more seconds to run the function.
    print('display_info() ran with arguments {} and {}!'.format(name, age))


display_info('Layla', 33)


print('\n#################### 7. COMBINED LOGGING AND TIMING USE-CASE FOR DECORATOR FUNCTIONS ####################\n')
"""
To implement 'both' DECORATOR FUNCTIONS on the display_info() function, we can simply add both @my_logger and @my_timer
above display_info() function definition. This would be equivalent to display_info = my_logger(my_timer(display_info)).
In this case, to ensure that, during execution, the functions are named correctly when running the decorators 
sequentially, we have to import wraps from functools, and then decorate all of our wrapper functions with the 
@wraps decorator, with the DECORATED FUNCTION argument name as an argument to it.
"""

from functools import wraps


# LOGGING DECORATOR FUNCTION
def my_logger(orig_func):

    import logging
    logging.basicConfig(filename='work_directory/decorators/{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)           # nested @wraps decorator, with the DECORATED FUNCTION argument name as an argument
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'. format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


# TIMING DECORATOR FUNCTION
def my_timer(orig_func):

    @wraps(orig_func)           # nested @wraps decorator, with the DECORATED FUNCTION argument name as an argument
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = orig_func(*args, **kwargs)     # display_info() runs here
        t2 = time.perf_counter()
        print('{} ran in {} seconds'.format(orig_func.__name__, t2-t1))
        return result           # this line can be commented out since orig_func(*args, **kwargs) has already been run

    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(2)           # time delay added just to take 2 more seconds to run the function.
    print('display_info() ran with arguments {} and {}!'.format(name, age))


'''
When we run the display_info() function now, we should expect to see all 3 of the following:
    - display_info() executed with its contained print() message
    - the time it took to run the function from the my_timer() DECORATOR FUNCTION, and
    - a log of the function run in the display_info.log file created by the my_logger DECORATOR FUNCTION.
and the time it took to run the function.
'''
display_info('Hemant', 48)

