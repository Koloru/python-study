# Daemon threads are threads that run in the background
# Not that important for your program to run
# Your program will not wait for them to complete

# non-daemon threads cannot normally be killed and they stay alive until they are complete
# useful for background tasks, garbage collection, waitnig for an input and other long running processes
import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)
# print(x.isDaemon())

answer = input("Do you wish to exit?")
