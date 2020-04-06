from timeit import Timer

import numpy as np

import fast_math

# Test code
a = np.random.uniform(-2, 2, size=3)
print(a)
fast_math.pure_python_clip(a, -1, 1, a)
print(a)

a = np.random.uniform(-2, 2, size=3)
print(a)
fast_math.numpy_clip(a, -1, 1, a)
print(a)

a = np.random.uniform(-2, 2, size=3)
print(a)
fast_math.cython_clip(a, -1, 1, a)
print(a)

a = np.random.uniform(-2, 2, size=100)

# Timin_valueg test
import_string = \
'''from __main__ import a
import fast_math'''  

python_timer = Timer(
    'fast_math.pure_python_clip(a, -1, 1, a)', 
    setup=import_string)

numpy_timer = Timer(
    'fast_math.numpy_clip(a, -1, 1, a)', 
    setup=import_string)

cython_timer = Timer(
    'fast_math.cython_clip(a, -1, 1, a)', 
    setup=import_string)

print('fast_math.pure_python_clip')
print(np.mean(python_timer.repeat(repeat=3, number=100_000)))
print('fast_math.numpy_clip')
print(np.mean(numpy_timer.repeat(repeat=3, number=100_000)))
print('fast_math.cython_clip')
print(np.mean(cython_timer.repeat(repeat=3, number=100_000)))
