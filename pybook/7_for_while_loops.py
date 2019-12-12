'''
continue:   Goes to the top of the closest enclosing loop
break:      Breaks out of the current closest enclosing loop
pass:       Does nothing (Usually used as a place holder to avoid getting errors from intermediate code)
'''

print('\n################### 1. for LOOP WITH continue ####################\n')
mystring = 'S-a-m-m-y'

for letter in mystring:
    if letter == '-':
        continue
    print(letter)

print('\n#################### 2. while LOOP WITH break ####################\n')

x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
print('WHILE loop borken!')

print('\n##################### 3. for LOOP WITH pass ######################\n')

food = ['apple', 'milk', 'honey']

for item in food:
    pass        # We have to put something here to avoid SyntaxError. Even a comment would return SyntaxError.

print('End of script!')


