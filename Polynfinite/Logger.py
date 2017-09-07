import logging


logging.basicConfig(filename='log.log', level=logging.INFO, format="[%(levelname)s]: %(message)s")
def logSavedImage(fileName, sizeX, sizeY, oversampling, backgroundColor, polygon, lineWidth, ratio, iterations):
    print("Saved image: " + fileName)

    logging.info('    ----    {filename}    ----    '.format(filename=fileName))
    logging.info('Size: {sizex}x{sizey}'.format(sizex=sizeX, sizey=sizeY))
    logging.info('Background color: {bgcolor}'.format(bgcolor=backgroundColor))
    logging.info('Oversampling: {oversampling}'.format(oversampling=oversampling))
    logging.info('Polygon used: {polygon}'.format(polygon=polygon))
    logging.info('Line width: {lineWidth}'.format(lineWidth=int(lineWidth)))
    logging.info('Ratio: {ratio}'.format(ratio=ratio))
    logging.info('Iterations: {iterations}\n'.format(iterations=iterations))
