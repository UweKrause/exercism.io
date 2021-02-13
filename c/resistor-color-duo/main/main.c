#include "../src/resistor_color_duo.h"
#include <stdio.h>

int main() {
    
    /*
     * when called with less than 2 arguments, the second item will be initialized with 0
     * (and semantic analysis in IDE complains)
     */
    printf("color code: %d\n", color_code((resistor_band_t[]){ BROWN }));
    
    // works as intended
    printf("color code: %d\n", color_code((resistor_band_t[]){ BROWN, ORANGE, RED , YELLOW}));
    
    
    
}
