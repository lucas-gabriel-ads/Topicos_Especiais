import cv2 as cv;

pic = cv.imread('foto.jpg', 1)

width = int(pic.shape[1] * 0.2)
height = int(pic.shape[0] * 0.2)
dim = (width, height)
pic_resized = cv.resize(pic, dim, interpolation = cv.INTER_AREA)
pic_recolor = cv.cvtColor(pic_resized, cv.COLOR_BGR2GRAY)
cv.imwrite('foto_gray.png', pic_recolor)

cv.imshow('Foto Original', pic)
cv.waitKey(0)
cv.imshow('Foto Redimensionada', pic_resized)
cv.waitKey(0)
cv.imshow('Foto Escala de Cinza', pic_recolor)
cv.waitKey(0)
cv.destroyAllWindows()
