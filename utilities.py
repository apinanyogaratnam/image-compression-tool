def footer_without_data(image, name_of_file):
    """Saves an image with the given name_of_file and saves it as 
    a .jpg file
    """

    image.save(name_of_file + ".jpg")
    print("Image saved in " + name_of_file + ".jpg")
    image.show()


def footer(image, data, name_of_file):
    """Saves an image with the given name_of_file and saves it as 
    a .jpg file using data as the data as the newly formed pixels
    """

    image.putdata(data)
    image.save(name_of_file + ".jpg")
    print("Image saved in " + name_of_file + ".jpg")
    image.show()


def get_average_tuple(list_of_tuples):
    """Return the average tuple from the list_of_tuples
    """

    sum_0 = 0
    sum_1 = 0
    sum_2 = 0

    for i in range(len(list_of_tuples)):
        sum_0 += list_of_tuples[i][0]
        sum_1 += list_of_tuples[i][1]
        sum_2 += list_of_tuples[i][2]

    avg_0 = sum_0 / 9
    avg_1 = sum_1 / 9
    avg_2 = sum_2 / 9

    return (round(avg_0), round(avg_1), round(avg_2))


def get_image_data(image):
    """Return a list of pixels from image
    """
    
    return list(image.getdata())


def print_grid(lst, width):
    """Print out lst into a grid given width of desired grid
    """

    for i in range(0, len(lst), width):
        print(lst[i:i+width])
