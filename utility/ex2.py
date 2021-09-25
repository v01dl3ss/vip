import cv2
import numpy as np


def grey_convert(img):
    h, w, c = img.shape
    grey_img = np.zeros((h, w, 1), dtype=np.uint8)
    i = 0
    while i < w:
        j = 1
        while j < h:
            grey_img[j, i] = 0.2989 * img[j, i, 0] + 0.5870 * img[j, i, 1] + 0.1140 * img[j, i, 2]
            j = j + 1
        i = i + 1
    return grey_img
