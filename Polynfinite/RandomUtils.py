import string
from secrets import randbelow, choice

def randomFilename():
    return ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(8)) + ".png"

def randomPolygon(minVertices, maxVertices, sizeX, sizeY):
    res = []
    nVertices = randomRange(minVertices, maxVertices)
    for _ in range (0, nVertices):
        res.append((randomRange(-sizeX, sizeX * 2), randomRange(-sizeY, sizeY * 2)))
    return res

def randomRange(minimum, maximum):
    return randbelow(maximum - minimum) + minimum