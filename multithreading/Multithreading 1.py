# A thread is a flow of execution
# Each thread takes its own turn running to achieve concurrency
# They all run concurrently but not trully parallel
# They take turns when one thread is idle

# GIL =  Global interpreter lock
# GIL allows only one thread to hold the control of the python interpreter


# Programs and tasks can be divided between CPU bound or IO bound

# CPU bound is for CPU intensive tasks which
# it is better to use multiprocessing for CPU bound/intensive tasks


# IO bound programs/tasks that are waiting for external events
# better to use multithreading for these tasks

import threading
import time


def eat():
    time.sleep(3)
    print('eating')


def drink():
    time.sleep(4)
    print('drinkign')


def study():
    time.sleep(5)
    print('studying')


eating = threading.Thread(target=eat, args=())
drinking = threading.Thread(target=drink, args=())
studying = threading.Thread(target=study, args=())


eating.start()
drinking.start()
studying.start()

# this is blocking
# waits until studying thread is finished before executing new code

studying.join()
print(threading.active_count())