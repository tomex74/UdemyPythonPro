from timeit import Timer

import numpy as np

import vector

# Timing test
import_string = '''\
import vector
'''  

timer_code = '''\
v = vector.Vector2D(-1, 1)
v *= 2.0
v = v / 2.0
v *= 2.0
v += vector.Vector2D(-4, -4)
'''

timer = Timer(timer_code, 
              setup=import_string)

print('Vector code')
num_runs = 1_000_000
print("Mean time: ", np.mean(timer.repeat(repeat=3, number=num_runs)) / num_runs)