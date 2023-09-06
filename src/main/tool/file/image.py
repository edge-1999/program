import cv2
import numpy as np


def an_inch_id_photo(file, new_file):
    img = cv2.resize(cv2.imread(file), None, fx=1.5, fy=1.5)
    dilate = cv2.dilate(
        cv2.erode(cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), np.array([55, 50, 125]), np.array([255, 255, 255])),
                  None, iterations=10), None, iterations=10)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if dilate[i, j] == 255:  # 像素点255表示白色, 180为灰度
                # 蓝底 (255, 0, 0)   红底(0, 0, 255)  白底(255, 255, 255)
                img[i, j] = (255, 255, 255)
    del dilate
    cv2.imwrite(new_file, img)
    del img
    # res = cv2.imread(new_file)
    # cv2.imshow('result...', res)
