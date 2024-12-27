

import numpy as np
import cv2

# creating object
fgbg1 = cv2.createBackgroundSubtractorMOG2()
fgbg2 = cv2.createBackgroundSubtractorKNN()

# capture frames from a camera
cap = cv2.VideoCapture(0)

while(1):
    # read frames
    ret, img = cap.read()

    # apply mask for background subtraction
    fgmask1 = fgbg1.apply(img)
    fgmask2 = fgbg2.apply(img)

    cv2.imshow('Original', img)
    cv2.imshow('MOG2', fgmask1)
    cv2.imshow('KNN', fgmask2)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

