my_list = ["Tobias", "Colette", "Aaron", "Mark"]
print("Original list:\t\t", my_list)

# .append() method
my_list.append("Carlos")
print("Appended list:\t\t", my_list)

# .insert() method
my_list.insert(2, "Henrick")
print("List after insert:\t", my_list)

# del function to delete specific items
del my_list[-1]
print("List after delete:\t", my_list)

# .pop() method DELETES AND RETURNS an object from a list (default is last item in the list)
popped_item = my_list.pop(3)
print("Popped list:\t\t", my_list, "\t\t\tPopped item:\t", popped_item)

# .remove() method to remove (the first instance of) a specific named item from a list
my_list.remove('Tobias')
print("List after remove:\t", my_list)

# WHILE 'empty list' evaluates as False
while my_list:
    popped_item_while = my_list.pop()
    print("Popped list:\t\t", my_list, "Popped item:\t", popped_item_while)

# .remove() method to remove (the first instance of) a specific named item from a list
my_list = ['Tobias', 'Colette', 'Henrick', 'Aaron', 'Mark', 'Carlos']


# ---------------------------- RANGE FUNCTION --------------------------------
#  range() function accepts an integer and returns a range OBJECT, which is nothing but a sequence of integers.
#  range() is used to create numeric sequences that could be used in iteration.
print("\n---------RANGE FUNCTION-----------")
print(range(0,10))
print(range(10))        #default start is '0'


# ---------------------------- LIST FUNCTION ----------------------------------
#  list() function converts an iterable (tuple, string, set, dictionary, or even a range object) to a list.
print("\n---------LIST FUNCTION-----------")
print(list(range(10)))


# --------------------------- EXTEND METHOD ------------------------------------
#  The .extend() method extends a list by adding all items of another list (passed as an argument) to the end.
print("\n---------EXTEND METHOD-----------")
list1 = ['Item1', 'Item2']
list2 = ['Item3', 'Item4', 'Item5']
print('list1:\t\t\t', list1)
print('list2:\t\t\t', list2)

list1.extend(list2)         #extends the list in-place
print('extended list1:\t', list1)

# --------------------------- REVERSE METHOD ------------------------------------
#  The .reverse() method reverses the list in place.
print("\n---------REVERSE METHOD-----------")
original_list = list(range(10))
print('original list:\t\t', original_list)

original_list.reverse()     #reverses the list in-place
print('reversed list:\t\t', original_list)


# -------------------- SORTED FUNCTION & SORT METHOD -----------------------------
# The SORTED function returns a sorted list
# The .sort() method sorts a list in place

print("\n---------SORTED FUNCTION-----------")
game_points = [10, 13, 9, 18, 11, 5,]
print('initial list:\t\t', game_points)

sorted_points = sorted(game_points)     # returns the sorted list that needs to be stored in another variable

print('sorted list:\t\t', sorted_points)

print("\n-----------SORT METHOD------------")
initial_scores = [10, 13, 9, 18, 11, 5,]
print('initial list:\t\t', initial_scores)

initial_scores.sort()                   # sorts the list in-place

print('sorted list:\t\t', initial_scores)




