#include "armstrong_numbers.h"

#include <stdlib.h>
#include <math.h>

/**
 * @param integer
 * @return the number of digits this integer has
 */
static int number_of_digits(int integer);


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


int armstrong_sum(int number) {

    int armstrong_sum = 0;

    int digits = number_of_digits(number);

    for (int remaining = number; remaining > 0; remaining /= 10) {
        int current = remaining % 10;
        armstrong_sum += pow(current, digits);
    }

    return armstrong_sum;
}

// there already was a check for numbers smaller than 9, but I want to keep this function correct.
int number_of_digits(int integer) {

    // trivial case, dont waste cpu cycles on division, early return
    if (abs(integer) <= 9) return 1;

    int number_of_digits = 0;

    for (int remaining = abs(integer); remaining > 0; remaining /= 10) {
        number_of_digits++;
    }

    return number_of_digits;
}
