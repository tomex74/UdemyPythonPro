# Note: Memory adresses most likely be different on different systems/runs

# All variables in python are per default a reference to the certain value,
# that is stored in the memory
my_var1 = 10
print(my_var1)
print(hex(id(my_var1)))

my_var2 = 10
print(my_var2)
print(hex(id(my_var2)))

print(hex(id(10)))

# Reference counting: How many variables points to the value in memory
import sys
import ctypes

# Variables to test
l1 = [1, 2, 3]

# sys.getrefcount returns the actual refcount + 1 
# (since the function itself, will be a reference of the value as well)

print("Ref count for l1: {}".format(sys.getrefcount(l1) - 1))
print("Ref count for l1: {}".format(ctypes.c_long.from_address(id(l1))))

l2 = l1

print("Ref count for l1: {}".format(sys.getrefcount(l1) - 1))
print("Ref count for l1: {}".format(ctypes.c_long.from_address(id(l1))))