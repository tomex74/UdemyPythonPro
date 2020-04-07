# Simple merge of two dicts into a new one
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d3 = {**d1, **d2}
print(d3)

# It is a merge and the keys are unique!
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'd': 4}

d3 = {**d1, **d2}
print(d3)

# Merge in dict in the dict definition
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4, **d1}

print(d2)
