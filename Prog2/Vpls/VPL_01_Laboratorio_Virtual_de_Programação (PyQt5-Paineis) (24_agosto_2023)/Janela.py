import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Janela(QWidget):
    __Lb_Nome = None
    __Lb_Telefone = None    
    __Lb_Email = None
    __Lb_Endereco = None
    __LEd_Nome = None
    __LEd_Telefone = None
    __LEd_Email = None
    __LEd_Endereco = None

    def __init__(self, Str="Janela"):
        super().__init__()
        self.setWindowTitle(Str)
        self.setGeometry(400, 200, 456, 280)
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("orange"))
        self.setPalette(p)
        
        self.inicialize()

    def closeEvent(self, event):
        self.destroy()
        sys.exit(0)

    def inicialize(self):
        Grid=QGridLayout()
        
        self.__Lb_Nome = QLabel(self, text="Nome:")
        self.__Lb_Telefone = QLabel(self, text="Telefone:")
        self.__Lb_Email = QLabel(self, text="Email:")
        self.__Lb_Endereco = QLabel(self, text="Endereço:")
        self.__LEd_Nome = QLineEdit(self, width=42)
        self.__LEd_Telefone = QLineEdit(self, width=42)
        self.__LEd_Email = QLineEdit(self, width=42)
        self.__LEd_Endereco = QLineEdit(self, width=42)
        
        Grid.addWidget(self.__Lb_Nome,0,0,1,1)
        Grid.addWidget(self.__Lb_Telefone,1,0,1,1)
        Grid.addWidget(self.__Lb_Email,2,0,1,1)
        Grid.addWidget(self.__Lb_Endereco,3,0,1,1)
        
        Grid.addWidget(self.__LEd_Nome,0,1,1,1)
        Grid.addWidget(self.__LEd_Telefone,1,1,1,1)
        Grid.addWidget(self.__LEd_Email,2,1,1,1)
        Grid.addWidget(self.__LEd_Endereco,3,1,1,1)
        
        self.setLayout(Grid)
        self.show()

