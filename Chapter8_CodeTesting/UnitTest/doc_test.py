import doctest

import vector

def test_equality(v1):
    """ Tests the equality operator.

    >>> test_equality(v2)
    True
    """
    expected_result = vector.Vector2D(-1, 1)
    return v1 == expected_result

def test_add(v1, v2):
    """ Tests the addition operator.

    >>> test_add(v1, v2)
    True
    """
    result = v1 + v2
    expected_result = vector.Vector2D(-1, 1)
    return result == expected_result

def test_sub(v1, v2):
    """ Tests the subtraction operator.

    >>> test_sub(v2, v3)
    True
    """
    result = v1 - v2
    expected_result = vector.Vector2D(-3.5, 3.5)
    return result == expected_result

def test_mul(v1, v2):
    """ Tests the multiplication operator.

    >>> test_mul(v1, v2)
    True
    """
    result = v1 * 5
    expected_result = vector.Vector2D(0.0, 0.0)
    result2 = v1 * v2
    expected_result2 = 0.0
    return (result == expected_result) and (result2 == expected_result2)
        
if __name__ == '__main__':
    v1 = vector.Vector2D(0, 0)
    v2 = vector.Vector2D(-1, 1)
    v3 = vector.Vector2D(2.5, -2.5)

    doctest.testmod()
