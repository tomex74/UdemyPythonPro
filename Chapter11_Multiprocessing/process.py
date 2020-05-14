import math
import time

from multiprocessing import Process

NUM_PROCESSES = 4

def calc():
    for i in range(0, 1_000_000):
        math.sqrt(i)

def main():
    processes = []

    start_time = time.perf_counter()

    for _ in range(NUM_PROCESSES):
        processes.append(Process(target=calc))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end_time = time.perf_counter()
    print("took: {} s".format(end_time - start_time))

if __name__ == "__main__":
    main()
