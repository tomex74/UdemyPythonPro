# x   y  OR  AND
# 0   0   0   0
# 0   1   1   0
# 1   0   1   0
# 1   1   1   1

a = False
b = True

def check_a(a):
    if a is True:
        return True
    else:
        return False

def check_b(b):
    if b is True:
        return True
    else:
        return False

if check_a(a) and check_b(b):
    print("hi")
else:
    print("bye")
