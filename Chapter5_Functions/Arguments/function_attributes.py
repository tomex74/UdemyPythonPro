def my_function(a, b, c=None):
    return a + b

print(dir(my_function))
print(my_function.__dict__)
print(my_function.__code__)
print(my_function.__code__.co_argcount)
print(my_function.__code__.co_varnames)
print(my_function.__code__.co_kwonlyargcount)