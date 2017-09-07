import random

BLACK = (0,0,0)
WHITE = (255,255,255)

def gradientColor(currentIteration, maxIteration, red="255", green="255", blue="255"):
    bnColor = int((maxIteration - currentIteration) * 255.0 / maxIteration)
    return (_valueToGradientValue(red, bnColor), _valueToGradientValue(green, bnColor), _valueToGradientValue(blue, bnColor))


def randomColor(n):
    red = random.randrange(0,255)
    green = random.randrange(0,255)
    blue = random.randrange(0,255)
    color = (red, green, blue)
    return color

def _valueToGradientValue(value, bnColor):
    if value is "CENTER":
        return bnColor
    if value is "EXTERIOR" or "BORDER":
        return 255 - bnColor
    if value is int:
        result = max(0,min(255, value))
        return result