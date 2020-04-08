my_var = 42

def f(my_var):
    local_var = 52
    print(local_var + my_var)

if __name__ == "__main__":
    my_var = 32
    f(my_var)
