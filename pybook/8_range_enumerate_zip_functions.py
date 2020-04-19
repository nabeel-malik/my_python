"""
The range() function RETURNS an immutable sequence of numbers between the given start integer and stop integer.

The enumerate() function adds counter to an iterable and RETURNS an enumerate object (in our case a list of tuples).

The zip() function takes in iterables as arguments and returns an iterator of tuples. This iterator generates a
series of tuples containing elements from each iterable. zip() can accept any type of iterable, such as files, lists,
tuples, dictionaries, sets, and so on.

The zip() function can also be used to UNZIP using the UNPACKING OPERATOR (*). Say you have a list of tuples and want
to separate the elements of each tuple into independent sequences. To do this, you can use zip() along with the
unpacking operator (*). See section 4.
"""

print('\n#################### 1. range() ####################\n')

for num in range(1,11):
    print(num)

list_from_range = list(range(0,11,2))
print('\n', list_from_range)

print('\n#################### 2. enumerate() ####################\n')

foodlist = ['nuts', 'beans', 'veggies', 'fruit']
print('foodlist:\t', foodlist, '\n')

print('for item in enumerate(foodlist):\t\tprint(item)')
for item in enumerate(foodlist):
    print(item)

print()

print('for item in enumerate(foodlist, start=1):\t\tprint(item)')
for item in enumerate(foodlist, start=1):
    print(item)

print()

print('list_enumerate = list(enumerate(foodlist, start=1))\t\tprint(list_enumerate)')
list_enumerate = list(enumerate(foodlist, start=1))     # casting the enumerate object to a list
print(list_enumerate)

print()

print('for index, item in enumerate(foodlist, start=1):\t\tprint(index, item)')
for index, item in enumerate(foodlist, start=1):    # unpacking the enumerate object
    print(index, item)

print('\n#################### 3. USING zip() TO ZIP ITERABLES ####################\n')

mylist1 = ['a','b','c']
mylist2 = [1,2,3]
print('mylist1:\t', mylist1)
print('mylist2:\t', mylist2)

print()

print('for item in zip(mylist1, mylist2):\t\tprint(item)')
for item in zip(mylist1, mylist2):
    print(item)

print()

print('list_zip = list(zip(mylist1, mylist2))\t', 'print(list_zip)')
list_zip = list(zip(mylist1, mylist2))      # casting the zip object to a list
print(list_zip)


print()

print('for item1, item2 in zip(mylist1, mylist2):\t\tprint(item1, item2)')
for item1, item2 in zip(mylist1, mylist2):      # unpacking the returned iterator of tuples
    print(item1, item2)

print('\n#################### 4. USING zip() TO UNZIP WITH UNPACKING OPERATOR (*) ####################\n')
'''
Say you have a LIST OF TUPLES and want to separate the elements of each tuple into INDEPENDENT SEQUENCES. 
To do this, you can use zip() along with the UNPACKING OPERATOR *, like so:
'''

pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

numbers_tuple, letters_tuple = zip(*pairs)                  # will create 2 independent tuples
numbers_list, letters_list = map(list, zip(*pairs))         # will create 2 independent lists

print("Two independent tuples:")
print(numbers_tuple)
print(letters_tuple)
print()
print("Two independent lists:")
print(numbers_list)
print(letters_list)
