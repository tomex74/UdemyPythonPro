from math import sqrt
from numbers import Number

class Vector2D:
    def __init__(self, x=0, y=0):
        """Constrcutor of the vector class.

        Args:
            x (scalar): The value of the x-coordinate
            x (scalar): The value of the y-coordinate
        """
        self.x = x
        self.y = y

    def __call__(self):   
        """Returns the representation of the vector as a string.
        """
        self.__repr__()

    def __repr__(self):
        """Returns the representation of the vector as a string.
        """
        return 'vector.Vector2D(%r, %r)' % (self.x, self.y)

    def __str__(self):
        """Returns the representation of the vector as a string.
        """
        return '(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        """Returns the absolute value, which is the magnitude
        of the vector
        
        Returns:
            float: The absolute value of the vector.
        """
        return sqrt(pow(self.x) + pow(self.y))

    def __bool__(self):
        """Returns if any value of the vector is not zero.
        
        Returns
            bool: If any value is not equal to zero.
        """
        return bool(abs(self))

    def __eq__(self, other):
        """Checks wether the vector is equal to the other vector, by
        comparing all values.
        
        Args:
            other (Vector2D): Vector that is left of the equallity operator.
        
        Returns:
            bool: If both vectors have the same values.
        """
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other):
        """[summary]
        
        Args:
            other ([type]): [description]
        
        Returns:
            [type]: [description]
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)

    def __sub__(self, other):
        """[summary]
        
        Args:
            other ([type]): [description]
        
        Returns:
            [type]: [description]
        """
        x = self.x - other.x
        y = self.y - other.y
        return Vector2D(x, y)

    def __mul__(self, other):
        """[summary]
        
        Args:
            other ([type]): [description]
        
        Raises:
            TypeError: [description]
        
        Returns:
            [type]: [description]
        """
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, Number):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError('Passed in argument must be from type Vector2D or Number.')

    def __truediv__(self, scalar):
        """[summary]
        
        Args:
            scalar ([type]): [description]
        
        Raises:
            ValueError: [description]
        
        Returns:
            [type]: [description]
        """
        if scalar == 0.0:
            raise ValueError('Passed in a scalar value of zero.')
        return Vector2D(self.x / scalar, self.y / scalar)
