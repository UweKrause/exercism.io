#ifndef RESISTOR_COLOR_TRIO_H
#define RESISTOR_COLOR_TRIO_H

    typedef enum {
        BLACK   = 0,
        BROWN   = 1,
        RED     = 2,
        ORANGE  = 3,
        YELLOW  = 4,
        GREEN   = 5,
        BLUE    = 6,
        VIOLET  = 7,
        GREY    = 8,
        WHITE   = 9
    } resistor_band_t;
    
    #define OHMS "ohms"
    #define KILOOHMS "kiloohms"
        
    typedef struct resistor_value_t {
        int value;
        char unit[9]; // make enough space for the string (plus \0 )
    } resistor_value_t;
    
    resistor_value_t color_code(resistor_band_t band[]);

#endif
