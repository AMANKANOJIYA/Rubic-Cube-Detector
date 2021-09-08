import CubeOpt as co
import cv2
import os

input_list=os.listdir(f"{os.getcwd()}\input_images\\")
for i in input_list:
    img=cv2.imread(f"./input_images/{i}")
    sample=co.CubeOpt(img)
    cv2.imshow("On test page", sample.getFilteredCube())
    cv2.waitKey(0)
    cv2.imwrite(f"{os.getcwd()}\output_opt\\{i}", img)
    cv2.destroyAllWindows()