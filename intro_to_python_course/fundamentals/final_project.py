def get_names():

    user_input_list = []

    print("List any 5 of the first 20 elements of the periodic table.")

    while len(user_input_list) < 5:
        user_input = input('Enter the name of an element: ').strip().lower()
        if user_input == "":
            print("Empty string not allowed!")
        elif user_input in user_input_list:
            print(user_input_list,"was already entered. No duplicates allowed.")
        else:
            user_input_list.append(user_input)

    else:
        return user_input_list

# ------------------------------------------------------------------------------------------------------------------ #

element_file = open(r'm4_files\elements1_20.txt', 'r')
element_list = []
element_file_line = element_file.readline()
while element_file_line:
    element_list.append(element_file_line.strip().lower())
    element_file_line = element_file.readline()

element_file.close()

user_score = 0
incorrect_str = "Not Found: "
correct_str = "Found: "

returned_user_list = get_names()

for item in returned_user_list:
    if item in element_list:
        user_score += 20
        correct_str += item + " "
    else:
        incorrect_str += item + " "

print(str(user_score) + "% correct\n" + correct_str + "\n" + incorrect_str)



