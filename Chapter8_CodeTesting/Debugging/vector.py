from math import sqrt
from numbers import Number

class Vector2D:
    def __init__(self, x=0, y=0):
        """Constrcutor of the vector class.

        Parameters
        ----------
        x : scalar
            The value of the x-coordinate
        y : scalar
            The value of the y-coordinate
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
        
        Returns
        -------
        float
            The absolute value of the vector.
        """
        return sqrt(pow(self.x) + pow(self.y))

    def __bool__(self):
        """Returns if any value of the vector is not zero.
        
        Returns
        -------
        bool
            If any value is not equal to zero.
        """
        return bool(abs(self))

    def __eq__(self, other):
        """Checks wether the vector is equal to the other vector, by
        comparing all values.
        
        Parameters
        ----------
        other : Vector2D
            Vector that is left of the equallity operator.
        
        Returns
        -------
        bool
            If both vectors have the same values.
        """
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other):
        """Adds the vector with another vector.
        
        Parameters
        ----------
        other : Vector2D
            Vector that is left of the plus operator.
        
        Returns
        -------
        Vector2D
            The result vector of the addition.
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)

    def __sub__(self, other):
        """Subtracts the vector with another vector.
        
        Parameters
        ----------
        other : Vector2D
            Vector that is left of the minus operator.
        
        Returns
        -------
        Vector2D
            The result vector of the subtraction.
        """
        x = self.x - other.x
        y = self.y - other.y
        return Vector2D(x, y)

    def __mul__(self, other):
        """Multiplicates the vector with i.) another vector, or ii.) with a scalar.

        Parameters
        ----------
        other : Vector2D or scalar
            Vector (or scalar) that is left of the multiplication operator.
        
        Returns
        -------
        Vector2D
            The result vector of the vector * scalar multiplication, or
            the result scalar of the vector * vector multiplication.

        Raises
        ------
        ValueError
            Other must be a number or a Vector2D.
        """
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, Number):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError('Passed in argument must be from type Vector2D or Number.')

    def __truediv__(self, scalar):
        """Divides the vector by a scalar value.
        
        Parameters
        ----------
        scalar : number
            Scalar value to divide by.
        
        Returns
        -------
        Vector2D
            The result of the scalar division.
        
        Raises
        ------
        ValueError
            If the passed in scalar is zero.
        """
        if scalar == 0.0:
            raise ValueError('Passed in a scalar value of zero.')
        return Vector2D(self.x / scalar, self.y / scalar)
