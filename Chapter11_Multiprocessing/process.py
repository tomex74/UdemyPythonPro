import math
import time

from multiprocessing import Process

NUM_PROCESSES = 4

def calc(upper_bound=8_000_000):
    res = 0

    for i in range(0, upper_bound):
        res += math.sqrt(i)

    print(res)

def main():
    processes = []

    start_time = time.perf_counter()

    for _ in range(NUM_PROCESSES):
        processes.append(Process(target=calc, args=[8_000_000]))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end_time = time.perf_counter()
    print("took: {} s".format(end_time - start_time))

if __name__ == "__main__":
    main()
