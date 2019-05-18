#  Function called to .pop(), .append() or .remove()
def list_o_matic(animal_list, animal_str):
    if animal_str == "":
        print(animal_list.pop(), "popped from the list\n")
        return animal_list
    elif animal_str in animal_list:
        animal_list.remove(animal_str)
        print("1 instance of", animal_str, "removed from the list\n")
        return animal_list
    else:
        animal_list.append(animal_str)
        print("1 instance of", animal_str, "appended to the list\n")
        return animal_list

# List initialization
animals = ['goat', 'horse', 'cat', 'snake', 'cat']

# Looping for user input until user types 'quit'
while animals:
    print('Look at all the animals:\t', animals)
    user_input = input("Enter the name of an animal: ").lower()
    if user_input == "quit":
        break
    else:
        animals = list_o_matic(animals, user_input)

# ELSE for WHILE, to deal with the case when WHILE CONDITION is FALSE.
else:
    print("The list is now empty")



