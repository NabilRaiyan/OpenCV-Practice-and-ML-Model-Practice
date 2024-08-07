# untill 1:18 hr

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/Cat.jpeg')

plt.imshow(img)
plt.show()
# cv.imshow('Cat', img)

# # BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)


# # BGR to L*a*b

# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('Lab', lab)



# cv.waitKey(0)