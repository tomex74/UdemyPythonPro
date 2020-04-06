from timeit import Timer

import numpy as np

# Test code
M = np.random.randint(low=-2, high=2, size=(10, 10))
print(M)
M_inverse = np.linalg.inv(M)
print(M_inverse)

# Timing test
import_string = \
'''import numpy as np
from __main__ import M'''  

timer = Timer(
    'np.linalg.inv(M)', 
    setup=import_string)

print('Matrix inverse')
num_runs = 100_000
print("Mean time: ", np.mean(timer.repeat(repeat=3, number=num_runs)) / num_runs)