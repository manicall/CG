from PyQt5.QtCore import QPoint
from isin import isIn_angle, isIn_hLine, mul, diff
import random as rand

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPoint

class Widget2(QtWidgets.QWidget):
    def __init__(self, statusBar):
        super().__init__()
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(Field(statusBar))
        
        self.setLayout(layout)
      
# область рисования     
class Field(QtWidgets.QLabel):
    def __init__(self, statusBar):
        super().__init__()
        self.statusBar = statusBar
        self.message = QtWidgets.QLabel()
        self.statusBar.addWidget(self.message)
        self.hasPoints = False
    
    def paintEvent(self, event):
        '''отрисовка содержимого QLabel'''
        qp = QtGui.QPainter(self)  
        qp.setPen(QtGui.QColor(255,0,0))
           
        self.createPolygon(qp)
    
    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        print(QPoint(ev.x(), ev.y()))
    
        self.message.setText(self.getMessage(QPoint(ev.x(), ev.y())))
            
        return super().mousePressEvent(ev)

    def getMessage(self, p):
        text = ""
        if isIn_angle(self.points, p):
            text = "Точка входит в многоугольник"
        else:
            text = "Точка НЕ входит в многоугольник"
        return text

    def createPolygon(self, qp):
        width = self.size().width() // 2
        height = self.size().height() // 2
        
        if not self.hasPoints:
            self.points = [QPoint(rand.randint(-100, 100) + width, 
                                rand.randint(-100, 100) + height) for i in range(10)]
            
            self.points = self.getPolygonPoints(self.points)
            
            self.hasPoints = True
            
        qp.drawLine(self.points[0], self.points[-1])
        for i in range(1, len(self.points)):
            qp.drawLine(self.points[i-1], self.points[i])
                
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
        if isIn_angle(p, t): return p # t принадлежит
        
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
      
class MyWidget(QtWidgets.QWidget):
    def __init__(self, field, title = "default"):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(450, 300)
        self.tab = QtWidgets.QTabWidget() 
        layout = QtWidgets.QVBoxLayout()
        
        self.tab.addTab(field, "1")
        
        layout.addWidget(self.tab)
        self.setLayout(layout)
        self.show()
        
    def addField(self, field, str):
        self.tab.addTab(field, str)
      
if __name__ == "__main__":
    pass