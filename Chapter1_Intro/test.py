import numpy as np

my_list = np.array([1, 2, 3], dtype=np.float32)
print(my_list)
my_list = my_list.reshape(-1, 1)
print(my_list)

l1 = [1, 2, 3, 4, 4]
l2 = [5, 6, 7]
print(l1 + l2)