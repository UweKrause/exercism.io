#include "../src/resistor_color.h"
#include <stdio.h>

int main() {
    
    int cc = color_code(BLACK);
    
    resistor_band_t rb = colors();
        
    printf("color code: %d band: %d\n", cc, rb);
}
