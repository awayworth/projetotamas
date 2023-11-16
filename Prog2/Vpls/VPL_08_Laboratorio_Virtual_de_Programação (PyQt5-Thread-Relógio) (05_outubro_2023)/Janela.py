import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *  # Questão 06
from ThreadClock import ThreadClock

class Janela(QWidget):  # Questão 07
    __Lb1 = None
    __LEd1 = None
    __Bt1 = None
    __MeuRelogio=None

    def __init__(self, Str="Janela", x1=400, y1=200, dx=640, dy=480, cor="orange"):  # Questão 08
        super().__init__()
        

        self.setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)

        
        self.inicialize()

    def closeEvent(self, event):  # Questão 09
        
        self.__MeuRelogio.parar()
        self.destroy()
        sys.exit(0)

    def action_executar(self):  # Questão 10
        if not self.__MeuRelogio.isRunning():
            self.__MeuRelogio.iniciar(3000)
            self.__Bt1.setText("Parar")
        else:
            self.__Bt1.setText("Iniciar")
            self.__MeuRelogio.parar()

    def inicialize(self):
        Grid = QGridLayout()

        # Questão 11
        self.__Lb1 = QLabel('Hora:')
        self.__LEd1 = QLineEdit()
        self.__Bt1 = QPushButton('Iniciar')

        # Questão 12
        self.__Bt1.clicked.connect(self.action_executar)

        # Questão 13
        Grid.addWidget(self.__Lb1, 0, 0)
        Grid.addWidget(self.__LEd1, 0, 1, 1 ,2)
        Grid.addWidget(self.__Bt1, 1, 1)
        
        self.__MeuRelogio = ThreadClock(self.__LEd1)
        self.setLayout(Grid)
        self.show()
