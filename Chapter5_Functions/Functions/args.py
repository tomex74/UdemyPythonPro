# using *args to allow undefined number of pos. arguments
# args is a common name for this, but you can name the variable as you like
def f(a, b, *args):
    return args

result = f(10, 20, 'a', True)
print(type(result), result)

# Error!
# def f(a, b, *c, d):
#     return c

# result = f(10, 20, 'a', True, None)
# print(type(result), result)

def f(a, b, c):
    return a, b, c

l = [1, 2, 3]
result = f(*l)
print(type(result), result)
