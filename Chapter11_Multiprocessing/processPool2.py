import math
import time

import concurrent.futures

NUM_PROCESSES = 4

def calc(upper_bound=7_000_000):
    res = 0

    for i in range(0, upper_bound):
        res += math.sqrt(i)

    return res
    

def main():
    start_time = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        args = [7_000_000 for _ in range(NUM_PROCESSES)]
        results = list(executor.map(calc, args))
        print(results)

    end_time = time.perf_counter()
    print("took: {} s".format(end_time - start_time))

if __name__ == "__main__":
    main()
