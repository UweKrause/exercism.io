#include "src/darts.h"
#include <stdio.h>

int main() {
    coordinate_t landing_position = { -9.0F, 9.0F };
    
    double distance = distance_by_koordinates(landing_position);

    int scored = score(landing_position);
    printf("distance: %f, score:%d", distance, scored);
} 
