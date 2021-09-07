import cv2
import numpy as np

img=cv2.imread(".\input\\rc-2.png")
# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
contours, h = cv2.findContours(edges, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
main=[]

for i in contours:
    M = cv2.moments(i)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    main.append([cy,cx,i])
main=sorted(main)
general,calc=[],3
for j in range(0,len(main),3):
    coo=sorted(main[j:calc], key=lambda x: x[1])
    general+=coo
    calc+=3
color_store=[]
for j in general:
    color_store+=[list(img[j[0],j[1]])]
    cv2.drawContours(img, [j[-1]], -1, (0,0,255), thickness = 5)
    cv2.imshow("image",img)
    cv2.waitKey(0)
maping,counter={},1
for color in color_store:
    if str(color) in maping.values():
        print(list(maping.keys())[list(maping.values()).index(str(color))],end="-")
    else:
        maping[counter]=str(color)
        print(counter,end="-")
        counter+=1
print("\n",maping)


cv2.waitKey(0)
cv2.destroyAllWindows()

