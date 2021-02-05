import concurrent.futures
import time


def sleep_func(seconds):
    print(f'Sleeping {seconds} second(s)...')                   # print
    time.sleep(seconds)
    return f'Finished sleeping for {seconds} second(s).'        # return


print("\n##################### 1. concurrent.futures.ThreadPoolExecutor() and 'Future' object' #####################\n")

start = time.perf_counter()

# It is normal to use context managers with ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:           # creates a 'ThreadPoolExecutor' object

    """
    The ThreadPoolExecutor.submit() method schedules a function to be executed, and returns a 'Future' object.
    
    The 'Future' object encapsulates the execution of our function, and allows us to check in on it after it has been 
    scheduled. 
        - So we can check whether it is running or completed, and also check the result. 
        - If we grab the result, then it will give us the return value of the function. 
    """

    # 1.1 RUNNING sleep_func() 1 TIME
    print('********** Running function 1 time: **********')
    start = time.perf_counter()

    f1 = executor.submit(sleep_func, 1)                             # .submit() returns a 'Future' object
    print(f1.result())              # .result() will wait till the function completes, and then print the return value

    end = time.perf_counter()
    print(f'Finished run in {round(end - start, 2)} second(s).')

    # 1.2 RUNNING sleep_func() 2 TIMES
    print('\n********** Running function 2 times: **********')
    start = time.perf_counter()

    f1 = executor.submit(sleep_func, 1)  # .submit() returns a 'Future' object
    f2 = executor.submit(sleep_func, 1)
    print(f1.result())  # .result() will wait till the function completes, and then print the return value
    print(f2.result())

    end = time.perf_counter()
    print(f'Finished run in {round(end - start, 2)} second(s).')

    # 1.3 RUNNING sleep_func() 10 TIMES WITH AN ARGUMENT OF 1 SECOND
    print('\n********** Running function 10 times with argument of 1 second: **********')
    start = time.perf_counter()

    futures = [executor.submit(sleep_func, 1) for _ in range(10)]

    """
    In order to get the results from the 'Future' objects above, we can use another method from concurrent.futures
    called .as_completed(). This will give us an iterator that we can loop over to yield the results of our threads 
    as they are completed.
    """
    for f in concurrent.futures.as_completed(futures):
        print(f.result())

    end = time.perf_counter()
    print(f'Finished run in {round(end - start, 2)} second(s).')

    """
    Now, to prove that the results are coming in as they are completed, we can use an array of arguments, with varying
    number of seconds.
    """

    # RUNNING sleep_func() 5 TIMES WITH A 5-ARRAY ARGUMENT, AND .submit() [TO RUN] and .as_completed() [FOR RESULTS]
    print("\n********** Running function 5 times with a 5-array argument, and submit() and .as_completed() **********")
    start = time.perf_counter()

    secs = [5, 4, 3, 2, 1]

    futures = [executor.submit(sleep_func, sec) for sec in secs]        # Now we are running .submit() 5 times

    for f in concurrent.futures.as_completed(futures):
        print(f.result())

    end = time.perf_counter()
    print(f'Finished run in {round(end - start, 2)} second(s).')

    """
    You can see from the last results that, we started [with .submit()] the 5 seconds thread first, but since we used
    the .as_completed() method, it gave the results in the order that the threads were completed (i.e. shorter first).
    """

    """
    Now, each .submit() runs the function once. In order to run .submit() on an entire list, we can:
    1. Use a FOR loop, or a LIST COMPREHENSION (like we have used in the last case above), or
    2. Use the .map() method: even with threads we can use the .map() method to run our function over a list of values.
    """

    # RUNNING sleep_func() 5 TIMES WITH A 5-ARRAY ARGUMENT, AND .map() FOR BOTH, THE FUNCTION RUNS AND RESULTS
    print("\n********** Running function 5 times with a 5-array argument, and .map() **********")
    start = time.perf_counter()

    secs = [5, 4, 3, 2, 1]

    '''
    Two key differences between .map() and the combination of .submit() + .as_completed() are:
    1. .map() returns results ('generator' object) instead of the 'Future' object returned by .submit()
    2. .map() will still run concurrently, but instead of returning results as the functions complete, as we saw 
        with .as_completed() earlier, .map() returns results in the order in which the functions were called.
    
    '''
    results = executor.map(sleep_func, secs)                # 'generator' object created and returned

    for result in results:
        print(result)

    end = time.perf_counter()
    print(f'Finished run in {round(end - start, 2)} second(s).')

    """
    You can see from the last results that, all of our thread started at the same time, and then it "looks" like they 
    ended at the same time, but in reality they did NOT actually complete at the same time. As mentioned above, when 
    using .map(), then it returns the results in the order that the threads were started. 
    
    Now, another thing to point out here is that if our function raises an exception, then it would not actually raise 
    the exception while running the threads. The exception will be raised when its value is retrieved from the 
    results generator. So, if you need to handle exceptions, then you can do that within the generator.
    
    Another thing to note is that even if we do not grab all of our results within the context manager above, 
    it is still going to automatically join all of the threads, and let them finish after the context manager ends.
    So if we comment out where we are print the results, and run it, then we will see that the program still waits
    until the threads have finished running and then move ahead to the code after the context manager.
    """















