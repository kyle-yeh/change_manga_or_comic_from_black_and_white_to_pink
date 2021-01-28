import sys
from pathlib import Path

import cv2
import numpy as np

from config.base import config


base = config()


def change_hsv_format_for_cv2(hsv):
    h = int(hsv[0] / 360 * 255)
    s = int(hsv[1] / 100 * 255)
    v = int(hsv[2] / 100 * 255)
    return [h, s, v]

for i in [[0],[1],[2]]:




def gray_to_pink(img,hsv):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in gray:
        for j in i:


hsv = change_hsv_format_for_cv2(base['hsv'])
for arg in sys.argv[1:]:
    _p = str(Path(arg))
    _p = r"C:\Github\change_manga_or_comic_from_black_and_white_to_pink\1.jpg"
    print(_p)
    img = cv2.imread(_p)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray.shape
    img.shape


    gray[0][0]
    np.max(gray[0])
    len(gray[0])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

input('')
