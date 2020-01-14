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


my_nums = square_numbers([1, 2, 3, 4, 5])       # 'my_nums' will be the generator object (iterator) yielded

print(my_nums)              # will print the generator object and its location

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

print('\n########################### 4. GENERATORS VS LISTS - MEMORY AND TIME EFFICIENCY ###########################\n')

import random
import time

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
        yield person

# Comment next 3 lines in, and following 3 lines out, in to see the time efficiency of LISTS
# t1 = time.perf_counter()
# people = people_list(1000000)
# t2 = time.perf_counter()


# Comment next 3 lines in, and previous 3 lines out, in to see the time efficiency of GENERATORS
t1 = time.perf_counter()
people = people_generator(1000000)
t2 = time.perf_counter()

print('Took {} Seconds'.format(t2-t1))