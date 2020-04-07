val = int(123)
print(val, type(val))

# From any base in the range [2, 36] to the decimal base (which is 10)
val = int("123")
print(val, type(val))

val = int("123", base=16)
print(val, type(val))

val = int("1111", base=2)
print(val, type(val))

# Special cases
val = int("0b1111", base=0)
print(val, type(val))

val = 0b1010
print(val, type(val))

# From Decimal base to another base
# Only implemented for these 3 bases per default in python
print(bin(val), type(bin(val)))
print(oct(val), type(oct(val)))
print(hex(val), type(hex(val)))