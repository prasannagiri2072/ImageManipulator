from PIL import Image

def get_image_details(image):
    img = Image.open(image)
    im = img.format, img.size, img.mode
    return im

def flip_image_vertically(image):
    try:
        img = Image.open(image)
        im = img.transpose(Image.FLIP_LEFT_RIGHT)
        return im
    except:
        message = "Either file location is wrong or something else went wrong."
        return message
    

def flip_image_horizontally(img):
    try:    
        img = Image.open(img)
        out = img.transpose(Image.FLIP_TOP_BOTTOM)
        return out 
    except:
        message = "Either file location is wrong or something else went wrong."
        return message
    
def convert_to_black_and_white(img):
    try:
        im = Image.open(img)
        im = im.convert("L")
        return im 
    except:
        message = "Either file location is wrong or something else went wrong."
        return message
    


def crop_image(img,x1,y1,x2,y2):
    try:
        im = Image.open(img)
        box = (x1, y1, x2, y2)
        region = im.crop(box)
        return region   
    except:
        message = "Either file location is wrong or something else went wrong."
        return message



def rotate_image(img, angle):
    try:
        img = Image.open(img)
        region = region.transpose(Image.ROTATE_180)
        return region
    except:
        message = "Either file location is wrong or something else went wrong."
        return message
def resize_image(img,h,w):
    try:
        im = Image.open(img)
        out = im.resize((h,w))
        return out
    except:
        message = "Either file location is wrong or something else went wrong."
        return message

def convert_to_jpg():
    filename = "IMG_1175.JPG"
    f = filename.split(".")
    if f == ".JPG":
        print("the file extension is already in .JPG")
    else:
        print("the file is not in .jpg ")
        