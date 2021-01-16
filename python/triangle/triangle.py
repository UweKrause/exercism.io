def validate_input(function):
    def validate(sides):
        a, b, c = sides

        # For a shape to be a triangle at all, all sides have to be of length > 0
        if a <= 0 and b <= 0 and c <= 0:
            return False

        # The sum of the lengths of any two sides must be greater than or equal to the length of the third side.
        if (a + b) <= c or (b + c) <= a or (c + a) <= b:
            return False

        return function(sides)

    return validate


@validate_input
def equilateral(sides):
    """An equilateral triangle has all three sides the same length."""
    a, b, c = sides
    return a == b == c


@validate_input
def isosceles(sides):
    """An isosceles triangle has at least two sides the same length.

    (It is sometimes specified as having exactly two sides the same length,
    but for the purposes of this exercise we'll say at least two.)"""
    a, b, c = sides
    return a == b or b == c or c == a


@validate_input
def scalene(sides):
    """A scalene triangle has all sides of different lengths."""
    a, b, c = sides
    return a != b != c
