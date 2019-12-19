
def factorial(integer):
    result = integer
    for a in range(integer - 1, 0, -1):
        result = result * a
    return result


for x in range(1, 4):
    user_input = input("Enter an integer to calculate the factorial of: ")

    try:
        int(user_input)
    except ValueError:
        if x == 3:
            print("Three (3) invalid user entries. Program aborted.")
            break
        else:
            print("User entry is not an integer.")
    else:
        user_input = int(user_input)
        print("The factorial of {0} is: {1}".format(user_input, factorial(user_input)))
        break

print("Thank you for using the factorial program. Good day!")

"""
USAGE OF TRY, EXCEPT, ELSE BLOCK:

try:
    # execute some code
except:
    # if that code raises an error, go here
    # (this part is just regular code)
else:
    # if the "try" code did not raise an error, go here
    # (this part is also just regular code)
"""

























