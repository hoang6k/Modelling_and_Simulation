import cv2


path = 'cv_cau_giay.png'
img = cv2.imread(path)

lake_color = (253, 219, 165)
bias = 20
MIN_THRESHOLD = (max(0, lake_color[0] - bias), max(0, lake_color[1] - bias), max(0, lake_color[2] - bias))
MAX_THRESHOLD = (min(255, lake_color[0] + bias), min(255, lake_color[1] + bias), min(255, lake_color[2] + bias))

lake = cv2.inRange(img, MIN_THRESHOLD, MAX_THRESHOLD)

cv2.imshow('image', img)
cv2.imshow('lake', lake)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('lake.pgm', lake)