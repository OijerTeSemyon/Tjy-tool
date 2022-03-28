import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

bk_img = cv2.imread("1.jpg")

filenamelist=["B软件201_200107121018_汤靖云.jpg","B软件201_200107121022_王麒语.jpg","B软件201_200107121020_王超强.jpg"]
namelist=["汤靖云","王麒语","王超强"]
filename=""
name=""

str=input()
if (str == '18'):
    filename = filenamelist[0]
    name = namelist[0]
elif (str=='22'):
    filename = filenamelist[1]
    name = namelist[1]

elif (str=='20'):
    filename = filenamelist[2]
    name = namelist[2]

fontpath = "font/simsun.ttc"
font = ImageFont.truetype(fontpath, 320)
img_pil = Image.fromarray(bk_img)
draw = ImageDraw.Draw(img_pil)

draw.text((100, 350),  name, font = font, fill = (255, 0, 0))
bk_img = np.array(img_pil)

cv2.waitKey()
cv2.imencode('.jpg', bk_img)[1].tofile(filename)
