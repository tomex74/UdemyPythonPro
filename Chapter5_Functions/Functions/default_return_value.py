def foo1(val):
    if val:
        return val
    else:
        return None

def foo2(val):
    if val:
        return val

def square_list(lst):
    lst = [val**2 for val in lst]
    return lst # if not returned => None

if __name__ == "__main__":
    print(foo1(0))
    print(foo2(0))

    lst = [1, 2, 3]
    lst = square_list(lst)
    print(lst)
