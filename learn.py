import cv2
import numpy as np

img=cv2.imread(".\input\\rc-1.png")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Calculation of Sobelx
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
     
# # Calculation of Sobely
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
laplasion=cv2.Laplacian(img,cv2.CV_64F)
# edged = cv2.Canny(laplasion, 20, 200)

# cv2.imshow("Image1",sobelx)
# cv2.imshow("Image2",sobely)
cv2.imshow("Image3",laplasion)
cv2.imshow("Image4",img)
# cv2.imshow("Image5",edged)

cv2.waitKey(0)
cv2.destroyAllWindows()
