#include "darts.h"
#include <math.h>



int score(coordinate_t landing_position) {
    return points_by_distance(distance_by_koordinates(landing_position));
}

float distance_by_koordinates(coordinate_t landing_position) {
    /*
     * Pythagoras: a^2 + b^2 == c^2
     * c = sqrt(a^2 + b^2)
     */
    
    float x = landing_position.x;
    float y = landing_position.y;
    
    return sqrt(x*x + y*y);
}

int points_by_distance(float distance)
{    
    if (distance <= DISTANCE_INNER) return POINTS_INNER;
    if (distance <= DISTANCE_MIDDLE) return POINTS_MIDDLE;
    if (distance <= DISTANCE_OUTER) return POINTS_OUTER;    
    
    return POINTS_MISS;
}
