import cv2 as cv
import numpy as np

img1 = cv.imread("foto.jpg", 0)

height, width = img1.shape
height = int(height * 0.2)
width = int(width * 0.2)

img1 = cv.resize(img1, (width, height), interpolation = cv.INTER_AREA)

#cv.imshow("Foto", img1)
#cv.waitKey(0)
#cv.destroyAllWindows()

menor = np.min(img1)
maior = np.max(img1)
media = (menor + maior) // 2

img_bin = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        pixel = img1[i,j];
        if pixel < media:
            img_bin[i,j] = 0;
        else:
            img_bin[i,j] = 255;

cv.imshow("Foto Binarizada", img_bin)
cv.waitKey(0)
cv.destroyAllWindows()