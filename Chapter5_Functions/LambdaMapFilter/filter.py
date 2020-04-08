# Pythons filter function takes:
# 1.) a function (callable)
# 2.) only one iterable

l = [-1, -2, 1, 2]

# return True if you want to keep the value
def is_positive(val):
    if val >= 0.0:
        return True
    else:
        return False

l_filtered = list(filter(is_positive, l))
