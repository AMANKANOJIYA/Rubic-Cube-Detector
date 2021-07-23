import cv2
import numpy as np

# color_lims = {'G':(( 50,100,100),( 90,255,240)), 'R':((170,110,110),(10,255,155)),
#               'W':((  0,  0, 120),(255, 50,255)), 'Y':(( 11, 80,150),( 40,255,255)),
#               'B':(( 95,60,70),(120,255,220)), 'O':((175, 180, 155),(10,255,255))}


color_lims = {"Red":[[170,110,110],[10,255,155],"R"],"Blue":[[100,50,50],[130,255,266],"B"],"Green":[[65,60,60],[80,255,255],"G"],"White":[[0,0,168],[172,111,255],"W"],"Orange":[[1,190,200],[18,255,255],"O"],"Yellow":[[20,100,100],[30,255,255],"G"]}

def detectSquare(img,color):
    img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    color_lim = color_lims[color]
    
    # if color in 'RO':
    #     big_hue = max((color_lim[0][0], color_lim[1][0]))
    #     small_hue = min((color_lim[0][0], color_lim[1][0]))
    #     lower_red = [(0, color_lim[0][1], color_lim[0][2]), (small_hue, color_lim[1][1], color_lim[1][2])]
    #     upper_red = [(big_hue, color_lim[0][1], color_lim[0][2]), (180, color_lim[1][1], color_lim[1][2])]
    #     mask = cv2.inRange(img, upper_red[0], upper_red[1])|cv2.inRange(img, lower_red[0], lower_red[1])
    # else:
    print(color_lim[0], color_lim[1])
    mask = cv2.inRange(img, np.array(color_lim[0]), np.array(color_lim[1]))

    # if smoothed:
    # kernel = np.ones(tuple([DS_MORPH_KERNEL_SIZE]*2))
    mask = cv2.erode(mask, mask, iterations=1)
    mask = cv2.dilate(mask, mask, iterations=1) 

    # if DEBUG_SHOW_MASK:
    #     mshow([mask], [color_name + ' mask in function'])

    return mask

img= cv2.imread("./input/rubic cube-7.jpeg")
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
disp_im = np.array(img)
for color in color_lims:
    sq = detectSquare(img, color)
    cv2.imshow(f" new {color}",sq)
    cv2.imshow(f"Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()