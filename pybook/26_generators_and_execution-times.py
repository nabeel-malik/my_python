import random       # used later in sections 4 and 5.
import time         # used later in sections 4 and 5.
import timeit       # used later in section 5.

"""
Python GENERATORS are a simple way of creating iterators.
Simply put, a GENERATOR is a function that returns an object (iterator) which we can iterate over (one value at a time).

It is fairly simple to create a GENERATOR in Python. It is as easy as defining a normal function with 'yield' statement
instead of a 'return' statement.
If a function contains at least one 'yield' statement (it may contain other yield or return statements), it becomes a
GENERATOR FUNCTION.
"""


# GENERATOR FUNCTION
def square_numbers(nums):
    for i in nums:
        yield (i * i)       # 'yield' keyword is what makes this function a GENERATOR FUNCTION


my_nums = square_numbers([1, 2, 3, 4, 5])       # 'my_nums' will be the generator object (iterator)

print(my_nums)              # will print the generator object and its location on memory


print('\n################################# 1. USING print(next()) WITH GENERATORS #################################\n')

# The print(next(my_nums)) command can be used multiple times to print the next value from the generator
# Running print(next(my_nums)) for a 6th time gives 'StopIteration' error

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
# print(next(my_nums))      # comment in to see 'StopIteration' error


print('\n################################### 2. USING for LOOP WITH GENERATORS ###################################\n')

my_nums = square_numbers([1, 2, 3, 4, 5])       # generators can not be 'rewound', they have to be run again to restart

for x in my_nums:           # printing generator output using a 'for' loop
    print(x)


print('\n############################# 3. GENERATOR EXPRESSION (VS LIST COMPREHENSION) #############################\n')

"""
The syntax for GENERATOR EXPRESSION is similar to that of a list comprehension, except that the [] are replaced with ().

GENERATORS produce items only when asked for. For this reason, GENERATOR EXPRESSIONS are much more memory efficient 
than an equivalent list comprehension.
"""

# my_nums = [x*x for x in [1, 2, 3, 4, 5]]      # this would be the equivalent list comprehension
my_nums = (x*x for x in [1, 2, 3, 4, 5])        # GENERATOR EXPRESSION

for x in my_nums:           # printing generator output using a 'for' loop
    print(x)


print('\n########################### 4. GENERATORS VS LISTS - time.perf_counter() METHOD ###########################\n')

"""
From the different clocks available in the time module, time.perf_counter() will give you the most accurate results 
when testing the difference between two times.
Python clocks explained here: https://www.webucator.com/blog/2015/08/python-clocks-explained/

timeit is the preferred way to measure execution time for code snippets, and it uses time.perf_counter() by default. 
See next section.
"""

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person        # Notice how 'yield' is placed INSIDE the for loop, as opposed to 'return' statement above.


# Timing the LIST
t1 = time.perf_counter()
people_l = people_list(1000000)
t2 = time.perf_counter()

# Timing the GENERATOR
t3 = time.perf_counter()
people_g = people_generator(1000000)
t4 = time.perf_counter()

print('Time taken for a list is:\t\t', t2-t1)
print('Time taken for a generator is:\t', t4-t3)


print('\n############################# 5. GENERATORS VS LISTS - timeit.timeit() METHOD #############################\n')

"""
timeit() method is available with python library timeit. It is used to get the execution time taken for small code 
snippets. This is the preferred method to time the execution of code snippets. The default timer for timeit() method is
time.perf_counter().

The timeit() method runs <setup> once, then executes <stmt> repeatedly and returns the amount of time which passes. 
The <number> argument to timeit() controls how many times to run the statement; the default is 1000000.

Syntax:         timeit.timeit(stmt, setup, timer, number)
Parameters:     stmt: This will take the CODE for which you want to measure the execution time. The default is "pass".
                setup: This will have setup details that need to be executed BEFORE stmt. The default is "pass."
                timer: This will have the timer value, timeit() already has a default value set, and we can IGNORE it.
                number: The stmt will execute as per the NUMBER is given here. The default value is 1000000.
                
"""

import_modules = 'import time, random'                  # defining string for modules to be imported before

test_code_list = '''
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result


people = people_list(1000000)
'''

test_code_generator = '''
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person
        
        
people = people_generator(1000000)
'''

print('Time taken for a list is:\t\t', timeit.timeit(setup=import_modules, stmt=test_code_list, number=1))
print('Time taken for a generator is:\t', timeit.timeit(setup=import_modules, stmt=test_code_generator, number=1))
