"""Test code.
"""
import cProfile
import pstats
import io
import random
from functools import wraps

def profile(fn):
    @wraps(fn)
    def profiler(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        fn_result = fn(*args, **kwargs)
        profiler.disable()
        stream = io.StringIO()
        ps = pstats.Stats(profiler, stream=stream).sort_stats('cumulative')
        ps.print_stats()
        print(stream.getvalue())
        return fn_result
    return profiler

def count_number_of_occurences(num, numbers_list):
    num_occurences = 0
    for curr_num in numbers_list:
        if num == curr_num:
            num_occurences += 1
    return num_occurences

@profile
def main():
    nums = [random.randint(-100, 100) for i in range(10_000)]
    for num in nums:
        count_number_of_occurences(num, nums)

if __name__ == "__main__":
    main()
