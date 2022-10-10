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
            self.points = [p for row in self.points for p in row]
            self.points = self.getPolygonPoints(self.points)
            
            self.hasPoints = True
        
        #for k in self.points:
        j = len(self.points) - 1
        for i in range(len(self.points)):   
            qp.drawLine(self.points[i], self.points[j])
            j = i
                
    # метод дейкстры
    def getPolygonPoints(self, points):    
        n = 3 # начальный треугольник
        p = [points[i] for i in range(3)]
        
        if(mul(diff(p[1], p[0]), diff(p[2], p[1])) < 0):
            # ориентация против часовой стрелки
            p[1], p[2] = p[2], p[1]
               
        for i in range(n, len(points)):
            p = self.insert(points[i], p) # добавление точки
            
        return p
    
    def insert(self, t, p): # добавление точки
        if isIn_hLine(p, t): return p # t принадлежит
        
        n = len(p)
        del1 = [0 for i in range(n)]  # n – число вершин
        q = [QPoint() for i in range(n + 1)]  # формируемый многоугольник

        for i in range(n):
            if(mul(diff(t, p[i]), (diff(p[(i + 1)%n], p[i]))) >= 0):
                del1[i] = 1 # отмечаем видимые стороны
            else:
                del1[i] = 0
        
        for i in range(n):
            if(del1[i] == 1 and del1[(i + 1)%n] == 0): break
        j = 0
        i = (i + 1)%n # i – номер последней
        # невидимой стороны
        while del1[i] == 0:
            q[j] = p[i]
            j += 1
            i = (i + 1)%n #  перепись вершин
            if j == n + 1: return p 
        
        q[j] = p[i]
        q[j + 1] = t # добавление вершин

        p = [QPoint for i in range(j + 2)] 
        n = j + 2
        for i in range(n):
            p[i] = q[i]
        
        return p
  
if __name__ == "__main__":
    pass