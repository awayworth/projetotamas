import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Janela(QWidget):
    __Lb_valor1 = None
    __Lb_valor2=None
    __Lb_result=None
    __LEd_valor1=None
    __LEd_valor2=None
    __LEd_result=None
    __Bt_adic=None
    __Bt_sub=None
    __Bt_mult=None
    __Bt_div=None

    def __init__(self, Str="Janela"):
        super().__init__()
        self.setWindowTitle(Str)
        self.setGeometry(400, 200, 456, 200)
        
        self.setAutoFillBackground(True)
        p=self.palette()
        p.setColor(self.backgroundRole(), QColor("orange"))
        self.setPalette(p)
        
        self.inicialize()
        
    def closeEvent(self, event):

        self.destroy()
        sys.exit(0)
        
    def action_Bt_adic(self):

        try:
            v1 = float(self.__LEd_valor1.text())
            v2 = float(self.__LEd_valor2.text())
            r = v1 + v2
            self.__LEd_result.setText("%5.2f" % r)
        except ValueError as ve:
            print("Voce deve digitar valores numericos. Err: %s" %ve)
                
    def action_Bt_sub(self):

        try:
            v1 = float(self.__LEd_valor1.text())
            v2 = float(self.__LEd_valor2.text())
            r = v1 - v2
            self.__LEd_result.setText("%5.2f" % r)
        except ValueError as ve:
            print("Voce deve digitar valores numericos. Err: %s" %ve)
                
    def action_Bt_mult(self):

        try:
            v1 = float(self.__LEd_valor1.text())
            v2 = float(self.__LEd_valor2.text())
            r = v1 * v2
            self.__LEd_result.setText("%5.2f" % r)
        except ValueError as ve:
            print("Voce deve digitar valores numericos. Err: %s" %ve)
            
    def action_Bt_div(self):

        try:
            v1 = float(self.__LEd_valor1.text())
            v2 = float(self.__LEd_valor2.text())
            r = v1 / v2
            self.__LEd_result.setText("%5.2f" % r)
        except ValueError as ve:
            print("Voce deve digitar valores numericos. Err: %s" %ve)
            
    def inicialize(self):
        Grid=QGridLayout()
        
        self.__Lb_valor1= QLabel(self, text="Valor1:")
        self.__Lb_valor2= QLabel(self, text="Valor2:")
        self.__Lb_result= QLabel(self, text="Resultado:")
        
        self.__LEd_valor1= QLineEdit(self, width=52)
        self.__LEd_valor2= QLineEdit(self, width=52)
        self.__LEd_result= QLineEdit(self, width=52)
        
        self.__Bt_adic=QPushButton(self, text='Adicionar')
        self.__Bt_adic.clicked.connect(self.action_Bt_adic)

        self.__Bt_sub = QPushButton(self, text='Subtrair')
        self.__Bt_sub.clicked.connect(self.action_Bt_sub)

        self.__Bt_mult = QPushButton(self, text='Multiplicar')
        self.__Bt_mult.clicked.connect(self.action_Bt_mult)

        self.__Bt_div = QPushButton(self, text='Dividir')
        self.__Bt_div.clicked.connect(self.action_Bt_div)

        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)
        
        self.__Lb_valor1.setAutoFillBackground(True)
        self.__Lb_valor1.setPalette(p1)
        
        self.__Lb_valor2.setAutoFillBackground(True)
        self.__Lb_valor2.setPalette(p1)
        
        self.__Lb_result.setAutoFillBackground(True)
        self.__Lb_result.setPalette(p1)
        
        Grid.addWidget(self.__Lb_valor1, 0, 0, 1, 1)
        Grid.addWidget(self.__Lb_valor2, 1, 0, 1, 1)
        Grid.addWidget(self.__Lb_result, 3, 0, 1, 1)
        
        Grid.addWidget(self.__LEd_valor1, 0, 1, 1, 4)
        Grid.addWidget(self.__LEd_valor2, 1, 1, 1, 4)
        Grid.addWidget(self.__LEd_result, 3, 1, 1, 4)
        
        Grid.addWidget(self.__Bt_adic, 2, 1, 1, 1)
        Grid.addWidget(self.__Bt_sub, 2, 2, 1, 1)
        Grid.addWidget(self.__Bt_mult, 2, 3, 1, 1)
        Grid.addWidget(self.__Bt_div, 2, 4, 1, 1)
        
        self.setLayout(Grid)
        self.show()

