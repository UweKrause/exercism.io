#include "resistor_color_trio.h"
#include <math.h>

int color_code_duo(resistor_band_t band[static 2])
{
    return band[0] * 10 + band[1];
}

resistor_value_t color_code(resistor_band_t band[static 3])
{
    int value = 0;
    unit_t unit = OHMS;
    
    int exponent = band[2];
    
    /*
     * wrap over when value gets longer than 3 digits (aka. thousand or more)
     *
     * The first 2 bands already give two digits (10)
     * one digit more is okay (exponent equals 1) (100)
     * the fourth digit would be the first thousands (exponent > 1) (1000),
     * and therefore must be wrapped.
     */
    if (exponent > 1) {
        unit = KILOOHMS;
        exponent -= 3;
    }
    
    value = color_code_duo(band) * pow(10, exponent);
    
    resistor_value_t capacity = {value, unit};
    
    return capacity;
}
