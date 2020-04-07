# Boolean type is for Ture or False statements
# Boolean is a subclass of an int
print(issubclass(bool, int))

val = True
print(isinstance(val, bool))
val = False
print(isinstance(val, bool))

# Since bool is a inmutable singleton object,
# the 'is' and the '==' operators will return the same result
# val = 2 # important!, every number != 0 is evaluated as True, per default
# val = 1 # important!
val = True
if val is 1:
    print("same memory adress")
elif val == 1:
    print("same value")
else:
    print("none")

# Every object as a True turh value, except:
# None, False, 0, empty sequences, maybe custom classes (later in the couse)

# 1.) At first python will look for the __bool__ method
# 2.) if not defined, the __len__ method is checked
# 3.) otherwiese, it will return True

l = [1, 2, 3] # len > 0
l = []
if l:
    print("yes")
else:
    print("no")
