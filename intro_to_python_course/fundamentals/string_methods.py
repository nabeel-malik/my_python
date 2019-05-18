
"""
STRING METHODS
"""

# -------------- .find() method -------------------

'''
The find() method returns the lowest index of the substring if it is found in given string.
If its is not found then it returns -1
'''

print("----------FIND METHOD----------")
work_tip = "good code has meaningful variable names"
print("work_tip:", work_tip, "\n")
location = work_tip.find("o")
# print(location)

while location >= 0:
    print("'o' at index:", location)

    location = work_tip.find("o", location + 1)

print("\nno more o's, -1 returned")

# -------------- .count() method -------------------

'''
The string count() method returns the number of occurrences of a substring in the given string. 
In simple words, count() method searches the substring in the given string and returns how many times 
the substring is present in it.
'''

print("\n----------COUNT METHOD----------")
my_string = "count method returns the number of occurrences of a substring in the given string"
print("Number of times 'o' occurs in the string is:", my_string.count('o'))