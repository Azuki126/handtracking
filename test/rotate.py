import cv2

img = cv2.imread("test/fue.png")

height, width = img.shape[:2]
center = (width/2, height/2)

#アフィン変換行列を作成する
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=33, scale=1)

rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))

cv2.imwrite('rotated_fue.png', rotated_image)
