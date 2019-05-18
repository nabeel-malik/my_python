user_input = input("Enter a number: ")

try:
    user_input = int(user_input)
except ValueError:
    print("Error: The entered number is not an integer!")
else:
    for x in range (1,11):
        product = user_input * x
        print ("{0} x {1} = {2}".format(user_input, x, product))