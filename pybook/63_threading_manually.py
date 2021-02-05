import threading
import time

"""
I/O bound tasks:    Tasks that are just waiting for I/O tasks to be completed, for instance reading from a file system,
                    network operations, downloading a file etc. Both, THREADING and MULTIPROCESSING can be useful here.
CPU bound tasks:    Tasks that use a lot of processing power, for instance number crunching, complex calculations etc.
                    MULTIPROCESSING can be useful here, but not THREADING.
"""


def do_something():
    time.sleep(1)


print('\n##################################### 1. SYNCHRONOUS run VS 2 THREADS #####################################\n')

print('Running function 2 times:')

# SYNCHRONOUS RUN
start_syn = time.perf_counter()

# Call function 2 times
do_something()
do_something()

end_syn = time.perf_counter()

print(f'Finished SYNCHRONOUS run in {round(end_syn - start_syn, 2)} second(s).')

# 2 THREADS

start_2thr = time.perf_counter()

# create threads
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

# start threads
t1.start()
t2.start()

# join threads before proceeding to remaining code
t1.join()
t2.join()

end_2thr = time.perf_counter()

print(f'Finished 2 THREADS run in {round(end_2thr - start_2thr, 2)} second(s).')

print('\n#################################### 2. SYNCHRONOUS run VS 10 THREADS ####################################\n')

print('Running function 10 times:')

# SYNCHRONOUS RUN
start_syn = time.perf_counter()

# Call function 10 times
do_something()
do_something()
do_something()
do_something()
do_something()
do_something()
do_something()
do_something()
do_something()
do_something()

end_syn = time.perf_counter()

print(f'Finished SYNCHRONOUS run in {round(end_syn - start_syn, 2)} second(s).')

# 10 THREADS
start_10thr = time.perf_counter()

# create thread list
threads = []

# loop to create 10 threads
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

# loop to join all 10 threads
for thread in threads:
    thread.join()

end_10thr = time.perf_counter()

print(f'Finished 10 THREADS run in {round(end_10thr - start_10thr, 2)} second(s).')


print('\n################################## 3. Threading functions with arguments ##################################\n')


# Function that takes in an argument
def do_something_else(seconds):
    time.sleep(seconds)

print('Running function 10 times:')

# SYNCHRONOUS RUN
start_syn = time.perf_counter()

# Call function 10 times
do_something_else(1.5)
do_something_else(1.5)
do_something_else(1.5)
do_something_else(1.5)
do_something_else(1.5)
do_something_else(1.5)
do_something_else(1.5)
do_something_else(1.5)
do_something_else(1.5)
do_something_else(1.5)

end_syn = time.perf_counter()

print(f'Finished SYNCHRONOUS run in {round(end_syn - start_syn, 2)} second(s).')

# 10 THREADS
start_10thr = time.perf_counter()

# create thread list
threads = []

# loop to create 10 threads
for _ in range(10):
    t = threading.Thread(target=do_something_else, args=[1.5])          # supply argument(s) as a list to 'args='
    t.start()
    threads.append(t)

# loop to join all 10 threads
for thread in threads:
    thread.join()

end_10thr = time.perf_counter()

print(f'Finished 10 THREADS run in {round(end_10thr - start_10thr, 2)} second(s).')

