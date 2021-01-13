import math


def classify(number: int) -> str:
    check_input(number)

    a = aliquot_sum(number)
    if a == number:
        return "perfect"
    if a > number:
        return "abundant"
    else:
        return "deficient"


def check_input(number: int):
    if number <= 0:
        raise ValueError("Input must be positive integer")


def aliquot_sum(number: int) -> int:
    return sum(factors(number)) - number


def factors(number: int) -> list[int]:
    factors = [candidate for candidate in lower_half_of_range(1, number) if is_factor(number, candidate)]
    if number > 1:
        factors.append(number)
    return factors


def lower_half_of_range(start: int, number: int):
    """
    Returns the lower half of the full range to the upper end of the full range.
    If the total range is not even dividable, the middlemost value of the full range belongs to the lower half.

    :param start: The lower end of the ranges
    :param number: The upper end of the full range
    :return: the lower half of the full range, starting with the specified lower end, including the middlemost number
    """
    return range(start, math.ceil(number / 2) + 1)


def is_factor(number: int, x: int) -> bool:
    return number % x == 0
