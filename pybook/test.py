# Comment next 3 lines in, and following 3 lines out, in to see the time efficiency of LISTS
# t1 = time.perf_counter()
# people = people_list(1000000)
# t2 = time.perf_counter()


# Comment next 3 lines in, and previous 3 lines out, in to see the time efficiency of GENERATORS
t1 = time.perf_counter()
people = people_generator(1000000)
t2 = time.perf_counter()

print('Took {} Seconds'.format(t2-t1))