from PyQt5.QtCore import QPoint
from isin import isIn_angle
import random as rand

import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPoint


def diff(p1: QPoint, p2: QPoint):
    return QPoint(p1.x() - p2.x(), p1.y() - p2.y())

def mul(p1: QPoint, p2: QPoint):
    return p1.x() * p2.y() - p1.y() * p2.x()

class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = MainWindow()
        self.window.show()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("РГР (построение)")
        self.resize(450, 300)
        
        self.setCentralWidget(Field())
      
# область рисования     
class Field(QtWidgets.QLabel):
    def __init__(self, points = None):
        super().__init__()
        self.points = points
        self.count = 0

    def paintEvent(self, event):
        '''отрисовка содержимого QLabel'''
        
        qp = QtGui.QPainter(self)  
        qp.setPen(QtGui.QColor(255,0,0))
    
        self.create_star_polygon(qp)    

    def create_star_polygon(self, qp):
        width = self.size().width() / 2
        height = self.size().height() / 2
        if self.points == None: 
            
            points = [QPoint(rand.randint(-100, 100) + width, 
                            rand.randint(-100, 100) + height) for i in range(10)]     
               
            self.points = points
            for i, p in enumerate(points):
                qp.drawText(p + QPoint(-2, 4), str(i))
                qp.drawEllipse(p, 8, 8)
            
            # соединение точек массива, хранящего вершины звезды
            qp.drawLine(points[0], points[1])
            qp.drawLine(points[2], points[1])
            qp.drawLine(points[0], points[2])
            
            if self.count == 0: print(self.createPolygon(points))
            self.count = 1
        else:
            for i, p in enumerate(self.points):
                qp.drawText(p + QPoint(-2, 4), str(i))
                qp.drawEllipse(p, 8, 8)
         
        # for i in range(1, 2):
        #     qp.drawLine(points[i-1], points[i])
        
    def createPolygon(self, points):    
        n = 3 # начальный треугольник
        p = [points[i] for i in range(3)]
        
        if(mul(diff(p[1], p[0]), diff(p[2], p[1])) < 0):
            # ориентация против часовой стрелки
            p[1], p[2] = p[2], p[1]
               
        self.widget = MyWidget(Field(p))
        for i in range(n, len(points)):
            p = self.insert(points[i], p) # добавление точки
            self.widget.addField(Field(p), str(i))
            
        return points
    
    def insert(self, t, p): # добавление точки
        if isIn_angle(t): return # t принадлежит
        
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
    app = App()
    sys.exit(app.exec())