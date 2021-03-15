#ifndef ARMSTRONG_NUMBERS
#define ARMSTRONG_NUMBERS

#include <stdbool.h>

/**
 * An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
 *
 * @param candidate
 * @return true if armstrong number, false otherwise
 */
bool is_armstrong_number(int candidate);

/**
 * An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
 *
 * @param number
 * @return the armstrong sum of the number
 */
int armstrong_sum(int number);

#endif
