def validate_input(function):
    def validate(number):
        if number <= 0:
            raise ValueError("Only positive integer please")
        else:
            return function(number)

    return validate


@validate_input
def steps(number):
    return steps_recursive(0, number)


def steps_recursive(step_count, number):
    if number == 1:
        return step_count

    number = number / 2 if number % 2 == 0 else number * 3 + 1
    return steps_recursive(step_count + 1, number)
