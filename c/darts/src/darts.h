#ifndef DARTS_H
#define DARTS_H



    #define DISTANCE_INNER      1
    #define DISTANCE_MIDDLE     5
    #define DISTANCE_OUTER      10

    #define POINTS_INNER    10
    #define POINTS_MIDDLE   5
    #define POINTS_OUTER    1
    #define POINTS_MISS     0
    
    typedef struct coordinate_t { float x,y; } coordinate_t;

    int score(coordinate_t landing_position);

    float distance_by_koordinates(coordinate_t landing_position);

    int points_by_distance(float distance);


#endif
