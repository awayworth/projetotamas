import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ThreadBalde import ThreadBalde

class Janela( QWidget ):
    __LEd1 = None
    __PBar=None
    __Bt1 = None
    __MeuBalde=None

    def __init__(self, Str="Janela", x1=400, y1=200, dx=640, dy=480, cor="orange"):
        super().__init__()
        
        self.setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)

        self.inicialize()

    def closeEvent(self, event):
        self.__MeuBalde.parar()
        self.destroy()
        sys.exit(0)
        
    def action_executar(self):
        if not self.__MeuBalde.isRunning():
            self.__MeuBalde.iniciar(5)
            self.__Bt1.setText("Parar")
        else:
            self.__Bt1.setText("Iniciar")
            self.__MeuBalde.parar()

    def inicialize(self):
        Grid = QGridLayout()
        
        self.__PBar = QProgressBar(self)
        self.__PBar.setOrientation(Qt.Vertical)
        self.__PBar.setGeometry(0,0,300,25)
        self.__PBar.setMaximum(100)
        
        self.__LEd1 = QLineEdit()
        self.__Bt1 = QPushButton('Parar')
        
        self.__Bt1.clicked.connect(self.action_executar)

        Grid.addWidget(self.__PBar, 0, 0, 4, 1)
        Grid.addWidget(self.__LEd1, 1, 1, 1 ,1)
        Grid.addWidget(self.__Bt1, 2, 1, 1, 1)
        
        self.__MeuBalde=ThreadBalde(self.__LEd1, self.__PBar)

        self.setLayout(Grid)
        self.show()

