cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef cython_clip(long[:] a, long min_value, long max_value, long[:] out):
    if min_value > max_value:
        raise ValueError("min_value must be <= max_value")
    if a.shape[0] != out.shape[0]:
        raise ValueError("input and output arrays must be the same size")
    for i in range(a.shape[0]):
        out[i] = (a[i] if a[i] < max_value else max_value) if a[i] > min_value else min_value
