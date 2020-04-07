# Immutable types: int, float, bool, str, tuple, user-defined classes (may be), etc.
# Mutable types: lists, dicts, sets, etc.

a = [1, 2]
b = [3, 4]
t = (a, b)
print(t)

a.append(3)
b.append(5)
print(t)

# Since the values of t are mutable lists, the lists itself can be changed
# Nevertheless the following line gives an error, since there a direct 
# tuple value would be changed
try:
    t[0] = b # Error!
except Exception as e:
    print('not valid cod: {!r}'.format(e))