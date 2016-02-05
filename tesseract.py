from PIL import Image
import pytesseract
#print pytesseract.image_to_string(Image.open('test.jpg'))
#print pytesseract.image_to_string(Image.open('test2.jpg'))
data= pytesseract.image_to_string(Image.open('rocket.jpg'))
words=[]
words=data.split(' ')
print words[0]
print words[1]
returnString=[]
for word in words:
    returnString.append('{\"word:\":\"%s\"}' % word)
print returnString