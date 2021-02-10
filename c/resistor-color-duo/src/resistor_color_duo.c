#include "resistor_color_duo.h"

int color_code(resistor_band_t band[])
{
    // even if it is working, this feels wrong (probably because it is...)
    // but I cant find a way to check for existence of the second value
    return band[0] * 10 + band[1];
}
