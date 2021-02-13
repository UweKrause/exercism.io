#include "resistor_color_trio.h"
#include <math.h>

int color_code_duo(resistor_band_t band[static 2])
{
    return band[0] * 10 + band[1];
}

resistor_value_t color_code(resistor_band_t band[static 3])
{
    int value = color_code_duo(band) * pow(10, band[2]);
    unit_t unit = OHMS;
    
    if (value >= 1000) {
        value /= 1000;
        unit = KILOOHMS;
    }
    
    return (resistor_value_t) {value, unit};
}
