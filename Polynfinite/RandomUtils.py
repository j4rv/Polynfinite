import random
import string

def randomFilename():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)) + ".png"

def randomPolygon(minVertices, maxVertices, sizeX, sizeY):
    res = []
    nVertices = random.randrange(minVertices, maxVertices)
    for i in range (0, nVertices):
        res.append((random.randrange(-sizeX, sizeX * 2), random.randrange(-sizeY, sizeY * 2)))
    return res