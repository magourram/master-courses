import threading
import time

def create_threads(f, n): 
    return threading.Thread(target=f, args=[n])

def my_sleep(n): 
    time.sleep(n/100)
    sleepsort.res.append(n)

def sleepsort(input): 
    sleepsort.res = []
    lists_thread = [create_threads(my_sleep, i) for i in input]
    [x.start() for x in lists_thread]
    while any([x.is_alive() for x in lists_thread]): pass
    print(sleepsort.res)
