
from func import get_image_details, flip_image_vertically,flip_image_horizontally,convert_to_black_and_white,crop_image,rotate_image,resize_image,convert_to_jpg
from PIL import Image
import os

#Getting image ready to manipulate.

img_from_user = input("Please provide path to the image to manipulate: ")

if img_from_user=="":
    print("You have not provided us any image. So, we are going for default image.")
    img_source = "C:/Users/Balu Ram Giri/Desktop/IMG_1175.JPG"
else:
    img_source = img_from_user


#Getting what manipulation to do based on user input.
img_manipulation_option = input("Press 1 to get details about image: \nPress 2 to flip image vertically: \nPress 3 to flip image horizantally: \nPress 4 to change color of the image: \nPress 5 to crop the image: \nPress 6 to rotate the image: \nPress 7 to resize the image: \nPress 8 to covert the file extension to .jpg: \nSelect a number form the option:")

if img_manipulation_option == "":
    print("No option selected. Please try again.")
elif img_manipulation_option == "1":
    data = get_image_details(img_source)
    print(f"FileType: {data[0]}" + f"\nImageSize: {data[1]}" + f"\nImageChannel:{data[2]}")
elif img_manipulation_option == "2":
    try:
        data = flip_image_vertically(img_source)
        data.show()
    except:
        data = flip_image_vertically(img_source)
        print(data)
elif img_manipulation_option == "3":
    try:
        data = flip_image_horizontally(img_source)
        data.show()
    except:
        data = flip_image_horizontally(img_source)
        print(data)
elif img_manipulation_option == "4":
    try:
        data = convert_to_black_and_white(img_source)
        data.show()
    except:
        data = convert_to_black_and_white(img_source)
        print(data)  
elif img_manipulation_option == "5":
    try:
        data = crop_image(img_source,100,120,140,200)
        data.show()
    except:
        data = crop_image(img_source,100,120,140,200)
        print(data)
elif img_manipulation_option == "6":
    try:
        data = rotate_image(img_source,180 )
        data.show()
    except:
        data = rotate_image(img_source,180)
        print(data)
elif img_manipulation_option == "7":
    try:
        h = int(input("enter height :"))
        w = int(input("enter width :"))
        data = resize_image(img_source,h,w)
        data.show()
    except:
        data = resize_image(img_source,h,w)
        print(data)
elif img_manipulation_option == "8":
    data = convert_to_jpg()
    print(data)
else:
    print(f"We do not have option {img_manipulation_option}. Please try again.")  