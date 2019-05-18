#This program removes punctuations from a user input string

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
print ("This program will remove the following punctuation from your input string: {0}".format(punctuation))

punc_list = list(punctuation)

user_input = input("Enter a string: ")
user_list = list(user_input)

#list_comprehension used below to create new list
output_list = [i for i in user_list if not i in punc_list]
output_str = ''.join(output_list)

print (output_str)

'''
NOTE: The use of list() method. list() is used to convert an iterable (tuple, string, set, dictionary) to a list.
NOTE: Usage of list comprehension.

'''