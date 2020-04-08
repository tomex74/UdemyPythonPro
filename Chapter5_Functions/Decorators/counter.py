# Decorators:
# takes a function as an argument
# returns a closure
# the clousure runs the previous passed in function with the *args and **kwargs arguments

def counter(fn):
    count = 0
    def count_up(*args, **kwargs):
        nonlocal count
        count += 1
        print('Counter: {}'.format(count))
        return fn(*args, **kwargs)
    return count_up

def f(a):
    return a**2

@counter
def f2(a):
    return a**2

if __name__ == "__main__":
    f_decorated = counter(f)
    print(f_decorated(1))
    print(f_decorated(2))
    print(f_decorated(3))

    print(f2(-1))
    print(f2(-2))
    print(f2(-3))