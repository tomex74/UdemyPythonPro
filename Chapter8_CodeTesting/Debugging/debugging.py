'''
1.) Simple Debugging with one file
2.) Debugging with an external module
3.) Debugging with passed in arguments
'''
from math import sqrt

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return sqrt(pow(self.x) + pow(self.y))

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__ == "__main__":
    v1 = Vector(1, 1)
    v2 = Vector(3, 3)
    v3 = v1 + v2
