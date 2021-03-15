#include "armstrong_numbers.h"

#include <stdlib.h>
#include <math.h>

#include <stdbool.h>

int armstrong_sum(int integer);

int number_of_digits(int integer);

/**
 * An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
 *
 * @param candidate
 * @return true if armstrong number, false otherwise
 */
bool is_armstrong_number(int candidate) {

    /*
     * "Since the number of digits is always positive and all digits have a non-negative value
     * the Armstrong sum will always be non-negative.
     * Ergo: Negative numbers cannot be Amstrong numbers."
     * - siebenschlaefer (excercism mentor)
     */
    if (candidate < 0) return false;

    /*
     * If the number of digits is only one (1):
     * (whatever ^ 1) always equals whatever (and therefore is an armstrong number)
     */
    if (abs(candidate) <= 9) return true;

    return candidate == armstrong_sum(candidate);
}


int armstrong_sum(int candidate) {

    int sum = 0;

    int digits = number_of_digits(candidate);

    int remaining = abs(candidate);
    while (remaining > 0) {
        int current = remaining % 10;
        sum += pow(current, digits);
        remaining /= 10;
    }
    return sum;
}

// there already was a check for numbers smaller than 9, but I want to keep this function correct.
int number_of_digits(int integer) {

    // trivial case, early return
    if (abs(integer) <= 9) return 1;

    int number_of_digits = 0;

    int remaining = abs(integer);
    while (remaining > 0) {
        number_of_digits++;
        remaining /= 10;
    }

    return number_of_digits;
}
