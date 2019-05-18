term_1 = input("Enter term 1 (term_1): ")
term_2 = input("Enter term 2 (term_2): ")
nterms = input("Enter the number of terms you need for the fibonacci sequence (nterms): ")

try:
    nterms = int(nterms)
except ValueError:
    print("Error: Invalid 'nterms' entry. 'nterms' should be an integer!")
else:
    try:
        term1 = int(term_1)
    except ValueError:
        print("Error: Invalid term_1 entry. term_1 should be an integer!")
    else:
        try:
            term_2 = int(term_2)
        except ValueError:
            print("Error: Invalid term_2 entry. term_2 should be an integer!")
        else:
            fib_list = []
            for x in range(1, nterms+1):
                if x == 1:
                    fib_list.append(term1)
                elif x == 2:
                    fib_list.append(term_2)
                else:
                    fib_list.append(fib_list[x-3]+fib_list[x-2])

            # To convert all the int items on the list to str
            fib_list_str = [str(i) for i in fib_list]
            fib_string = ", ".join(fib_list_str[:])
            print ("The resultant fibonacci sequence is", fib_string)


"""
Note the usage of nested TRY, EXCEPT, ELSE blocks in this code to check ValueError for multiple user entries

A good explanation of TRY, EXCEPT, ELSE, FINALLY: https://docs.python.org/2.5/whatsnew/pep-341.html
"""