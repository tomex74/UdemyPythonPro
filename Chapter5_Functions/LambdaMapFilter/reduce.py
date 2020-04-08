l =[-1, 1, 5, -10, 234]

def reduce_sequence(fn, sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = fn(result, e)
    return result

print(reduce_sequence(max, l))

# Build-in reducing function:
# min, max, sum, any, all
import functools

print(functools.reduce(max, l))
print(functools.reduce(lambda a, b: a if a > b else b, l))
