import cv2
import numpy as np

class CubeOpt:
    def __init__(self,img):
        self.img=img

    def removeBadCont(self,conts):
        new_conts = []
        for cont in conts:
            bound_rect = cv2.minAreaRect(cont)
            length, breadth = float(bound_rect[1][0]), float(bound_rect[1][1])
            area = cv2.contourArea(cont)
            peri = cv2.arcLength(cont, True)
            poly = cv2.approxPolyDP(cont, 0.1 * peri, True)
            corner = len(poly)
            try:
                if max((length/breadth, breadth/length)) > 5:
                    continue
                if not 0.9*self.img.shape[0] > max((length, breadth)) > 0.05*self.img.shape[0]:
                    continue
                if area/(length*breadth) <0.5:
                    continue
                if corner>4 or corner<2:
                    continue
                if (length * breadth) / area <= 0.8:
                    continue
                if (2 * (length + breadth)) / peri <= 0.8:
                    continue
                new_conts.append(cont)
            except ZeroDivisionError:
                continue
        return new_conts

    def getFilteredCube(self):
        hsv=cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        # ----------- Blue Color Mask Creation ----------------
        BlueMask=self.ColorDetection("Blue", hsv)
        # ----------- Red Color Mask Creation ----------------
        RedMask=self.ColorDetection("Red", hsv)
        # ----------- Orange Color Mask Creation ----------------
        OrangeMask=self.ColorDetection("Orange", hsv)
        # ----------- White Color Mask Creation ----------------
        WhiteMask=self.ColorDetection("White",hsv)
        # ----------- Green Color Mask Creation ----------------
        GreenMask=self.ColorDetection("Green", hsv)
        # ----------- Yellow Color Mask Creation ----------------
        YellowMask=self.ColorDetection("Yellow", hsv)

        result=RedMask | GreenMask | BlueMask | WhiteMask | YellowMask | OrangeMask
        MaskedImg=cv2.bitwise_and(self.img,self.img, mask=result)
        return self.img

    def ColorDetection(self,color,hsv):
        colordict={"Red":[[0, 50, 70],[9, 255, 255],[159, 50, 70],[180, 255, 255],"R"],"Blue":[[90, 50, 70],[128, 255, 255],"B"],"Green":[[36, 50, 70],[89, 255, 255],"G"],"White":[[0, 0, 231],[180, 18, 255],"W"],"Orange":[[10, 50, 70],[24,255,255],"O"],"Yellow":[[ 25, 50,70],[35,255,255],"Y"]}

        if color in colordict:
            if color=="Red":
                lower_l=np.array(colordict[color][0])
                upper_l=np.array(colordict[color][1])
                lower_u=np.array(colordict[color][2])
                upper_u=np.array(colordict[color][3])
                Mask_l=cv2.inRange(hsv,lower_l,upper_l)
                Mask_u=cv2.inRange(hsv,lower_u,upper_u)
                Mask=Mask_l+Mask_u
            else:
                lower=np.array(colordict[color][0])
                upper=np.array(colordict[color][1])
                Mask=cv2.inRange(hsv,lower,upper)
            
            kernel=np.ones((2,2),np.uint8)
            img_Erode=cv2.erode(Mask, kernel,iterations=2)
            img_dilate=cv2.dilate(img_Erode, kernel,iterations=1)

            # Find Canny edges
            edged = cv2.Canny(img_Erode, 20, 200)
            cv2.imshow("contore",edged)
            # Find contours and print how many were found
            # res = cv2.cvtColor((self.img).copy(), cv2.COLOR_BGR2GRAY)
            # ret, thrash = cv2.threshold(res, 40, 255, cv2.THRESH_BINARY)
            # contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            newContor=self.removeBadCont(contours)

            for c in newContor:
                cv2.drawContours(self.img, [c], -1, (0,0,255), 3)  
                M = cv2.moments(c)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                cv2.circle(self.img,(cx,cy), 5, (0,0,255), -1)
                name_col=colordict[color][-1]
                cv2.putText(self.img, name_col, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    
            return img_dilate

        return "Error"

if __name__=="__main__":
    pass