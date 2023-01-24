from PIL import Image
from pytesseract import pytesseract
Tesseract_Path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ImagePath = input("Please enter image path :")

pytesseract.tesseract_cmd = Tesseract_Path
Image = Image.open(ImagePath)
ImageText = pytesseract.image_to_string(Image)
print(ImageText)