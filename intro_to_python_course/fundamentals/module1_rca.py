user_input = input("Enter a string: ").lower()
word = ""

if user_input[-1] != " ":
    user_input = user_input + " "

for letter in user_input:
    if letter.isalpha():
        word += letter
    elif word != "" and word[0] >= "h":
        print(word.upper())
        word = ""
    else:
        word = ""
