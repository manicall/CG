import numpy as np
from PyQt5.QtCore import QPoint

def getStar(startX, startY,
            innerRadius, outerRadius,
            numRays, startAngleR = 0):
    deltaAngleR = np.pi / numRays
    points = []

    for i in range(numRays * 2):
        angleR = startAngleR + i * deltaAngleR 
        ca = np.cos(angleR)
        sa = np.sin(angleR)
        relX = ca
        relY = sa
        if i & 1 == 0:
            relX *= outerRadius
            relY *= outerRadius
        else:
            relX *= innerRadius
            relY *= innerRadius

        points.append(QPoint(relX + startX, relY + startY))
        
    return points      

def getRegularPolygon(startX, startY, radius, num):
    deltaAngleR = np.pi / num
    points = []

    for i in range(num):
        angleR = 2 * i * deltaAngleR
        ca = np.cos(angleR)
        sa = np.sin(angleR)
        relX = ca
        relY = sa

        relX *= radius
        relY *= radius
            
        points.append(QPoint(int(relX + startX), int(relY + startY)))
        
    return points      
    

def innerPolygons(width, height, numOfPolygons):
    points = []
    
    r = 10
    n = 3
    
    for i in range(numOfPolygons):
        points.extend(getRegularPolygon(width, height, r, n))
        r += 10
        n += 1

    return points

if __name__ == "__main__":
    pass