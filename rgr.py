import sys
import numpy as np
from widget1 import Widget1

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QSlider

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
        
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.setCentralWidget(Widget1(self.statusBar))      
      
if __name__ == "__main__":
    app = App()
    sys.exit(app.exec())