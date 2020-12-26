import math


def is_armstrong_number(number):
    numbers = list(str(number))
    power = len(numbers)

    sum_so_far = 0
    for character in numbers:
        sum_so_far += int(math.pow(int(character), power))

    return sum_so_far == number
