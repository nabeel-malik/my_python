print('\n------------------------------------------- FUNCTIONS -------------------------------------------\n')

print("########################### 1. SIMPLE PIG LATIN PROGRAM ###########################\n")

def pig_latin(arg_string):
    if arg_string[0].lower() in 'aeiou':
        return arg_string + 'ay'
    else:
        return arg_string[1:] + arg_string[0] + 'ay'

print(pig_latin('apple'))
print(pig_latin('word'))

print("######################### 2. POSITIONAL ARGUMENTS WITH *args, AKA TUPLE PACKING #########################\n")
'''
A POSITIONAL ARGUMENT is a name that is not followed by an equal sign (=) and default value. 
A KEYWORD ARGUMENT is followed by an equal sign (=) and an expression that gives its default value. 
Broadly speaking, a "positional argument" is any function/method argument/parameter that is 
identified by its position in sequence.
'''


def myfunc(*args):      # *args takes multiple positional arguments into a TUPLE, aka Tuple Packing
    print(args)
    print(sum(args), '\n')    # notice that sum() takes an iterable and returns its sum


myfunc(40,60,100,200)

print("###################### 3. KEYWORD ARGUMENTS WITH **kwargs, AKA DICTIONARY PACKING ######################\n")


def myfunc(**kwargs):      # **kwargs takes multiple keyword arguments into a DICTIONARY, aka Dictionary Packing
    print(kwargs)
    if 'vegetable' in kwargs:
        print('The value for vegetable is {0}'.format(kwargs['vegetable']),'\n')
    else:
        print('Vegetable not found.\n')


myfunc(fruit='apple', vegetable='spinach', drink='juice')    # These are called 'keyword arguments' in a function.

print("################### 4. POSITIONAL AND KEYWORD ARGUMENTS IN COMBINATION ###################\n")


def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {0} {1}'.format(args[1],kwargs['fruit']))


myfunc(1,2,4,vegetable='broccoli',fruit='apples')       # If you put another positional argument at the end >> error.
