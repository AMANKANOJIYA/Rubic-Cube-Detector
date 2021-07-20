import cv2
import numpy as np 

img= cv2.imread("input/rubic cube-2.jpeg")
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def empty(a):
    pass


# cv2.namedWindow("HSV Tracker")
# cv2.resizeWindow("HSV Tracker", 700, 300)
# cv2.createTrackbar("HUE lower", "HSV Tracker", 0,179,empty)
# cv2.createTrackbar("HUE Upper", "HSV Tracker", 179,179,empty)
# cv2.createTrackbar("Saturation lower", "HSV Tracker", 0,255,empty)
# cv2.createTrackbar("Saturation Upper", "HSV Tracker", 255,255,empty)
# cv2.createTrackbar("Value lower", "HSV Tracker", 0,255,empty)
# cv2.createTrackbar("Value Upper", "HSV Tracker", 255,255,empty)


# while True:
#     img= cv2.imread("input/rubic cube-2.jpeg")
#     hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     hmin,hmax=cv2.getTrackbarPos("HUE lower", "HSV Tracker"),cv2.getTrackbarPos("HUE Upper", "HSV Tracker")
#     smin,smax=cv2.getTrackbarPos("Saturation lower", "HSV Tracker"),cv2.getTrackbarPos("Saturation Upper", "HSV Tracker")
#     vmin,vmax=cv2.getTrackbarPos("Value lower", "HSV Tracker"),cv2.getTrackbarPos("Value Upper", "HSV Tracker")

#     # Preparing a array of respactive lower and upper trackbar
#     l_b = np.array([hmin, smin, vmin])
#     u_b = np.array([hmax, smax, vmax])

#     # created a mask to apply on frame
#     mask = cv2.inRange(hsv, l_b, u_b)

#     # Bitwize and operator 
#     res = cv2.bitwise_and(img, img, mask=mask)

#     # Showing all the frames original, mask, res
#     cv2.imshow("frame", img)
#     cv2.imshow("hsv", hsv)
#     cv2.imshow("mask", mask)
#     cv2.imshow("res", res)

#     # Exit on key press
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#          break

# ----------- Blue Color Mask Creation ----------------
lowerBlue=np.array([100,50,50])
upperBlue=np.array([130,255,266])
BlueMask=cv2.inRange(hsv,lowerBlue,upperBlue)

cv2.imshow("Blue Mask",BlueMask)

# ----------- Red Color Mask Creation ----------------
lowerRed=np.array([0,100,100])
upperRed=np.array([20,255,255])
RedMask=cv2.inRange(hsv,lowerRed,upperRed)

cv2.imshow("Red Mask",RedMask)

# ----------- Orange Color Mask Creation ----------------
lowerOrange=np.array([1,190,200])
upperOrange=np.array([18,255,255])
OrangeMask=cv2.inRange(hsv,lowerOrange,upperOrange)

cv2.imshow("Orange Mask",OrangeMask)

# ----------- White Color Mask Creation ----------------
lowerWhite=np.array([0,0,200])
upperWhite=np.array([145,60,255])
WhiteMask=cv2.inRange(hsv,lowerWhite,upperWhite)

cv2.imshow("White Mask",WhiteMask)

# ----------- Green Color Mask Creation ----------------
lowerGreen=np.array([65,60,60])
upperGreen=np.array([80,255,255])
GreenMask=cv2.inRange(hsv,lowerGreen,upperGreen)

cv2.imshow("Green Mask",GreenMask)

# ----------- Yellow Color Mask Creation ----------------
lowerYellow=np.array([20,100,100])
upperYellow=np.array([30,255,255])
YellowMask=cv2.inRange(hsv,lowerYellow,upperYellow)

cv2.imshow("Yellow Mask",YellowMask)

# mask=["RedMask","BlueMask","GreenMask","OrangeMask","WhiteMask","YellowMask"]
# imgMasked=img
# for i in mask:
#     newMask=cv2.bitwise_and(img,img, mask=eval(i))
#     imgMasked=cv2.bitwise_or(imgMasked, newMask)

# cv2.imshow("Mask Image",imgMasked)
cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()



# lower=np.array([110,50,50])
# upper=np.array([130,255,255])

# mask=cv2.inRange(hsv,lower,upper)



# blue
# lowerBlue=np.array([14,99,113])
# upperBule=np.array([158,255,255])
# lowerBlue=np.array([100,50,50])
# upperBlue=np.array([130,255,266])


# red
# lowerRed=np.array([0,118,135])
# upperRed=np.array([95,255,255])
# lowerRed=np.array([0,100,100])
# upperRed=np.array([20,255,255])


# white
# lowerWhite=np.array([0,0,185])
# upperWhite=np.array([174,29,255])
# lowerWhite=np.array([0,0,200])
# upperWhite=np.array([145,60,255])


# yellow
# lowerYellow=np.array([0,187,230])
# upperYellow=np.array([56,255,255])
# lowerYellow=np.array([20,100,100])
# upperYellow=np.array([30,255,255])


# orange
# lowerOrange=np.array([0,172,202])
# upperOrange=np.array([17,255,255])
# lowerOrange=np.array([1,190,200])
# upperOrange=np.array([18,255,255])


# green
# lowerGreen=np.array([35,154,45])
# upperGreen=np.array([94,255,255])
# lowerGreen=np.array([65,60,60])
# upperGreen=np.array([80,255,255])