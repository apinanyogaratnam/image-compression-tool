from utilities import *
from PIL import ImageFilter


def greyscale_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        colour_sum = round(current_tuple[0]*0.3) + round(current_tuple[1]*0.59) + round(current_tuple[1]*0.11)
        current_tuple[0] = colour_sum
        current_tuple[1] = colour_sum
        current_tuple[2]= colour_sum
        data.append(tuple(current_tuple))
    
    footer(image, data, "greyscale_filter")


def green_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] = round(current_tuple[0]*0.3)
        current_tuple[1] = round(current_tuple[1]*0.59)
        current_tuple[2]= round(current_tuple[1]*0.11)
        data.append(tuple(current_tuple))
    
    footer(image, data, "green_filter")


def greyscale_alternative_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        avg = round(sum(current_tuple) / 3)
        current_tuple[0] = avg
        current_tuple[1] = avg
        current_tuple[2]= avg
        data.append(tuple(current_tuple))
    
    footer(image, data, "greyscale_alternate_filter")

def blue_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] = 0
        data.append(tuple(current_tuple))
    
    footer(image, data, "blue_filter")


def dark_blue_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[1] = 0
        data.append(tuple(current_tuple))
    
    footer(image, data, "pink_filter")


def yellow_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[2] = 0
        data.append(tuple(current_tuple))

    footer(image, data, "yellow_filter")


def reduce_opacity_filter(image, opacity_level):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] = round(current_tuple[0] / opacity_level)
        current_tuple[1] = round(current_tuple[1] / opacity_level)
        current_tuple[2] = round(current_tuple[2] / opacity_level)
        data.append(tuple(current_tuple))

    footer(image, data, "reduce_opacity_filter")


def blur_filter_3x3(image):
    size_of_image = image.size
    width = size_of_image[0]
    image_data = list(image.getdata())

    data = []
    for i in range(len(image_data)):
        p1, p2, p3 = i, i+1, i+2
        p4, p5, p6 = p1 + width, p1 + width + 1, p1 + width + 2
        p7, p8, p9 = p4 + width, p4 + width + 1, p4 + width + 2

        if (p9 > len(image_data)-1): break

        average_tuple = get_average_tuple([image_data[p1], image_data[p2], image_data[p3], image_data[p4], image_data[p5], image_data[p6], image_data[p7], image_data[p8], image_data[p9]])
        data.append(average_tuple)

    footer(image, data, "blur_filter")


def blur_filter_4x3(image):
    size_of_image = image.size
    width = size_of_image[0]
    image_data = get_image_data(image)

    data = []
    for i in range(len(image_data)):
        p1, p2, p3, p4 = i, i+1, i+2, i+3
        p5, p6, p7, p8 = p1 + width, p1 + width + 1, p1 + width + 2, p1 + width + 3
        p9, p10, p11, p12 = p5 + width, p5 + width + 1, p5 + width + 2, p5 + width + 3

        if (p12 > len(image_data)-1): break

        average_tuple = get_average_tuple([image_data[p1], image_data[p2], image_data[p3], image_data[p4], image_data[p5], image_data[p6], image_data[p7], image_data[p8], image_data[p9], image_data[p10], image_data[p11], image_data[p12]])
        data.append(average_tuple)

    footer(image, data, "blur_filter")

# results:
    # 3x3: caused paleness
    # 4x4 caused brightness


def blur_lib_filter(image, level_of_blur):
    """Blur an image depending on level_of_blur from 0 to 100
    """

    image = image.filter(ImageFilter.GaussianBlur(level_of_blur))
    # image.filter(ImageFilter.BLUR)

    footer_without_data(image, "blurry_image_filter")


def luminosity(image, level_of_luminosity):
    """Filter increases or reduces luminosity depeneding on
    level_of_luminosity
    """

    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] += level_of_luminosity
        current_tuple[1] += level_of_luminosity
        current_tuple[2] += level_of_luminosity
        data.append(tuple(current_tuple))
    
    footer(image, data, "blue_filter")