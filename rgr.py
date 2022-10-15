import sys
from widget1 import Widget1
from widget2 import Widget2
from widget3 import Widget3
from PyQt5 import QtWidgets

class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = MainWindow()
        self.window.show()
        
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вычислительная геометрия")
        self.resize(450, 300)
        
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        
        self.tab = QtWidgets.QTabWidget()
        self.tab.addTab(Widget1(self.statusBar), "Звездчатый многоугольник")
        self.tab.addTab(Widget2(self.statusBar), "Проверка на принадлежность")
        self.tab.addTab(Widget3(), "прямоугольник методом дейкстры")
        
        self.tab.currentChanged.connect(self.on_tabBarClicked)
        
        self.setCentralWidget(self.tab)
        
    def on_tabBarClicked(self):
        try:
            self.tab.currentWidget().setStatusBar(self.statusBar)
        except AttributeError:
            pass     
      
if __name__ == "__main__":
    app = App()
    sys.exit(app.exec())
    