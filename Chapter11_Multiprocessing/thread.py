import math
import time

from threading import Thread

NUM_THREADS = 4

def calc():
    for i in range(0, 1_000_000):
        math.sqrt(i)

def main():
    threads = []

    start_time = time.perf_counter()

    for _ in range(NUM_THREADS):
        threads.append(Thread(target=calc))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    print("took: {} s".format(end_time - start_time))

if __name__ == "__main__":
    main()
