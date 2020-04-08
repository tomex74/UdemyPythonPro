# Pythons map function takes:
# 1.) a function (callable)
# 2.) an variable number of iterables (>= 1)

l = [1, 2, 3]

def square(val):
    return val**2

l_squared = list(map(square, l))
print(l_squared)


l1 = [1, 2, 3]
l2 = [-1, -2, -3]

def add(a, b):
    return a + b

l_added = list(map(add, l1, l2))

l_added2 = list(map(lambda a, b: a + b, l1, l2))