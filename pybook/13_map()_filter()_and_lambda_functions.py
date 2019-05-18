"""
The map() function applies a given function to each item of an iterable and returns a map object.

The filter() method filters the elements of an iterable for which the specified function returns True,
and returns an iterator with the filtered results.

lambda functions are anonymous functions with the syntax: <lambda arguments: expression>
lambda functions are usually used for single-use, in-line functions.
"""

print("\n###################################### 1. map() FUNCTION ######################################\n")


def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return 'ODD'


names = ['Andy', 'Eve', 'Sally', 'George']

for item in map(splicer, names):
    print(item)

print("\n###################################### 2. filter() FUNCTION ######################################\n")


def check_even(mystring):
    return len(mystring)%2 == 0


names = ['Andy', 'Eve', 'Sally', 'George']

for item in filter(check_even, names):      # Note: The function argument to filter() should always return a boolean.
    print(item)

print("\n###################################### 3. lambda FUNCTION ######################################\n")

result = lambda num: num**2
print(result(5))

'''
But lambdas are anonymous functions. So typically we would not name them (by assigning them to a variable).
Most of the times lambdas are used in conjunction with other functions like map() and filter().
'''

print("\n######################### 3. lambda FUNCTION IN CONJUNCTION WITH map() #########################\n")

numlist = [1,2,3,4,5,6]

for item in map(lambda num: num**2, numlist):       # You could iterate through the returned map object from map()
    print(item)

print(list(map(lambda num: num**2, numlist)))       # You could also apply list()to the returned map object from map()

print("\n######################### 3. lambda FUNCTION IN CONJUNCTION WITH filter() #########################\n")

names = ['Andy', 'Eve', 'Sally', 'George']

for item in filter(lambda mystring: len(mystring)%2 == 0, names):   # Iterating through the returned iterator
    print(item)

print(list(filter(lambda mystring: len(mystring)%2 ==0, names)))    # Applying list() to the returned iterator