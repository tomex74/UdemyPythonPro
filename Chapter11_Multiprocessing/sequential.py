import math
import time

NUM_THREADS = 4

def calc(upper_bound=7_000_000):
    res = 0

    for i in range(0, upper_bound):
        res += math.sqrt(i)

    print(res)

def main():
    start_time = time.perf_counter()

    for _ in range(NUM_THREADS):
        calc(7_000_000)

    end_time = time.perf_counter()
    print("took: {} s".format(end_time - start_time))

if __name__ == "__main__":
    main()
