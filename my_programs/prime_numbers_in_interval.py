lower = int(input("Range START integer: "))
upper = int(input("Range END integer: "))
prime_num_list = []

for num in range (lower,upper+1):
    #Since prime numbers are greater than 1
    if num > 1:
        for i in range (2,num):
            if (num % i == 0):
                break
        else:
            prime_num_list.append(str(num))

prime_numbers = ", ".join(prime_num_list[:])

count = len(prime_num_list)


print("There are {0} prime numbers between {1} and {2}, and they are:".format(count, lower, upper), prime_numbers)


"""
USAGE OF FOR ELSE LOOP:

FOR loops also have an ELSE clause which most of us are unfamiliar with.
The ELSE clause executes when the loop completes 'normally'. This means that the loop did not encounter any BREAK.

for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything.. (Did not encounter a break)
    not_found_in_container()
"""