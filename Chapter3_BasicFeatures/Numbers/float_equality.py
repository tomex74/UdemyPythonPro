# In the last video we had following problem
val2 = 0.1 + 0.1 + 0.1
print(val2 == 0.3)

# Rounding does not help really
print(round(0.1, 4) + round(0.1, 4) + round(0.1, 4) == round(0.3, 4)) # False
print(round(0.1 + 0.1 + 0.1, 6) == round(0.3, 4)) # True

# For floats better compare absolute and relative tolerance
# for any eps > 0, a == b if |x - y| < eps
import math

def is_equal(x, y, eps):
    return math.fabs(x - y) < eps

eps = 1e-12

# Own implementation
val1 = 0.1 + 0.1 + 0.1
val2 = 0.3
print(is_equal(val1, val2, eps))

val1 = 10_000.1 + 10_000.1 + 10_000.1
val2 = 30_000.3
print(is_equal(val1, val2, eps))

# Relative tolerance: maximum allowed difference between the two numbers,
# based on the magnitude of the two numbers
# If rel_tol=0.01
# tol = 0.01 * max(|x|, |y|)

# Math's isclose function
val1 = 0.1 + 0.1 + 0.1
val2 = 0.3
print(math.isclose(val1, val2, rel_tol=1e-09, abs_tol=0.0))

val1 = 10_000.1 + 10_000.1 + 10_000.1
val2 = 30_000.3
print(math.isclose(val1, val2, rel_tol=1e-09, abs_tol=0.0))
