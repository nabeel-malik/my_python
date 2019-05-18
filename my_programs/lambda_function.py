# This program uses a lambda function to display powers of a number


base_num = input("Please enter base number (base_num): ")
nterms = input("Please enter the number of terms (nterms): ")

try:
    base_num = int(base_num)
except ValueError:
    print ("Invalid entry for base_num. Please enter a positive integer!")
else:
    try:
        nterms = int(nterms)
    except ValueError:
        print("Invalid entry for nterms. Please enter a positive integer!")
    else:
        print ("The base is {0} and the number of terms is {1}".format(base_num, nterms))
        power = lambda base,exponent: base**exponent
        for n in range (0,nterms):
            result = power(base_num,n)
            print("{0} raised to power {1} is {2}".format(base_num, n, result))



"""
Note the usage of LAMBDA (anonymous) function instead of explicitly defining the function with def().

Syntax of LAMBDA function:
lambda arguments: expression

EXAMPLE:
double = lambda x: x * 2

print(double(5))
#Output = 10

This is nearly the same as:
def double(x):
   return x * 2

link: https://www.programiz.com/python-programming/anonymous-function
"""