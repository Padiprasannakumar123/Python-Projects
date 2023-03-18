import img2pdf
from PIL import Image
import os
img_path="WIN_20230213_22_14_24_Pro.jpg"
pdf_path="C:\Users\PARASURAM\Desktop\python assignments\pythonimage.pdf"
image=Image.open(img_path)
pdf_bytes=img2pdf.convert(image.filename)
file=open(pdf_path,"wb")
file.write(pdf_bytes)
image.close()
file.close()
print("converted image to pdf")