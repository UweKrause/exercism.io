#include "../src/armstrong_numbers.h"

#include <stdio.h>

int main(void) {

    int in[5] = {0, 1, 12, 153, 12345};

    for (int i = 0; i < 5; ++i) {
        int cand = in[i];
        printf("%d : %d\n", cand, is_armstrong_number(cand));
    }


    return 0;
}