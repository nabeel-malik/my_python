import math

'''
USAGE OF math.ceil(x) AND math.floor(x)

Round up, down. Let us consider this program. We use math.ceil to always round up to the nearest integer.
Round() cannot do this—it will round up or down depending on the fractional value.
Ceil: math.ceil(x)
This will always round up. So the ceil of 1.1 is 2. An integer is returned.
Floor: math.floor(y)
This will round down to the nearest integer. The floor of 1.9 is 1. This is a mathematical function.

'''

user_input = input("Enter a string: ")

tot_comparisons = (math.ceil(len(user_input)/2))

for comparison in range (0, tot_comparisons):
    if user_input[0 + comparison] != user_input[-1 - comparison]:
        print("The entered string is NOT a palindrome!")
        break
else:
    print ("The entered string IS a palindrome!")


