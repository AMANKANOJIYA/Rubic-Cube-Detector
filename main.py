import cv2
import numpy as np 


img= cv2.imread("./input/rc-1.png")
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
original=img.copy()

def empty(a):
    pass

def remove_bad_contours(conts):
        new_conts = []
        for cont in conts:
            bound_rect = cv2.minAreaRect(cont)
            length, breadth = float(bound_rect[1][0]), float(bound_rect[1][1])
            try:
                if max((length/breadth, breadth/length)) > 5:
                    continue
                if not 0.9*img.shape[0] > max((length, breadth)) > 0.05*img.shape[0]:
                    continue
                # if cv2.contourArea(cont)/(length*breadth) <0.4:
                #     continue
##                print length/breadth, cv2.contourArea(cont)/(length*breadth)
                new_conts.append(cont)
            except ZeroDivisionError:
                continue

        return new_conts

def colorDetection(color,image):
    colordict={"Red":[[0, 50, 70],[9, 255, 255],[159, 50, 70],[180, 255, 255],"R"],"Blue":[[90, 50, 70],[128, 255, 255],"B"],"Green":[[36, 50, 70],[89, 255, 255],"G"],"White":[[0, 0, 231],[180, 18, 255],"W"],"Orange":[[10, 50, 70],[24,255,255],"O"],"Yellow":[[ 25, 50,70],[35,255,255],"Y"]}

    if color in colordict:
        if color=="Red":
            lower_l=np.array(colordict[color][0])
            upper_l=np.array(colordict[color][1])
            lower_u=np.array(colordict[color][2])
            upper_u=np.array(colordict[color][3])
            Mask_l=cv2.inRange(image,lower_l,upper_l)
            Mask_u=cv2.inRange(image,lower_u,upper_u)
            Mask=Mask_l+Mask_u
        else:
            lower=np.array(colordict[color][0])
            upper=np.array(colordict[color][1])
            Mask=cv2.inRange(image,lower,upper)
        
        kernel=np.ones((2,2),np.uint8)
        img_Erode=cv2.erode(Mask, kernel,iterations=2)
        img_dilate=cv2.dilate(img_Erode, kernel,iterations=1)


        # Find Canny edges
        edged = cv2.Canny(img_Erode, 20, 200)

        # Find contours and print how many were found
        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        newContor=remove_bad_contours(contours)

        for c in newContor:
            cv2.drawContours(img, [c], -1, (0,0,255), 3)  
            M = cv2.moments(c)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.circle(img,(cx,cy), 5, (0,0,255), -1)
            name_col=colordict[color][-1]
            cv2.putText(img, name_col, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

 
        return img_dilate

    return "Error"


nullarray=np.zeros([img.shape[0],img.shape[1],3])
nullarray2=np.zeros([img.shape[0],img.shape[1],3])
nullarray.fill(255)

# ----------- Blue Color Mask Creation ----------------
BlueMask=colorDetection("Blue", hsv)

# ----------- Red Color Mask Creation ----------------
RedMask=colorDetection("Red", hsv)

# ----------- Orange Color Mask Creation ----------------
OrangeMask=colorDetection("Orange", hsv)

# ----------- White Color Mask Creation ----------------
WhiteMask=colorDetection("White",hsv)

# ----------- Green Color Mask Creation ----------------
GreenMask=colorDetection("Green", hsv)

# ----------- Yellow Color Mask Creation ----------------
YellowMask=colorDetection("Yellow", hsv)


# Adding ALl Masks In ONE 
result=RedMask | GreenMask | BlueMask | WhiteMask | YellowMask | OrangeMask
cv2.imshow("Original",original)
MaskedImg=cv2.bitwise_and(img,img, mask=result)
cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()