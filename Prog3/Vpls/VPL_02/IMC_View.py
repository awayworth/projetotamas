import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class View( QWidget ):
    __Lb_peso = None
    __Lb_altura = None
    __Lb_imc = None
    __Lb_classif = None
    __LEd_peso = None
    __LEd_altura = None
    __LEd_imc = None
    __LEd_classif = None
    __Bt_calc = None
    __Cntr = None

    def __init__(self,Cntr,Str="Janela"):
        super().__init__()
        self.setWindowTitle(Str)
        self.__Cntr=Cntr
        self.setGeometry(520, 280, 10, 10)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('orange'))
        self.setPalette(p)

        self.inicialize()

    def closeEvent(self, event):

        print("Destruindo janela...")
        self.destroy()
        sys.exit(0)

    def get_Peso(self):
        return (self.__LEd_peso.text())

    def get_Altura(self):
        return (self.__LEd_altura.text())

    def set_imc(self, imc):
        self.__LEd_imc.setText("%5.2f" % imc)

    def set_classif(self,classificacao):
        self.__LEd_classif.setText(classificacao)

    def action_Bt_calc(self):

        self.__Cntr.action_Calcular()

    def show_error(self, Erro):

        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Erro")
        error_box.setText(Erro)
        error_box.exec_()

    def inicialize(self):
        Grid=QGridLayout()

        self.__Lb_peso=QLabel(self, text="Peso:", width=12)
        self.__Lb_altura=QLabel(self, text="Altura:", width=12)
        self.__Lb_imc=QLabel(self, text="IMC:", width=12)
        self.__Lb_classif=QLabel(self, text="Classificação:", width=12)
        
        self.__LEd_peso=QLineEdit(self, width=28)
        self.__LEd_altura=QLineEdit(self, width=28)
        self.__LEd_imc=QLineEdit(self, width=28)
        self.__LEd_classif=QLineEdit(self, width=28)

        self.__Bt_calc=QPushButton(self, text='Calcular')

        self.__Bt_calc.clicked.connect(self.action_Bt_calc)
        
        Grid.addWidget(self.__Lb_peso, 0, 0)
        Grid.addWidget(self.__Lb_altura, 1, 0)
        Grid.addWidget(self.__Lb_imc, 3, 0)
        Grid.addWidget(self.__Lb_classif, 4, 0)
        
        Grid.addWidget(self.__LEd_peso, 0, 1, 1, 1)
        Grid.addWidget(self.__LEd_altura, 1, 1, 1, 1)
        Grid.addWidget(self.__LEd_imc, 3, 1, 1, 1)
        Grid.addWidget(self.__LEd_classif, 4, 1, 1, 1)
        
        Grid.addWidget(self.__Bt_calc, 2, 0)

        self.setLayout(Grid)
        self.show()

