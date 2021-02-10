#include "armstrong_numbers.h"

#include <stdlib.h>
#include <math.h>

#include <stdbool.h>

int number_of_digits(int integer);

int armstrong_sum(int digits, int integer);

/**
 * An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
 *
 * @param candidate
 * @return true if armstrong number, false otherwise
 */
bool is_armstrong_number(int candidate) {

    // whatever ^ 1 always equals whatever (and therefore is an armstrong number)
    if (abs(candidate) <= 9) {
        return true;
    }

    int digits = number_of_digits(candidate);

    return candidate == armstrong_sum(digits, candidate);
}

// duplicate abs() and checks in this excercism, but I want to keep the function correct for future use
int number_of_digits(int integer) {

    integer = abs(integer);

    if (integer <= 9) {
        return 1;
    }

    int number_of_digits = 0;

    int remaining = integer;
    while (remaining > 0) {
        number_of_digits++;
        remaining /= 10;
    }

    return number_of_digits;
}

int armstrong_sum(int digits, int candidate) {
    int sum = 0;

    int remaining = abs(candidate);
    while (remaining > 0) {
        int current = remaining % 10;
        sum += pow(current, digits);
        remaining /= 10;
    }
    return sum;
}
