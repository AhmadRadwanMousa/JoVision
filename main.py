from PIL import Image
def Image_to_Black(img):
    width,height =img.size
    for x in range (width):
        for y in range (height):
            r,g,b=img.getpixel((x,y))
            gray=int((r+g+b)/3)
            img.putpixel ((x,y),(gray,gray,gray))
    return img

img_path=input ("enter image path : ")
img =Image.open(img_path)
Image_to_Black(img)
img.save("Black&White "+img_path)
