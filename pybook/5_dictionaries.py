print('\n--------------------------------------------- DICTIONARIES ---------------------------------------------')
empty_dictionary = {}

'''
A dictionary is a collection which is unordered, mutable and indexed. Dictionaries are mappings, not a sequence.
In Python dictionaries are written with {}, and they have keys and values. 

You can access the items of a dictionary by referring to its key name inside [] or by using the get() method.
You can update the items of a dictionary by referring to its key name inside [] or by using the update() method.

Values in the dictionary can be just about anything. The keys can also be any immutable data type (integer, string etc.)
'''

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print('student:\t\t\t\t\t\t\t\t', student)

print("student['name']:\t\t\t\t\t\t", student['name'])
print("student['age']:\t\t\t\t\t\t\t", student['age'])
print("student['courses']:\t\t\t\t\t\t", student['courses'])

print('\n#################### .get() METHOD ####################\n')

# The get() method returns the value for the specified key if key is in dictionary.

print('student:\t\t\t\t\t\t\t\t', student)

print("student.get('age')\t\t\t\t\t\t", student.get('age'))

# print(student['phone'])   --> will give you a KeyError since the key 'phone' does not exist.
# To avoid getting this error we can use the get() method to return None or a default value [2nd argument to the get()]

print("student.get('phone')\t\t\t\t\t", student.get('phone'))
print("student.get('phone','Not found')\t\t", student.get('phone','Not found'))

print('\n#################### .update() METHOD ####################\n')

# The update() method adds element(s) to the dictionary if the key is not in the dictionary.
# If the key is in the dictionary, it updates the key with the new value.

# The update() method takes either a dictionary as the argument, or an iterable object of
# key/value pairs (generally tuples).

print('student:\t\t\t\t\t\t\t\t', student)

student['cell'] = '555'
print("student['cell'] = '555'\t\t\t\t\t", student)

student.update({'name':'Jane','age':28, 'sex':'female'})    # .update() method with dictionary as argument
print("student.update({'name':'Jane','age':28, 'sex':'female'}):\t\t", student)

student.update(name = 'Charlie', sex = 'male')              # .update() method with an iterable as an argument
print("student.update(name = 'Charlie', sex = 'male'):\t\t\t\t\t", student)


print('\n#################### del FUNCTION AND .pop() METHOD ####################\n')

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print('student:\t\t\t\t\t\t\t\t', student)

del student['age']                  # deletes the element with specified key from the dictionary in-place
print("del student['age']:\t\t\t\t\t\t", student)

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print('\nstudent:\t\t\t\t\t\t\t\t', student)

popped_age = student.pop('age')    # deletes the element with specified key from the dictionary in-place, and returns it
print("student.pop('age')\t\t\t\t\t\t", student, '\t\t\t\t\t\t\tpopped_age:', popped_age)

print('\n#################### len() FUNCTION AND .keys(), .values() AND .items() METHODS ####################\n')

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print('student:\t\t\t\t\t\t\t\t', student)

# len() returns the number of keys in the dictionary
print("len(student):\t\t\t\t\t\t\t", len(student))

# .keys() returns a view object that displays a list of all the keys in the dictionary
print('student.keys():\t\t\t\t\t\t\t', student.keys())

# .values() returns a view object that displays a list of all the values in the dictionary.
print('student.values():\t\t\t\t\t\t', student.values())

# .items() returns a view object that displays a list of dictionary's (key, value) tuple pairs.
print('student.items():\t\t\t\t\t\t', student.items())

print('\n#################### LOOPING THROUGH A DICTIONARY & .items() ATTRIBUTE ####################\n')
# If we loop through a dictionary the same way we loop through lists, i.e. without using the .items() method),
# we will just loop through the keys.

student = {'name': 'John', 'age': 25, 'gender': 'male'}
print('student:\t\t\t\t\t\t\t\t', student)

print('\nfor element in student():     print(element)')
for element in student:        # loops through dictionary keys by default
    print(element)

print('\nfor element in student.keys():     print(element)')
for element in student.keys():        # loops through dictionary keys because of the .keys() attribute
    print(element)

print('\nfor element in student.values():     print(element)')
for element in student.values():        # loops through dictionary values because of the .values() attribute
    print(element)

print('\nfor element in student.items():     print(element)')
for element in student.items():        # loops through dictionary key-value pairs because of the .items() attribute
    print(element)

print('\nfor key, value in student.items():     print(key, value)')
for key, value in student.items():      # See tuple unpacking in xx_tuple_and_dictionary_unpacking.py
    print(key, value)

