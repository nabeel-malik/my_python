from random import shuffle, randint

print('\n#################### 1. shuffle() FUNCTION ####################\n')

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('list_numbers:\t\t\t', list_numbers)

shuffle(list_numbers)       # shuffles the sequence IN-PLACE
print('shuffle(list_numbers):\t', list_numbers)

print('\n#################### 1. randint() FUNCTION ####################\n')

print('randint(0,100):\t\t\t', randint(0, 100))      # RETURNS a random integer between the the first two arguments
