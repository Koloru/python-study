# multiprocessing
# running tasks in parallel in different cpu cores

import time
from multiprocessing import Process, cpu_count


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    start = time.perf_counter()
    print(cpu_count())
    # add a comma on args to make it a parameter instead of an expression
    a = Process(target=counter, args=(10000000,))
    b = Process(target=counter, args=(10000000,))
    c = Process(target=counter, args=(10000000,))
    d = Process(target=counter, args=(10000000,))
    a.start()
    c.start()
    d.start()
    b.start()
    a.join()
    c.join()
    d.join()
    b.join()
    end = time.perf_counter()
    print('Finished in: ', end - start, "seconds")


if __name__ == '__main__':
    main()
