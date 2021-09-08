# File Import
import cv2
import os
import CubeOpt as co
import CubeTrac as ct
import argparse

# Setting Up Arg Parser
parser = argparse.ArgumentParser(description="Rubic Cube Color Detection With 2 Different method")
parser.add_argument("-co","--cubeopt",action="store_true", help="Detection using Cube Optimisation method (HSV Detection)") 
parser.add_argument("-ct","--cubetrac",action="store_true", help="Detection using CubeTracking method (Cannry Detection)") 
args = parser.parse_args()
dict_args = vars(args)

# Get List of file name from specific file 
input_list = os.listdir(f"{os.getcwd()}\input_images\\")

# Main function to get output as per argument
def main(cubeopt=False, cubetrac=False):
    if cubeopt:
       for i in input_list:
            name = i.split(".")[0]
            img = cv2.imread(f"./input_images/{i}")
            sample = co.CubeOpt(img)
            sample.getFilteredCube()
            print(name)
            cv2.imwrite(f"{os.getcwd()}\output_opt\\output_{name}.jpg", img)
    if cubetrac:
        for i in input_list:
            name = i.split(".")[0]
            img=cv2.imread(f"./input_images/{i}")
            sample = ct.CubeTrac(img)
            text = sample.getTrackedCube()
            print(text)
            with open(f"{os.getcwd()}\output_trac\\output_{name}", "w") as file:
                file.write(text)
    return True

# Main Function Call 
main(dict_args["cubeopt"],dict_args["cubetrac"])
cv2.destroyAllWindows()

if __name__ == "__main__":
    pass