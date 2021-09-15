# Rubic Cube Detector

## How It Works

It work using command on console specified for each method
In this module it contain Two method gives seperate Output With Different Approach

- _CubeOpt_
- _CubeTrac_

### CubeOpt

```bat

python main.py -co

// or //

python main.py --cubeopt

```

- In this we used Hsv tracking to configer the cube and filtering it through some parameters
- cube Optimisation file contain some functions Within the class eg:
  - `getFilteredCube(self)` _Main Function_
  - `ColorDetection(self, color, hsv_image)` _Supporting Function_
  - `removeBadCont(self, contors)` _Supporting Function_
- This file Gives Output in `output_opt/` file
- Output in form of images with color tag on the center

### CubeTrac

```bat

python main.py -ct

// or //

python main.py --cubetrac

```

- In this we used Canny Edge Detection to configer the cube and filtering it through some parameters
- cube Optimisation file contain some functions Within the class eg:
  - `getTrackedCube(self)` _Main Function_
  - `arrangeCube(self, contors)` _Supporting Function_
- This file Gives Output in `output_trac/` file
- Output in form of Text file contain unique number pattern for color

## For Both Type Of Out Put

```bat

python main.py -ct -co

// or //

python main.py --cubetrac --cubeopt

```

## External Module Used

- <a href="https://opencv.org/" >OpenCv</a>
- <a href="https://opencv.org/" >Numpy</a>
- <a href="https://docs.python.org/3/library/os.html" >OS</a>
- <a href="https://docs.python.org/3/library/argparse.html" >ArgParse</a>

## LICENCE

#### MIT License
