from collections import defaultdict


def validate_input(function):
    """Decorator. Main functions are executed only with valid input."""

    def validator(min_factor, max_factor):
        if max_factor < min_factor:
            raise ValueError("Min factor must be smaller or equal as max factor")
        if min_factor == max_factor:
            return None, []
        else:
            return function(min_factor, max_factor)

    return validator


@validate_input
def largest(min_factor, max_factor):
    return largest_or_smallest(min_factor, max_factor, 'largest')


@validate_input
def smallest(min_factor, max_factor):
    return largest_or_smallest(min_factor, max_factor, 'smallest')


def largest_or_smallest(min_factor, max_factor, function_name):
    products_and_factors = palindromeproducts(min_factor, max_factor)

    if products_and_factors == {}:
        return None, []
    if function_name == 'largest':
        return max(products_and_factors), products_and_factors.get(max(products_and_factors))
    if function_name == 'smallest':
        return min(products_and_factors), products_and_factors.get(min(products_and_factors))


def palindromeproducts(min_factor, max_factor):
    """Calculates a dictionary with palindrome products. Keys are the products. Values are lists of factor lists"""
    dictionary = defaultdict(list)

    for x in range(min_factor, max_factor + 1):
        for y in range(min_factor, max_factor + 1):
            product = x * y
            if is_palindrome(product):
                dictionary[product].append([x, y])
    return dictionary


def is_palindrome(candidate: int) -> bool:
    reverse = int(str(candidate)[::-1])
    return candidate == reverse
