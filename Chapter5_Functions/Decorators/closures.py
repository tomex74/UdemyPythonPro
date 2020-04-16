# First class functions: 
# you can treat functions as any other object
# - passing as argument
# - calling
# - assigning to a variable

# Closures:
# A closure is an inner function that remembers/has access to variables in the local scope 
# of the outer function (where it was created).

def outer_fn():
    message = 'Outer: Hi!'

    def inner_fn():
        print(message)
    return inner_fn()

def main():
    outer_fn()

if __name__ == "__main__":
    main()
