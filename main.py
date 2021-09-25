import cv2
import glob
import os
from pathlib import Path
from utility.ex1 import *
from utility.ex2 import *

print("Package Imported")

# Ex1
videos = glob.glob("resources/videos/*.mp4")
for v in videos:
    des = make_folder(v)
    convert_video2image(v, 5, 0, des)

# Ex2
b = cv2.imread("resources/images/color.jpg")
b = grey_convert(b)
cv2.imshow("ex2", b)
cv2.waitKey(0)

