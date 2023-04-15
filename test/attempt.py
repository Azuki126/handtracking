import cv2

img = cv2.imread("test/rotated_fue.png")
img = img[0:801, 270:355]

cv2.imwrite("test/baked.png", img)
print(img.shape)