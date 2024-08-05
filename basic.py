import cv2 as cv

img = cv.imread('Photos/Cat.jpeg')
cv.imshow('Cat', img)


# convert and image to gray scale
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scale', grayImg)

# Blur
blurImg = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
cv.imshow("Blured image", blurImg)


# Edge cascade finding edges in an image
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edge', canny)


# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('Dialated Image',dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded Image',eroded)

# Resize or crop an image
resizedImg = cv.resize(img, (600, 500))
cv.imshow('Resized image', resizedImg)

croppingImg = img[100:200, 200:400]
cv.imshow("Cropped Image", croppingImg)

cv.waitKey(0)