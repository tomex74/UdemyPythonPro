from timeit import Timer

import numpy as np

import fast_vector

# Test code
a = np.random.randint(-2, 2, size=3)
print(a)
fast_vector.pure_python_clip(a, -1, 1, a)
print(a)

a = np.random.randint(-2, 2, size=3)
print(a)
fast_vector.numpy_clip(a, -1, 1, a)
print(a)

a = np.random.randint(-2, 2, size=3)
print(a)
fast_vector.cython_clip(a, -1, 1, a)
print(a)

a = np.random.randint(-2, 2, size=3)
print(a)
fast_vector.c_api_clip(list(a), -1, 1, list(a))
print(a)

a = np.random.randint(-2, 2, size=100)

# Timing test
import_string = \
'''from __main__ import a
import fast_vector'''  

python_timer = Timer(
    'fast_vector.pure_python_clip(a, -1, 1, a)', 
    setup=import_string)

numpy_timer = Timer(
    'fast_vector.numpy_clip(a, -1, 1, a)', 
    setup=import_string)

cython_timer = Timer(
    'fast_vector.cython_clip(a, -1, 1, a)', 
    setup=import_string)

c_api_timer = Timer(
    'fast_vector.c_api_clip(list(a), -1, 1, list(a))', 
    setup=import_string)

num_runs = 100_000
print('fast_vector.pure_python_clip')
print(np.mean(python_timer.repeat(repeat=3, number=num_runs)) / num_runs)
print('fast_vector.numpy_clip')
print(np.mean(numpy_timer.repeat(repeat=3, number=num_runs)) / num_runs)
print('fast_vector.cython_clip')
print(np.mean(cython_timer.repeat(repeat=3, number=num_runs)) / num_runs)
print('fast_vector.c_api_clip')
print(np.mean(c_api_timer.repeat(repeat=3, number=num_runs)) / num_runs)
