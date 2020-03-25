"""
A programming language is said to have FIRST-CLASS FUNCTIONS if it treats functions as FIRST-CLASS CITIZENS.

A FIRST-CLASS CITIZEN (sometimes called FIRST-CLASS OBJECTS) in a programming language is an entity which supports all
the operations generally available to other entities. These operations typically include:
    - being assigned to a variable,
    - being passed as an argument, and
    - being returned from a function.

"""

print('\n################################# 1. ASSIGNING A FUNCTION TO A VARIABLE #################################\n')


def square(x):
    return x*x


a = square(5)       # the result of square() function is assigned to 'a'.
b = square          # the square() function, itself, is assigned to 'b', i.e. 'b' is a function.

print(a)            # will print what is returned from square() function
print(b)            # will print the function object and its location on memory
print(b(5))         # will print what is returned from function 'b'

print('\n####################### 2. PASSING A FUNCTION AS AN ARGUMENT (TO ANOTHER FUNCTION) #######################\n')
"""
Any function that either accepts another function as an argument, or returns a function, is called a HIGHER-ORDER
FUNCTION.
"""


# Function to be passed as an argument
def cube(x):
    return x * x * x


# Higher-order function (accepting another function as an argument)
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


my_output = my_map(cube, [1, 2, 3, 4, 5])       # notice that we do not put the () in after 'cube'.

print(my_output)

print('\n##################### 3. A FUNCTION BEING RETURNED FROM ANOTHER FUNCTION - EXAMPLE 1 #####################\n')


def logger(msg):
    def log_message():
        print('Log:', msg)

    return log_message


log_hi = logger('Hi!')          # log_hi is now equal to the function log_message that was returned.
log_hi()                        # it remembered the argument that we passed to the logger() function. This is CLOSURE.

print('\n##################### 4. A FUNCTION BEING RETURNED FROM ANOTHER FUNCTION - EXAMPLE 2 #####################\n')


def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_text


print_h1 = html_tag('h1')       # print_h1 is now equal to the function wrap_text that was returned.
print_h1('Test headline!')      # it remembered the argument that we passed to the html_tag() function. This is CLOSURE.
print_h1('Another headline!')

print()

print_p = html_tag('p')         # creating a new variable (function) with a different argument passed to html_tag()
print_p('Test paragraph!')


print('\n############################################## 5. CLOSURES ##############################################\n')
"""
A CLOSURE is a function object that remembers values in enclosing scopes even if they are not present in memory.
A CLOSURE 'closes' over the 'FREE VARIABLES' from its environment.
A 'FREE VARIABLE' is not defined in the current environment, i.e. in the collection of LOCAL variables, and is also 
not a GLOBAL variable. Therefore it must be defined elsewhere. And this is the concept of CLOSURES.

The following criteria must be met to create CLOSURE in Python:
    - We must have a nested function (function inside a function).
    - The nested function must refer to a value defined in the enclosing function.
    - The enclosing function must return the nested function.

Read more: https://www.programiz.com/python-programming/closure
"""


def outer_func(hello_hi):
    exclamation = hello_hi

    def inner_func(msg):
        print(exclamation, msg)

    return inner_func


hi_func = outer_func('Hi!')             # hi_func is now equal to the function inner_func that was returned.
hi_func('Python is fun!')               # inner_func() remembers the variable in the enclosing function --> CLOSURE

hello_func = outer_func('Hello!')
hello_func('Python rocks!')

