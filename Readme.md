# Rubic Cube Color Detector (RealTime)

## How It Works 
In this module it contain Two method gives seperate Output With Different Approach
- *CubeOpt*
- *CubeTrac*

### CubeOpt
- In this we used Hsv tracking to configer the cube and filtering it through some parameters
- cube Optimisation file contain some functions Within the class eg: 
  - ` getFilteredCube(self) ` Main Function
  - ` ColorDetection(self, color, hsv_image) ` Main Function
  - ` removeBadCont(self, contors) ` Main Function
- This file Gives Output in `output_opt/` file 
- Output in form of images with color tag on the center

### CubeTrac
<!-- - In this we used Hsv tracking to configer the cube and filtering it through some parameters
- cube Optimisation file contain some functions Within the class eg: 
  - ` getFilteredCube(self) ` Main Function
  - ` ColorDetection(self, color, hsv_image) ` Main Function
  - ` removeBadCont(self, contors) ` Main Function -->
- This file Gives Output in `output_trac/` file 


## OpenCV Image

- Red , Orange , Yellow , Green , Blue , White
- RUbic Cube detection and adding color name at the center of Each color

## How to Use ??

Put all the Files in Input Folder No specific File name Required
It will Give You out put at Output Folder In Image FORMAT
You can find it using following Format <Filename>\_Output.<Extenction>
