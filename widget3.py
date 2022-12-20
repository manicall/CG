from PyQt5.QtCore import QPoint
from isin import diff, isIn_hLine, mul
from star import innerPolygons
import numpy as np
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPoint

class Widget3(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
                
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(Field())
        
        self.setLayout(layout)
      
# область рисования     
class Field(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.hasPoints = False
        
    def paintEvent(self, event):
        '''отрисовка содержимого QLabel'''
        qp = QtGui.QPainter(self)  
        qp.setPen(QtGui.QColor(255,0,0))
           
        self.createPolygon(qp)
    
    def createPolygon(self, qp):
        width = self.size().width() // 2
        height = self.size().height() // 2
        
        if not self.hasPoints:
            self.points = innerPolygons(width, height, 10)
            H = self.jarvismarch(self.points)
            
            self.hasPoints = True
        
        j = len(H) - 1
        for i in range(len(H)):    
            qp.drawLine(self.points[H[i]], self.points[H[j]])
            j = i
                
    # метод заворачивания подарка
    def jarvismarch(self, points):
        A = [[p.x(), p.y()] for p in points]
        
        n = len(A)
        P = [*range(n)]
        # start point
        for i in range(1,n):
            if A[P[i]][0]<A[P[0]][0]: 
                P[i], P[0] = P[0], P[i]  
        H = [P[0]]
        del P[0]
        P.append(H[0])
        while True:
            right = 0
            for i in range(1,len(P)):
                if rotate(A[H[-1]],A[P[right]],A[P[i]])<0:
                    right = i
            if P[right]==H[0]: 
                break
            else:
                H.append(P[right])
            del P[right]
        return H

def rotate(A,B,C):
    return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

if __name__ == "__main__":
    pass