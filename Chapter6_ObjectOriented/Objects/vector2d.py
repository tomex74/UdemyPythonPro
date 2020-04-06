from math import sqrt

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector2D(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return sqrt(pow(self.x) + pow(self.y))

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
