user_input = input("Enter a sentence: ")

user_input_list = user_input.split(' ')

#You can use the following for CASE-SENSITIVE sorting, where upper-case is sorted above lower-case (if rest is same)
#user_input_list.sort()

#We will use the following for CASE-INSENSITIVE sorting, where no case has sorting preference
user_input_list = sorted(user_input_list, key=str.lower)

print ("The sorted list of words now follows: ")

for word in user_input_list:
    print (word)

#The sort() function is older, and sorted() is recommended to use in all cases.

'''

TO READ MORE ABOUT PYTHON SORTING:
https://developers.google.com/edu/python/sorting

'''

