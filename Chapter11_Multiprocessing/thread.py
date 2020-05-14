import math
import time

from threading import Thread

NUM_THREADS = 2

def calc(upper_bound=7_000_000):
    res = 0

    for i in range(0, upper_bound):
        res += math.sqrt(i)

    print(res)

def main():
    threads = []

    start_time = time.perf_counter()

    for _ in range(NUM_THREADS):
        threads.append(Thread(target=calc, args=[7_000_000]))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    print("took: {} s".format(end_time - start_time))

if __name__ == "__main__":
    main()
