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

if __name__ == "__main__":
    pass