import multiprocessing
import time


"""
Unlike THREADING, which is only useful in I/O bound tasks, MULTIPROCESSING can be useful in both, I/O bound tasks and
CPU bound tasks. 
"""


def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done sleeping.')


t1 = time.perf_counter()

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

# start threads
p1.start()
p2.start()

# join threads before proceeding to remaining code
p1.join()
p2.join()

t2 = time.perf_counter()

print(f'Finished in {t2-t1} second(s).')

