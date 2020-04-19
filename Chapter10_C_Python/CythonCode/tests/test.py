from timeit import Timer

import numpy as np

import fastvector

# Test code
a = np.random.randint(-2, 2, size=3)
print(a)
fastvector.pure_python_clip(a, -1, 1, a)
print(a)

a = np.random.randint(-2, 2, size=3)
print(a)
fastvector.numpy_clip(a, -1, 1, a)
print(a)

a = np.random.randint(-2, 2, size=3)
print(a)
fastvector.cython_clip(a, -1, 1, a)
print(a)

a = np.random.randint(-2, 2, size=100)

# Timing test
import_string = \
'''from __main__ import a
import fastvector'''  

python_timer = Timer(
    'fastvector.pure_python_clip(a, -1, 1, a)', 
    setup=import_string)

numpy_timer = Timer(
    'fastvector.numpy_clip(a, -1, 1, a)', 
    setup=import_string)

cython_timer = Timer(
    'fastvector.cython_clip(a, -1, 1, a)', 
    setup=import_string)

num_runs = 100_000
print('fastvector.pure_python_clip')
print(np.mean(python_timer.repeat(repeat=3, number=num_runs)) / 100_000)
print('fastvector.numpy_clip')
print(np.mean(numpy_timer.repeat(repeat=3, number=num_runs)) / 100_000)
print('fastvector.cython_clip')
print(np.mean(cython_timer.repeat(repeat=3, number=100_000)) / 100_000)
