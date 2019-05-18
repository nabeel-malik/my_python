#This program uses lambda function with filter() to find even numbers in a list
user_input = input('Enter the positive integers separated by commas(","): ')
user_input_list = user_input.split(",")

try:
    user_input_list = [int(i) for i in user_input_list]
except ValueError:
    print("Invalid entry. Please ensure that all the entries are positive integers")
else:
    even_list = list(filter(lambda x: (x%2 == 0), user_input_list))

    # we need to convert all items in the list to string to be able to join them
    even_list =[str(i) for i in even_list]
    even_numbers_str = ", ".join(even_list[:])

    count = len(even_list)

    print ("There are {0} even numbers in your entry. They are: {1}".format(count,even_numbers_str))



"""
Note the usage of lambda function with filter()

Link: https://www.programiz.com/python-programming/anonymous-function
"""