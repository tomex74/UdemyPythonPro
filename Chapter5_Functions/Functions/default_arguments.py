def f(a, b, c=100):
    return a + b + c

x = 2
y = 3
z = 4

print(f(x, y, z))
print(f(x, y))

# Error
# def f(a, b=100, c):
#     return a + b + c

def f(a, b=-100, c=100):
    return a + b + c

print(f(a=x, b=y, c=z))
print(f(a=x, c=y))
print(f(a=x))
print(f(a=x))
