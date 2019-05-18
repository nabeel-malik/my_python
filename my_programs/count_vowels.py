# Program to count the number of
# each vowel in a string using
# dictionary and list comprehension

ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.lower()

# Nested list comprehension inside a dictionary comprehension
count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)
print ("a: {0}".format(count['a']))
print ("e: {0}".format(count['e']))
print ("i: {0}".format(count['i']))
print ("o: {0}".format(count['o']))
print ("u: {0}".format(count['u']))


'''
NOTE: IN THIS PROGRAM WE HAVE NESTED A LIST COMPREHENSION INSIDE A DICTIONARY COMPREHENSION (IN LINE 11).
THIS IS A VERY ELEGANT WAY TO CODE.

LIST COMPREHENSIONS: https://www.programiz.com/python-programming/list
DICTIONARY COMPREHENSIONS: https://www.programiz.com/python-programming/dictionary

'''