import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        args_list = list(args) + [val for _, val in kwargs.items()]
        print('Duration: {:.8f}s, for function: {}({}) = {}'.format(elapsed, name, args_list, result))
        return result
    return clocked

def f(a, *args, **kwargs):
    return a**2

if __name__ == "__main__":
    f_decorated = clock(f)
    f_decorated(2, 3, 4)