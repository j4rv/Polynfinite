import logging

def logSavedImage(fileName, sizeX, sizeY, oversampling, backgroundColor, polygon, lineWidth, ratio, iterations):
    print("Saved image: " + fileName)

    logging.basicConfig(filename='log.log', level=logging.INFO)
    logging.info('    ----    {filename}    ----    '.format(filename=fileName))
    logging.info('Size: {sizex}x{sizey}.'.format(sizex=sizeX, sizey=sizeY))
    logging.info('Background color: {bgcolor}'.format(bgcolor=backgroundColor))
    logging.info('Oversampling: {oversampling}'.format(oversampling=oversampling))
    logging.info('Polygon used: {polygon}'.format(polygon=polygon))
    logging.info('Line width: {lineWidth}.'.format(lineWidth=lineWidth))
    logging.info('Ratio: {ratio}.'.format(ratio=ratio))
    logging.info('Iterations: {iterations}.'.format(iterations=iterations))
    logging.info('\n')
