#include "../src/resistor_color_duo.h"
#include <stdio.h>

int main() {
    
    int cc = color_code((resistor_band_t[]){ BROWN, BLACK });
        
    printf("color code: %d\n", cc);
}
