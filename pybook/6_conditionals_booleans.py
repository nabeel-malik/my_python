print('\n------------------------------------- CONDITIONALS AND BOOLEANS -------------------------------------')
'''
Python evaluates the following as FALSE:
    - False
    - None
    - Zero of any numeric object (integer or float)
    - Any empty sequence. For example '', () or []
    - Any empty mapping. For example {}
    
Everything else, by default, will evaluate to TRUE.
'''

a = False
b = None
c = 0       #integer
d = []      #empty list
e = {}      #empty dictionary

f = True
g = not None
h = 5
i = ['Jack', 'Richard']
j = {'name': 'Jack', 'age': 28}

print('''
a = False
b = None
c = 0       #integer
d = []      #empty list
e = {}      #empty dictionary

f = True
g = not None
h = 5
i = ['Jack', 'Richard']
j = {'name': 'Jack', 'age': 28}

''')

if a:
    print('a evaluated to True')
else:
    print('a evaluated to False')

if b:
    print('b evaluated to True')
else:
    print('b evaluated to False')

if c:
    print('c evaluated to True')
else:
    print('c evaluated to False')

if d:
    print('d evaluated to True')
else:
    print('d evaluated to False')

if e:
    print('e evaluated to True')
else:
    print('e evaluated to False')

print()

if f:
    print('f evaluated to True')
else:
    print('f evaluated to False')

if g:
    print('g evaluated to True')
else:
    print('g evaluated to False')

if h:
    print('h evaluated to True')
else:
    print('h evaluated to False')

if i:
    print('i evaluated to True')
else:
    print('i evaluated to False')

if j:
    print('j evaluated to True')
else:
    print('j evaluated to False')

print("\n#################### DIFFERENCE BETWEEN '==' AND is COMPARISON ####################\n")
a = [1,2,3]
b = [1,2,3]
c = a

print('''
a = [1,2,3]
b = [1,2,3]
c = a
''')

print('id(a):\t', id(a))
print('id(b):\t', id(b))
print('id(c):\t', id(c))

print('')


print('a == b:\t', a == b)
print('a is b:\t', a is b)

print('a == c:\t', a == c)
print('a is c:\t', a is c)
