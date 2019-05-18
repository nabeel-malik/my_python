num = 1

def func():
    num = 2         # The integer is being reassigned here. This will NOT change the list in the global scope too.
    print(num)

func()

print(num)

print("--------------------------------------")

mylist = [1,2,3]

def func2(list):
    list[1] = 'X'       # The list is being mutated here. This will change the list in the global scope too.
    print(list)

func2(mylist)

print(mylist)

print("--------------------------------------")

mylist = [1,2,3]

def func2(list):
    list = [4,5,6]      # The list is being reassigned here. This will NOT change the list in the global scope too.
    print(list)

func2(mylist)

print(mylist)




