#include "resistor_color.h"

int color_code(resistor_band_t band) {
    
    // dummy implementation, just to get rid of compiler errors
    return (int) band;
}

resistor_band_t colors() {
    
    // just copied from the testcases for now, just to get rid of compiler errors
    resistor_band_t expected[] = {
        BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, GREY, WHITE        
    };
   
   return *expected;
}
