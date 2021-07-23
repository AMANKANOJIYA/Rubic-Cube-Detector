import cv2
import numpy as np 


img= cv2.imread("./input/rubic cube-6.jpg")
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def empty(a):
    pass

def colorDetection(color,image):
    
    colordict={"Red":[[0,100,20],[5,255,255],[160,100,20],[179,255,255],"R"],"Blue":[[85,50,70],[140,255,220],"B"],"Green":[[50,100,100],[ 90,255,240],"G"],"White":[[ 0,  0, 120],[255, 50,255],"W"],"Orange":[[5,100,20],[28,255,255],"O"],"Yellow":[[ 25, 80,150],[40,255,255],"Y"]}

    if color in colordict:
        if color=="Red":
            print(color)
            lower_l=np.array(colordict[color][0])
            upper_l=np.array(colordict[color][1])
            lower_u=np.array(colordict[color][2])
            upper_u=np.array(colordict[color][3])
            Mask_l=cv2.inRange(image,lower_l,upper_l)
            Mask_u=cv2.inRange(image,lower_u,upper_u)
            Mask=Mask_l+Mask_u
        else:
            print(color)
            lower=np.array(colordict[color][0])
            upper=np.array(colordict[color][1])
            Mask=cv2.inRange(image,lower,upper)
        
        kernel=np.ones((2,2),np.uint8)
        img_Erode=cv2.erode(Mask, kernel,iterations=2)
        img_dilate=cv2.dilate(img_Erode, kernel,iterations=1)
        cv2.imshow("Dilated Image",img_dilate)
        # ------------------------------------------------------------------------------------------------
        # Find Canny edges
        edged = cv2.Canny(img_Erode, 20, 200)
        cv2.imshow('1 - Canny Edges', edged)
        # cv2.waitKey(0)


        # Find contours and print how many were found
        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        #Draw all contours
        # cv2.drawContours(img_dilate, contours, -1, (0,255,0), 3)
        # cv2.imshow('2 - All Contours over blank image', img_dilate)
        # cv2.waitKey(0)


        for c in contours:
            # Calculate accuracy as a percent of the contour perimeter
            accuracy = 0.03 * cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, accuracy, True)
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
            cv2.imshow('Approx Poly DP', image)

        # ------------------------------------------------------------------------------------------------
        # cv2.imshow("Mask", Mask)
        # cv2.imshow("img_Erode", img_Erode)
        # cv2.imshow("img_dilate", img_dilate)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return img_dilate

    return "Error"


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

nullarray=np.zeros([img.shape[0],img.shape[1],3])
nullarray2=np.zeros([img.shape[0],img.shape[1],3])
nullarray.fill(255)

# ----------- Blue Color Mask Creation ----------------
# lowerBlue=np.array([100,50,50])
# upperBlue=np.array([130,255,266])
# BlueMask=cv2.inRange(hsv,lowerBlue,upperBlue)
BlueMask=colorDetection("Blue", hsv)

# cv2.imshow("Blue Mask",BlueMask)

# ----------- Red Color Mask Creation ----------------
# lowerRed=np.array([0,118,135])
# upperRed=np.array([95,255,255])
# RedMask=cv2.inRange(hsv,lowerRed,upperRed)
RedMask=colorDetection("Red", hsv)

# cv2.imshow("Red Mask",RedMask)

# ----------- Orange Color Mask Creation ----------------
# lowerOrange=np.array([1,190,200])
# upperOrange=np.array([18,255,255])
# OrangeMask=cv2.inRange(hsv,lowerOrange,upperOrange)
OrangeMask=colorDetection("Orange", hsv)

# cv2.imshow("Orange Mask",OrangeMask)

# ----------- White Color Mask Creation ----------------
# lowerWhite=np.array([0,0,168])
# upperWhite=np.array([172,111,255])
# WhiteMask=cv2.inRange(hsv,lowerWhite,upperWhite)
WhiteMask=colorDetection("White",hsv)

# cv2.imshow("White Mask",WhiteMask)

# ----------- Green Color Mask Creation ----------------
# lowerGreen=np.array([65,60,60])
# upperGreen=np.array([80,255,255])
# GreenMask=cv2.inRange(hsv,lowerGreen,upperGreen)
GreenMask=colorDetection("Green", hsv)

# cv2.imshow("Green Mask",GreenMask)

# ----------- Yellow Color Mask Creation ----------------
# lowerYellow=np.array([20,100,100])
# upperYellow=np.array([30,255,255])
# YellowMask=cv2.inRange(hsv,lowerYellow,upperYellow)
YellowMask=colorDetection("Yellow", hsv)

# cv2.imshow("Yellow Mask",YellowMask)


# Adding ALl Masks In ONE 
result=RedMask | GreenMask | BlueMask | WhiteMask | YellowMask | OrangeMask
# cv2.imshow("Resultmask",result)

MaskedImg=cv2.bitwise_and(img,img, mask=result)
cv2.imshow(" Masked Image",MaskedImg)
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
# lower_white = np.array([0,0,168])
# upper_white = np.array([172,111,255])


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



color_lims = {'G':(( 50,100,100),( 90,255,240)), 'R':((170,110,110),(10,255,155)),
              'W':((  0,  0, 120),(255, 50,255)), 'Y':(( 11, 80,150),( 40,255,255)),
              'B':(( 95,60,70),(120,255,220)), 'O':((175, 180, 155),(10,255,255))}

