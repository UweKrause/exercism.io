def validate_input(func):
    def validator(number):
        if number <= 0 or number > 64:
            raise ValueError("Invalid input")
        else:
            return func(number)

    return validator


@validate_input
def square(number: int):
    return 2 ** (number - 1)


def total(fields: int = 64):
    return sum(square(x) for x in range(1, fields + 1))
