import Polynfinite.Colors as Colors
from PIL import Image, ImageDraw


def drawLine(draw, p, p2, width, color):
    draw.line((p[0], p[1], p2[0], p2[1]), fill=color, width=int(width))


def drawAndAddToList(draw, p, p2, list, ratio, width, color):
    drawLine(draw, p, p2, width, color)
    list.append((p[0] * ratio + (1 - ratio) * p2[0], p[1] * ratio + (1 - ratio) * p2[1]))


def polynfinite(sizeX, sizeY, bgColor, poly, ratio, width, n):
    im = Image.new('RGB', (sizeX, sizeY), bgColor)
    draw = ImageDraw.Draw(im)
    _polynfiniteFromPolygonRecursive(draw, poly, ratio, width, n, n)
    return im


def _polynfiniteFromPolygonRecursive(draw, poly, ratio, width, n, maxN):
    firstP = None
    lastP = None
    subPoly = []
    #This controls the colors used for each line
    #TODO: Make it configurable from Options.py
    color = Colors.gradientColor(n, maxN, red="CENTER", green="BORDER", blue=255)

    for p in poly:
        if lastP:
            drawAndAddToList(draw, p, lastP, subPoly, ratio, width, color)
        else:
            firstP = p
        lastP = p
    drawAndAddToList(draw, firstP, lastP, subPoly, ratio, width, color)

    if n > 0:
        _polynfiniteFromPolygonRecursive(draw, subPoly, ratio, width, n - 1, maxN)
