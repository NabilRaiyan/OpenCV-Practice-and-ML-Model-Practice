# until 52 min


import cv2 as cv
import numpy as np

img = cv.imread('Photos/Cat.jpeg')
cv.imshow('Cat', img)


# translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down


translatedImg = translate(img, -100, -50)
cv.imshow('Translated Image',translatedImg)

# Rotation 
def rotate(img, angel, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angel, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotatedImg = rotate(img, 45)
cv.imshow('Rotated Image', rotatedImg)

# Resize image
resize = cv.resize(img, (500, 400), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized image", resize)

# flipping
flip = cv.flip(img, 1)
cv.imshow("Flipped image", flip)


cv.waitKey(0)
