from PIL import Image


im = Image.open('test_modified.png')  # Insert image to decode
image = im.load()
decode_key = open("key.txt", "r")
key = decode_key.read()

final_message = ""
all_xy_coordinates = key.split("\n")
del all_xy_coordinates[len(all_xy_coordinates)-1] #To remove the last "\n" added

for xy in all_xy_coordinates:
    print("xy", xy)
    x, y, rgb_index = xy.split(" ")
    RGB = image[int(x), int(y)]
    print("RGB", RGB)
    ascii_value = RGB[int(rgb_index)]
    print("ASCII value", ascii_value)
    letter = chr(ascii_value) #Decode
    print("letter", letter)
    final_message += letter
    print("")

print("_____________________________")
print("FINAL MESSAGE:", final_message)
decode_key.close()