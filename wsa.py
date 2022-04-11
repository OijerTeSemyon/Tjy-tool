import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd
import os
import shutil

name_list = os.listdir("./Originalpic/")
houzhui = name_list[0][name_list[0].find('.'):]
for i in range(len(name_list)):
    name = name_list[i]
    shutil.move("./Originalpic/"+name,"./"+"originalpic"+houzhui)

file = pd.read_excel(io='./user.xls',sheet_name=0,usecols=[0,1])
filenamelist=file["filenamelist"]
namelist=file["namelist"]
fontpath = "font/simsun.ttc"


for i in range(len(filenamelist)):
    bk_img = cv2.imread("originalpic.jpg")
    font = ImageFont.truetype(fontpath, 320)
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((100, 350),  namelist[i], font = font, fill = (255, 0, 0))
    bk_img = np.array(img_pil)
    cv2.waitKey()
    cv2.imencode('.jpg', bk_img)[1].tofile(filenamelist[i])

print("Success!")
