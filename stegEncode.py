from PIL import Image
import random


#Clear the key
decode_key = open("key.txt", "w")  # Insert image to encode
decode_key.write("")
decode_key.close()


#Recursive method
def get_random_valid_xy(ascii_val, ima, xsize, ysize):
    x_ran = random.randint(0, xsize-1)
    y_ran = random.randint(0, ysize-1)
    # print("x:", x_ran, " y:", y_ran)
    rgb = ima[x_ran, y_ran]
    if rgb[0] + ascii_val <= 255: #useless to check like this
        return x_ran, y_ran
    elif rgb[1] + ascii_val <= 255:
        return x_ran, y_ran
    elif rgb[2] + ascii_val <= 255:
        return x_ran, y_ran
    else:
        return get_random_valid_xy(ascii_val, ima, xsize, ysize)


# count_stop = 0
#Recursive method
def get_random_valid_xy2(ascii_val, ima, xsize, ysize, max_rgb_value_difference):  # , count_stop
    x_ran = random.randint(0, xsize-1)
    y_ran = random.randint(0, ysize-1)
    # print("x:", x_ran, " y:", y_ran)
    rgb = ima[x_ran, y_ran]
    if max_rgb_value_difference >= rgb[0] - ascii_val >= 0:
        return x_ran, y_ran
    elif max_rgb_value_difference >= rgb[1] - ascii_val >= 0:
        return x_ran, y_ran
    elif max_rgb_value_difference >= rgb[2] - ascii_val >= 0:
        return x_ran, y_ran
    # elif count_stop == 100: #To avoid infinite or long lasting loop in case none or few valid positions
    #     return None
    else:
        return get_random_valid_xy2(ascii_val, ima, xsize, ysize, max_rgb_value_difference)


#Bad idea? un_scramble on the decode side to get the actual coordinates?
def scramble_coordinates(x_coord, y_coord):
    x_coord *= 5
    y_coord *= 7
    return x_coord, y_coord


im = Image.open('test2.png')
image = im.load()
text = input("Enter text:")
decode_key = open("key.txt", "a")

x_size = im.size[0]  # Determine size of image: ima.size[0]
y_size = im.size[1]  # Determine size of image: ima.size[1]

for letter in text:
    ascii_value = ord(letter)
    # x, y = get_random_valid_xy(ascii_value, image, x_size, y_size)  # Random valid position
    x, y = get_random_valid_xy2(ascii_value, image, x_size, y_size, 50)  # Random valid position
    print("x:", x, " y:", y)
    RGB = image[x, y]

    # To make the change less obvious it's best to change the smallest rgb value
    smallest_rgb_index = 0
    if RGB[0] > RGB[1]:
        smallest_rgb_index = 1
    if RGB[1] > RGB[2]:
        smallest_rgb_index = 2

    list_RGB = list(RGB)
    list_RGB[smallest_rgb_index] = ord(letter)
    new_RGB = tuple(list_RGB)

    print("smallestvalindex:", RGB, new_RGB, smallest_rgb_index)
    image[x, y] = new_RGB
    decode_key.write(str(x) + " ")
    decode_key.write(str(y) + " ")
    decode_key.write(str(smallest_rgb_index) + "\n")

decode_key.close()
im.show()
im.save("test_modified2.png", "PNG")