from math import sqrt
from numbers import Number

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __call__(self):
        self.__repr__()

    def __repr__(self):
        return 'vector.Vector2D(%r, %r)' % (self.x, self.y)

    def __str__(self):
        return '(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return sqrt(pow(self.x) + pow(self.y))

    def __bool__(self):
        return bool(abs(self))

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector2D(x, y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, Number):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError('Passed in argument must be from type Vector2D or Number.')

    def __truediv__(self, scalar):
        if scalar == 0.0:
            raise ValueError('Passed in a scalar value of zero.')
        return Vector2D(self.x / scalar, self.y / scalar)
