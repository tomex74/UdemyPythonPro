# The python int object uses a variable number of bits
# In contrast to other common programming langueges like c/c++/java etc.
# There a integer type has a fixed number of bits (e.g. 8/16/32 or 64 bit)
import sys

my_value = 42
print(type(my_value))

# Sizeof in Bytes(!)
print(sys.getsizeof(0))
print(sys.getsizeof(1))
print(sys.getsizeof(2**5))
print(sys.getsizeof(2**10))
print(sys.getsizeof(2**15))
print(sys.getsizeof(2**25))
print(sys.getsizeof(2**50))
print(sys.getsizeof(2**75))
print(sys.getsizeof(2**100))

# Arithmetic operations
# The division of int / int returns always a float!
# For the other operations (int, int) will return an int
result = 10 / 5
print(result, type(result))

result = 10 // 5
print(result, type(result))
result = 10 % 5
print(result, type(result))

result = 10 + 5
print(result, type(result))
result = 10 - 5
print(result, type(result))
result = 10 * 5
print(result, type(result))

# Floor vs. float-to-int-cast
import math

val = 2.5
print(int(val))
print(math.floor(val))

val = -2.5
print(int(val))
print(math.floor(val))
