import sys
import numpy as np

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QSlider
from star import getStar

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
        
        main_layout = QtWidgets.QVBoxLayout()
        hBox = QtWidgets.QHBoxLayout()
        
        sliderKeys = ('r', 'R', 'n')
        self.sliders = {key : QSlider(Qt.Orientation.Horizontal) 
                        for key in sliderKeys}
        
        min, max = 1, 100
        for slider, label in zip(self.sliders.values(), sliderKeys):
            slider.setRange(min, max)
            slider.valueChanged.connect(self.on_SliderValueChanged)
            hBox.addWidget(QtWidgets.QLabel(label))
            hBox.addWidget(slider)

        self.field = Field(self.sliders)
        
        main_layout.addLayout(hBox)
        main_layout.addWidget(self.field)
        
        widget = QtWidgets.QWidget()
        widget.setLayout(main_layout)
        
        self.statusBar = QtWidgets.QStatusBar()
       
        self.params = {label : QtWidgets.QLabel(f'{label}: {slider.value()}')
                       for label, slider in self.sliders.items()}
        
        for label in sliderKeys:
            self.statusBar.addWidget(self.params[label])
              
        self.setStatusBar(self.statusBar)
        self.setCentralWidget(widget)
    
    def on_SliderValueChanged(self):
        for label, slider in self.sliders.items():
            self.params[label].setText(f"{label}: {slider.value()}")
            
        self.field.update()   
    
# область рисования     
class Field(QtWidgets.QLabel):
    def __init__(self, sliders):
        super().__init__()
        self.sliders = sliders
        
    def paintEvent(self, event):
        '''отрисовка содержимого QLabel'''
        qp = QtGui.QPainter(self)
        self.create_star_polygon(qp)    

    def create_star_polygon(self, qp):
        width = self.size().width() / 2
        height = self.size().height() / 2
        
        r = self.sliders['r'].value()
        R = self.sliders['R'].value()
        n = self.sliders['n'].value()
        p = getStar(width, height, r, R, n)
        
        # соединение точек массива, хранящего вершины звезды
        qp.drawLine(p[0], p[-1])
        for i in range(1, len(p)):
            qp.drawLine(p[i-1], p[i])
        
if __name__ == "__main__":
    app = App()
    sys.exit(app.exec())