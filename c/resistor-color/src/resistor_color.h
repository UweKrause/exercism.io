#ifndef RESISTOR_COLOR_H
#define RESISTOR_COLOR_H

// just copied from the testcases for now, just to get rid of compiler errors
typedef enum {
    BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, GREY, WHITE
} resistor_band_t;

int color_code(resistor_band_t band);

resistor_band_t colors();

#endif
