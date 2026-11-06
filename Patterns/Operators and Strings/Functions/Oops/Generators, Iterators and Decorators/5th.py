#5.​ Create a decorator to measure and print the execution time of functions.
import time
def exe_time(func):
    def wrapper():
        starttime = time.time()
        func()
        endtime = time.time()
        tasktime = endtime - starttime
        print("execution time of functions: ",tasktime)

    return wrapper()

@exe_time
def pavan():

 print("pavan")
 time.sleep(2)