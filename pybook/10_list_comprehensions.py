print('\n------------------------------------------- LIST COMPREHENSIONS -------------------------------------------')

hello_string = 'hello'
print('hello_string:\t\t', hello_string)

mylist1 = [letter for letter in hello_string]
print('''
mylist1 = [letter for letter in hello_string]
print(mylist1)''')
print('>>', mylist1)

mylist2 = [letter for letter in hello_string if letter != 'e']
print('''
mylist2 = [letter for letter in hello_string if letter != 'e']
print(mylist2)''')
print('>>', mylist2)

mylist3 = [num for num in range(0, 11)]
print('''
mylist3 = [num for num in range(0, 11)]
print(mylist3)''')
print('>>', mylist3)

mylist4 = [num for num in mylist3 if num%2 == 0]
print('''
mylist4 = [num for num in mylist3 if num%2 == 0]
print(mylist4)''')
print('>>', mylist4)

mylist5 = [num * 2 for num in mylist3]
print('''
mylist5 = [num * 2 for num in mylist3]
print(mylist5)''')
print('>>', mylist5, '\n')


print("#################### 1. CELCIUS TO FAHRENHEIT CONVERSION WITH LIST COMPREHENSION ####################\n")

celcius = [0, 10, 20, 34.5]
print('celcius:\t\t', celcius, '\n')

fahrenheit = [(((9/5) * temp) + 32) for temp in celcius]
print("fahrenheit = [(((9/5) * temp) + 32) for temp in celcius]\nprint(fahrenheit)")
print('>>', fahrenheit, '\n\n')


print("########################## 2. if else STATEMENT INSIDE LIST COMPREHENSIONS ##########################\n")

# Note:
# When using IF statement inside a list comprehension, it is placed AFTER the for loop, as expected.
# However, when using if else statement inside a list comprehension, it has to be placed BEFORE the for loop.

results = [x if x%2 == 0 else 'ODD' for x in range (0,11)]
print("results = [x if x%2 == 0 else 'ODD' for x in range (0,11)]\nprint(results)")
print('>>', results, '\n')

print("""
TASK - SKYLINE FUNCTION: Create a function called 'skyline' that takes in a string, and returns a matching string where 
every even letter is uppercase, and every odd letter is lowercase.""")

def skyline(str):
    mylist = [str[i].lower() if i%2 == 0 else str[i].upper() for i in range(0, len(str))]
    return "".join(mylist)

print("""
def skyline(str):
    mylist = [str[i].lower() if i%2 == 0 else str[i].upper() for i in range(0, len(str))]
    return "".join(mylist)

print(skyline('randomnanny'))""")

print('>> ', skyline('randomnanny'),'\n\n')

print("################## 3. if else WITH MULTIPLE CONDITIONS INSIDE LIST COMPREHENSIONS ##################\n")

# Note: When using the if else statement with multiple conditions, we do not use elif. See construct below.

print('''
TASK - TIZZFUZZ PROGRAM: Write a program that prints the integers from 1 to 31. But for multiples of 3 print "Tizz" 
instead of the number, and for the multiples of 5 print "Fuzz". For numbers which are multiples 
of both 3 and 5 print "TizzFuzz".''')

tizzfuzz_list = ['TizzFuzz' if num%3 == 0 and num%5 == 0 else 'Tizz' if num%3 == 0 else 'Fuzz' if num%5 == 0
                else num for num in range(1,31)]

print('''
tizzfuzz_list = ['TizzFuzz' if num%3 == 0 and num%5 == 0 else 'Tizz' if num%3 == 0 else 'Fuzz' if num%5 == 0
\t\t\t\telse num for num in range(1,31)]
for item in tizzfuzz_list:
\tprint(item, end=' ')
''')

for item in tizzfuzz_list:
    print(item, end=' ')

print('\n\n')

print("############################ 4. NESTED LOOPS INSIDE LIST COMPREHENSIONS ############################\n")

nested_list = [x*y for x in [2,4,6] for y in [1,10,1000]]
print("nested_list = [x*y for x in [2,4,6] for y in [1,10,1000]]\nprint(nested_list)")
print('>>', nested_list)

