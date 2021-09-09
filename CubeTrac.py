import cv2
import numpy as np
'''
Works On Canny edge detection method

WorkFlow :
getTrackedCube() ---> arrangeCube() ---> getTrackedCube()
'''
class CubeTrac:
    def __init__(self, img):
        '''
        Image Configuration
        '''
        self.img=img
    
    def getTrackedCube(self):
        '''
        Image Operation and color number assigning
        '''
        # Convert to graycsale
        img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        # Blur the image for better edge detection
        img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
         # Canny Edge Detection
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
        #Geting Contores
        contours, h = cv2.findContours(edges, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        #Arrange Cube and Creating color arrangement
        color_store = self.arrangeCube(contours)

        #Mapping
        maping,counter,text,pattern={},1,"",1
        for color in color_store:
            if str(color) in maping.values():
                text+=str(list(maping.keys())[list(maping.values()).index(str(color))])+" "
            else:
                maping[counter]=str(color)
                text+=str(counter)+" "
                counter += 1
            if pattern % 3 == 0:
                text+="\n"
            pattern+=1
        return text[:-1]

    def arrangeCube(self, contours):
        '''
        Arrange the Contore in proper Order
        '''
        main=[]
        for i in contours:
            M = cv2.moments(i)
            try:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01'] / M['m00'])
            except ZeroDivisionError:
                continue
            main.append([cy,cx,i])
        main=sorted(main)
        general,calc=[],3
        for j in range(0,len(main),3):
            coo=sorted(main[j:calc], key=lambda x: x[1])
            general+=coo
            calc+=3
        color_store=[]
        for j in general:
            color_store+=[list(self.img[j[0],j[1]])]
            cv2.drawContours(self.img, [j[-1]], -1, (0,0,0), thickness = 5)
        return color_store


if __name__ == "__main__":
    cv2.waitKey(0)
    cv2.destroyAllWindows()