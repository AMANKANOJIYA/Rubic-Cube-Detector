import main as cn
import cv2
import os

input_list=os.listdir(f"{os.getcwd()}\input\\")
for i in input_list:
    img=cv2.imread(f"./input/{i}")
    sample=cn.CubeOpt(img)
    cv2.imshow("On test page", sample.getFilteredCube())
    cv2.waitKey(0)
    cv2.imwrite(f"{os.getcwd()}\output\\{i}", img)
    cv2.destroyAllWindows()