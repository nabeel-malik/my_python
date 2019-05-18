print('\n--------------------------------------------- LISTS ---------------------------------------------')
empty_list = []

print('\n#################### COMMONLY USED LIST METHODS ####################\n')

courses = ['History', 'Math', 'Physics', 'CompSci', 'Literature']
print('courses:\t\t\t\t\t\t\t', courses)

courses.append('Geology')
print("courses.append('Geology')\t\t\t", courses)

courses.insert(0, 'Biology')
print("courses.insert(0, 'Biology')\t\t", courses)

courses.remove('Math')
print("courses.remove('Math')\t\t\t\t", courses)

first_pop_item = courses.pop()      #deletes the last item (default) of the list in-place, and returns the popped value.
print("courses.pop()\t\t\t\t\t\t", courses, '\t\t\t\tfirst_pop_item:', first_pop_item)

second_pop_item = courses.pop(1)    #deletes the item with specified index of the list in-place, and returns it.
print("courses.pop(1)\t\t\t\t\t\t", courses, '\t\t\t\t\t\t\tsecond_pop_item:', second_pop_item)

print('\ncourses:\t\t\t\t\t\t\t', courses)

courses_2 = ['Art', 'Education']
print('courses_2:\t\t\t\t\t\t\t', courses_2)

courses.extend(courses_2)           # Extends the object list with the argument list
print('courses.extend(courses_2):\t\t\t', courses)

courses.reverse()                   # Reverses indexes in-place
print('\ncourses.reverse():\t\t\t\t\t', courses)

courses.sort()                      # List of strings is sorted in alphabetical order in-place
print('courses.sort():\t\t\t\t\t\t', courses)

courses.sort(reverse = True)        # List of strings is sorted in reverse alphabetical order in-place
print('courses.sort(reverse = True):\t\t', courses)

print('courses:\t\t\t\t\t\t\t', courses)

sorted_list = sorted(courses)       # Returns a sorted version of the list without altering the original list.
print('sorted_list:\t\t\t\t\t\t', sorted_list, '\t\twhere sorted_list = sorted(courses)')

print('\ncourses:\t\t\t\t\t\t\t', courses)

print("courses.index('CompSci')\t\t\t", courses.index('CompSci'))  # Returns index of the item in argument.
print("'Physics' in courses\t\t\t\t", 'Physics' in courses)
print("'Math' in courses\t\t\t\t\t", 'Math' in courses)

print('\n#################### LISTS WITH ENUMERATE FUNCTION ####################\n')

print('\ncourses:\t\t\t\t\t\t\t', courses)

print('\nfor item, course in enumerate(courses):    print(item, course)')
for item, course in enumerate(courses):     # enumerate() function returns a tuple with the index (default) and value
    print(item, course)

print('\nfor item, course in enumerate(courses, start=1):    print(item, course)')
for item, course in enumerate(courses, start=1):
    print(item, course)

print('\n#################### STRING METHOD .join() TO CONVERT LIST TO STRING ####################\n')

print('\ncourses:\t\t\t\t\t\t\t', courses)

courses_str = ', '.join(courses)        # Returns a string of the list items join by commas
print("courses_str:\t\t\t\t\t\t", courses_str, "\t\t\t\t\t\twhere courses_str = ', '.join(courses)")

courses_str_2 = ' - '.join(courses)     # Returns a string of the list items join by hyphens
print("courses_str_2:\t\t\t\t\t\t", courses_str_2, "\t\t\t\twhere courses_str_2 = ' - '.join(courses)")

print('\n#################### STRING METHOD .split() TO CONVERT STRING TO LIST ####################\n')

new_list = courses_str.split(', ')          # Returns a list split from the string at ', '
print("new_list:\t\t\t\t\t\t\t", new_list, "\t\twhere new_list = courses_str.split(', ')")

new_list_2 = courses_str_2.split(' - ')     # Returns a list split from the string at ' - '
print("new_list_2:\t\t\t\t\t\t\t", new_list_2, "\t\twhere new_list_2 = courses_str.split(' - ')")


print('\n#################### FUNCTIONS FOR INTEGER LISTS ####################\n')

nums = [5, 3, 2, 8, 7]
print('nums:\t\t\t\t\t\t\t\t', nums)
print('min(nums):\t\t\t\t\t\t\t', min(nums))
print('max(nums):\t\t\t\t\t\t\t', max(nums))
print('sum(nums):\t\t\t\t\t\t\t', sum(nums))

print('\n--------------------------------------------- TUPLES ---------------------------------------------')

# Tuples () behave very similar to lists (loop through items, access values etc.) except that tuples are immutable.
# Tuples have just 2 methods: .count() and .index()
empty_tuple = ()

tuple_1 = ('History', 'Math', 'Physics', 'CompSci', 'Literature')   # Note that we use () for tuples instead of []
print('tuple_1:\t\t\t\t\t\t\t', tuple_1)

#tuple_1[0] = 'Art'      --> If commented in --> exit code 1, because tuple object does not support item assignment.

print('\n########################### TUPLE UNPACKING ###########################\n')
# Tuple unpacking is a feature that assigns ('unpacks') the items of a tuple on the right hand side to the items
# of a variable with the same structure on the left hand side.

list_tuple = [(1,2), (3,4), (5,6)]
print('list_tuple:\t\t\t\t\t\t\t', list_tuple)

print('for a,b in list_tuple:\tprint(b)')
for a,b in list_tuple:
    print(b)

print('\n--------------------------------------------- SETS ---------------------------------------------')

# Sets {} are values that are unordered and have no duplicates
empty_set = set()           # {} is used to create empty dictionary.
# The set() constructor constructs a Python set from the given iterable AND returns it.
my_set = set('Parallel')        # set() takes just 1 iterable as an optional argument
print("my_set = set('Parallel'):\t", my_set)

set_1 = {'History', 'Math', 'Physics', 'CompSci'}   # Note that we use {} for tuples instead of []
print('set_1:\t\t\t\t\t\t', set_1)          # Duplicate values will be removed from the set

set_1.add('Chemistry')        # Adds an element to the set IF it is not already present in it.
print("set_1.add('Chemistry'):\t\t", set_1)

print("'Physics' in set_1\t\t\t", 'Physics' in set_1)    # Sets are optimised for this functionality

set_2 = {'Art', 'Math', 'Physics', 'Design', 'CompSci'}
print('\nset_1:\t\t\t\t\t\t', set_1)
print('set_2:\t\t\t\t\t\t', set_2)

print("set_1.intersection(set_2)\t", set_1.intersection(set_2))     # returns intersection
print("set_1.difference(set_2)\t\t", set_1.difference(set_2))       # returns difference
print("set_1.union(set_2)\t\t\t", set_1.union(set_2))               # returns union



