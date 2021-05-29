#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// dark lines
void dark_lines_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i+=9) {
        image[i] = 0;
    }

    return;
}

// red filter
void red_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i+=3) {
        image[i] = 0;
    }

    return;
}

// empty filter
void empty_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i++) {
        image[i] = 0;
    }

    return;
}

// green filter
void green_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i+=2) {
        image[i] = 0;
    }

    return;
}

// blue/turquise filter
void blue_turquise_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i+=4) {
        image[i] = 0;
    }

    return;
}

// broken screen filter
void broken_screen_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i+=5) {
        image[i] = 0;
    }

    return;
}

// reduced opacity filter
void reduced_opacity_filter(size_t size_of_image, unsigned char *image, int opacity_level) {
    if (1 > opacity_level && opacity_level > 255) {
        printf("opacity level out of range of [1, 255]");
        return;
    }

    for (long i=0; i<size_of_image; i++) {
        image[i] = image[i] / 3;
    }

    return;
}

// brighter_filter
void brighter_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i++) {
        image[i] = image[i] * 3;
        if (image[i] >255) image[i] = 255;
    }
}

void dark_lines_filter(size_t size_of_image, unsigned char *image);
void red_filter(size_t size_of_image, unsigned char *image);
void empty_filter(size_t size_of_image, unsigned char *image);
void green_filter(size_t size_of_image, unsigned char *image);
void blue_turquise_filter(size_t size_of_image, unsigned char *image);
void broken_screen_filter(size_t size_of_image, unsigned char *image);

// opacity level range: 1 <= opacity_level <= 255
void reduced_opacity_filter(size_t size_of_image, unsigned char *image, int opacity_level);
void brighter_filter(size_t size_of_image, unsigned char *image);
