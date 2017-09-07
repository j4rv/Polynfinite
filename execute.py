from Polynfinite.Drawer import polynfinite
from Polynfinite import Logger
from Polynfinite.RandomUtils import randomFilename, randomPolygon
from Polynfinite.Options import *
from PIL import Image


_SIZE_X = FINAL_SIZE_X * OVERSAMPLING
_SIZE_Y = FINAL_SIZE_Y * OVERSAMPLING
sys.setrecursionlimit(10000) #To allow a high number of iterations.


for _ in range(IMAGES_TO_CREATE):
    fileName = randomFilename()
    polygon = randomPolygon(MIN_VERTICES, MAX_VERTICES, _SIZE_X, _SIZE_Y)
    image = polynfinite(_SIZE_X, _SIZE_Y, BACKGROUND_COLOR, polygon, RATIO, LINE_WIDTH, ITERATIONS)

    if OVERSAMPLING != 1:
        image = image.resize((FINAL_SIZE_X, FINAL_SIZE_Y), resample=Image.BICUBIC)

    image.save(SAVE_FOLDER + fileName, "PNG")
    Logger.logSavedImage(fileName, FINAL_SIZE_X, FINAL_SIZE_Y, OVERSAMPLING, BACKGROUND_COLOR, polygon, LINE_WIDTH, RATIO, ITERATIONS)