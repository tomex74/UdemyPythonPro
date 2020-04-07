# Floats in a computer represents rational numbers
# BUT: The computer has only a subset of the infinite set of rational numbers, since
# the computer has only a fixed size
# Floats are implemented as doubles (fixed as 64bits, in contrast to variable sized integers)

# sign: 1bit
# exponent: 11bits [-1022, 1023]
# significant digits: 52bits

val = float(42.1)
print(type(val), val)

val = float("42.1")
print(type(val), val)

# val = float("10/2") # Error!
# print(type(val), val)

# Some numbers cannot be represented using a finite number of bits
val = 1 / 10
print('{:.32f}'.format(val))
val = 1 / 3
print('{:.32f}'.format(val))

# Expected to be 0.3
val2 = 0.1 + 0.1 + 0.1
print('{:.32}'.format(val2))
print(val2 == 0.3)
