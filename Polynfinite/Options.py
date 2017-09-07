import sys
from Polynfinite import Colors

#Image options
FINAL_SIZE_X = 1920
FINAL_SIZE_Y = 1080
OVERSAMPLING = 2                    #For smoother results (without aliasing).
BACKGROUND_COLOR = Colors.BLACK
IMAGES_TO_CREATE = 6
SAVE_FOLDER = "./renders/"

#Polygon options
LINE_WIDTH = OVERSAMPLING           #Integer numbers only.
RATIO = 0.01                        #From zero to one.
ITERATIONS = 100
MIN_VERTICES = 3
MAX_VERTICES = 6