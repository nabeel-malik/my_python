
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide (a,b):
    return a/b

print ("Select operation.")
print ("1.Add")
print ("2.Subtract")
print ("3.Multiply")
print ("4.Divide")

user_choice = input("Enter choice (1/2/3/4): ")

try:
    user_choice = int(user_choice)
except ValueError:
    print ("Invalid entry. Please enter a valid choice (1/2/3/4)")
else:
    if not ((user_choice == 1) or (user_choice == 2) or (user_choice == 3) or (user_choice ==4)):
        print ("Invalid entry. Please enter a valid choice (1/2/3/4)")
    else:

#ADDITION
        if (user_choice == 1):
            print("You have selected ADDITION.")
            num1 = input("Please enter the FIRST number: ")
            num2 = input("Please enter the SECOND number: ")

            try:
                num1 = int(num1)
            except ValueError:
                try:
                    num1 = float(num1)
                except ValueError:
                    print ("Invalid entry.")
            else:
                try:
                    num2 = int(num2)
                except ValueError:
                    try:
                        num2 = float(num2)
                    except ValueError:
                        print("Invalid entry.")
            finally:
                    sum = add(num1, num2)
                    print("{0} + {1} = {2}".format(num1, num2, sum))

#SUBTRACTION
        elif (user_choice == 2):
            print("You have selected SUBTRACTION.")
            num1 = input("Please enter the FIRST number: ")
            num2 = input("Please enter the SECOND number: ")

            try:
                num1 = int(num1)
            except ValueError:
                try:
                    num1 = float(num1)
                except ValueError:
                    print ("Invalid entry.")
            else:
                try:
                    num2 = int(num2)
                except ValueError:
                    try:
                        num2 = float(num2)
                    except ValueError:
                        print("Invalid entry.")
            finally:
                    difference = subtract(num1, num2)
                    print("{0} - {1} = {2}".format(num1, num2, difference))

#MULTIPLICATION
        elif (user_choice == 3):
            print("You have selected MULTIPLICATION.")
            num1 = input("Please enter the FIRST number: ")
            num2 = input("Please enter the SECOND number: ")

            try:
                num1 = int(num1)
            except ValueError:
                try:
                    num1 = float(num1)
                except ValueError:
                    print ("Invalid entry.")
            else:
                try:
                    num2 = int(num2)
                except ValueError:
                    try:
                        num2 = float(num2)
                    except ValueError:
                        print("Invalid entry.")
            finally:
                    product = multiply(num1, num2)
                    print("{0} x {1} = {2}".format(num1, num2, product))

#DIVISION
        elif (user_choice == 4):
            print("You have selected DIVISION.")
            num1 = input("Please enter the FIRST number: ")
            num2 = input("Please enter the SECOND number: ")

            try:
                num1 = int(num1)
            except ValueError:
                try:
                    num1 = float(num1)
                except ValueError:
                    print ("Invalid entry.")
            else:
                try:
                    num2 = int(num2)
                except ValueError:
                    try:
                        num2 = float(num2)
                    except ValueError:
                        print("Invalid entry.")
            finally:
                    quotient = divide(num1, num2)
                    print("{0} / {1} = {2}".format(num1, num2, quotient))

