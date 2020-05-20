import pytesseract
from PIL import Image,ImageEnhance
from wand.image import Image as wi
import spacy
import numpy as np
import PyPDF2
import cv2
import re


pdf=wi(filename="TE_198.pdf",resolution=200)
pdfImage=pdf.convert("jpeg")

for img in pdfImage.sequence:
    page=wi(image=img)
    page.save(filename="my_first_image.jpg")

text=pytesseract.image_to_string('my_first_image.jpg')
with open('file.txt', mode = 'w') as f:
    f.write(text)

with open("file.txt", "r") as myfile:
    data=myfile.readlines()

nlp = spacy.load('en_core_web_sm')
ans=[]
for string in data:
    k=0
    check=string.split()
    for items in check:
        if(items.lower()=='total' or items.lower()=='subtotal'):
            k=1
    if k==0:
        for strr in check:
            try : 
	            float(strr) 
	            res = True
            except: 
	            res = False
            if(res==True):
                for c in strr:
                    if(c=='.'):
                        ans.append(float(strr))
                        break
        doc=nlp(string)
        for ent in doc.ents:
            if ent.label_=='MONEY':
                try:
                    float(ent.text)
                    chk=True
                except:
                    chk=False
                if chk==True:
                    ans.append(float(ent.text))
                
fans=0
for k in ans:
    fans+=k
print(fans)