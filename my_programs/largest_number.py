user_input = str(input("Enter 3 numbers separated by commas: "))

list = user_input.split(",")
num1 = float(list[0])
num2 = float(list[1])
num3 = float(list[2])

if (num1 > num2) and (num1 > num3):
    print ("{0} is the largest number".format(num1))
elif (num2 > num1) and (num2 > num3):
    print("{0} is the largest number".format(num2))
else:
    print("{0} is the largest number".format(num3))

