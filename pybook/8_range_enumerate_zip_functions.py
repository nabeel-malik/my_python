'''
The range() function RETURNS an immutable sequence of numbers between the given start integer and stop integer.

The enumerate() function adds counter to an iterable and RETURNS an enumerate object (in our case a list of tuples).

The zip() function takes iterables (can be zero or more), makes an iterator that aggregates elements
based on the iterables passed, and RETURNS an iterator of tuples.
'''

print('\n#################### 1. range() ####################\n')

for num in range(1,11):
    print(num)

list_from_range = list(range(0,11,2))
print('\n', list_from_range)

print('\n#################### 1. enumerate() ####################\n')

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

print('\n#################### 1. zip() ####################\n')

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



