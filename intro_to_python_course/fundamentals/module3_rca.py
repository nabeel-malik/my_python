def word_mixer(arg_list):
    arg_list.sort()
    new_words = []
    while len(arg_list) > 5:
        new_words.append(arg_list.pop(-5))
        new_words.append(arg_list.pop(0))
        new_words.append(arg_list.pop() + "\n")
    new_str = " ".join(new_words)
    return new_str


user_str = input("Enter string: ")

user_list = user_str.split(" ")

user_list_len = len(user_list)

for index in range(0,user_list_len):
    if len(user_list[index]) <= 3:
        user_list[index] = user_list[index].lower()
    elif len(user_list[index]) >= 7:
        user_list[index] = user_list[index].upper()
    else:
        pass

print(word_mixer(user_list))





