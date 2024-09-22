from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  

ssimage = Image.open('ss.png')
usersimage = Image.open('users.png')

sstext = pytesseract.image_to_string(ssimage)
userstext = pytesseract.image_to_string(usersimage)

print('text in screeshots : ', sstext)

print('text in users ss : ', userstext)