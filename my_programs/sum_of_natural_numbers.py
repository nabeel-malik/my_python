user_input = input("Please enter a positive integer: ")
try:
    user_input = int(user_input)
except ValueError:
    print ("Invalid entry. Please enter a POSITIVE INTEGER!")
else:
    sum = 0
    for x in range(1,user_input+1):
        sum += x
    print("The sum of natural numbers till the {0}th term is: {1}".format(user_input,sum))

