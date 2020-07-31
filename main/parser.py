import argparse
from func import get_image_details, flip_image_vertically,flip_image_horizontally,convert_to_black_and_white,crop_image,rotate_image,resize_image,convert_to_jpg
from PIL import Image
import os

parser = argparse.ArgumentParser()
parser.add_argument("mani",help="Press 1 to get details about image: \nPress 2 to flip image vertically: \nPress 3 to flip image horizantally: \nPress 4 to change color of the image: \nPress 5 to crop the image: \nPress 6 to rotate the image: \nPress 7 to resize the image: \nPress 8 to covert the file extension to .jpg: \nSelect a number form the option:",type=int)
args = parser.parse_args()
print(args)
img_source = "../Images/wallpaper.png"
if args.mani == 1 :
    data = get_image_details(img_source)    
    print(f"FileType: {data[0]}" + f"\nImageSize: {data[1]}" + f"\nImageChannel:{data[2]}")
elif args.mani == 2 :
    try:
        data = flip_image_vertically(img_source)
        data.show()
    except:
        data = flip_image_vertically(img_source)
        print(data)
elif args.mani == 3 :
    try:
        data = flip_image_horizontally(img_source)
        data.show()
    except:
        data = flip_image_horizontally(img_source)
        print(data)
elif args.mani == 4 :
    try:
        data = convert_to_black_and_white(img_source)
        data.show()
    except:
        data = convert_to_black_and_white(img_source)
        print(data)
elif args.mani == 5 :
    try:
        data = crop_image(img_source,100,120,140,200)
        data.show()
    except:
        data = crop_image(img_source,100,120,140,200)
        print(data)
elif args.mani == 6 :
    try:
        data = rotate_image(img_source,180 )
        data.show()
    except:
        data = rotate_image(img_source,180)
        print(data)
elif args.mani == 7 :
    try:
        h = int(input("enter height :"))
        w = int(input("enter width :"))
        data = resize_image(img_source,h,w)
        data.show()
    except:
        data = resize_image(img_source,h,w)
        print(data)
elif args.mani == 8 :
    data = convert_to_jpg()
    print(data)
else:
    print(f"We do not have option {args.mani}. Please try again.")        
