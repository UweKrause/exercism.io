import math


def distance(x, y) -> float:
    """Calculates a distance of two number coordinates x, y from the center 0, 0"""
    return math.sqrt(abs(x) ** 2 + abs(y) ** 2)


def score(x, y) -> int:
    """Calculates the points, depending on the position of the dart"""
    dis = distance(x, y)

    if dis <= 1:
        return 10
    if dis <= 5:
        return 5
    if dis <= 10:
        return 1
    else:
        return 0
