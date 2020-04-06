import time
from functools import wraps

import numpy as np

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end-start))
        return r
    return wrapper

# Test code
M = np.random.randint(low=-2, high=2, size=(10, 10))
print(M)
M_inverse = np.linalg.inv(M)
print(M_inverse)


@timethis
def get_matrix_inverse(M):
    return np.linalg.inv(M)

get_matrix_inverse(M)
