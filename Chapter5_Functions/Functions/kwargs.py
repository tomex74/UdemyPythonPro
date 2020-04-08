# specific: positional arguments (the normal function parameters)
# *args: positional arguments (tuple)
# **kwargs: remaining keyword arguments (dict)

def f(a, b, *args, **kwargs):
    return args, kwargs

d = {"kw1": 1, "kw2": 2}
result = f(10, 20, 'a', True, **d)
print(type(result), result)
