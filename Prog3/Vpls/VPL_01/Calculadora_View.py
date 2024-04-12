import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class View(QWidget):
    __Lb_valor1 = None
    __Lb_valor2 = None
    __Lb_result = None
    __LEd_valor1 = None
    __LEd_valor2 = None
    __LEd_result = None
    __Bt_adic = None
    __Bt_sub = None
    __Bt_mult = None
    __Bt_div = None
    __Cntr = None

    def __init__(self, Cntr, Str="Janela"):
        super().__init__()
        self.__Cntr=Cntr
        self.setWindowTitle(Str)
        self.setGeometry(320, 160, 10, 10)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('orange'))
        self.setPalette(p)

        self.inicialize()

    def closeEvent(self, event):
        print("Destruindo janela...")
        self.destroy()
        sys.exit(0)

    def get_Valor1(self):
        return(self.__LEd_valor1.text())

    def get_Valor2(self):
        return(self.__LEd_valor2.text())

    def set_Resultado(self, resultado):
        self.__LEd_result.setText("%5.2f" % resultado)

    def action_Bt_adic(self):
        self.__Cntr.action_Adicionar()

    def action_Bt_sub(self):
        self.__Cntr.action_Subtrair()

    def action_Bt_mult(self):
        self.__Cntr.action_Multiplicar()

    def action_Bt_div(self):
        self.__Cntr.action_Dividir()

    def show_error(self, Erro):
        QMessageBox.critical(self, "Janela de Erro", Erro)

    def inicialize(self):
        Grid=QGridLayout()

        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)

        self.__Lb_valor1=QLabel(self, text="Valor1:", width=12)
        self.__Lb_valor2=QLabel(self, text="Valor2:", width=12)
        self.__Lb_result = QLabel(self, text="Resultado:", width=12)

        self.__Lb_valor1.setAlignment(Qt.AlignRight)
        self.__Lb_valor2.setAlignment(Qt.AlignRight)
        self.__Lb_result.setAlignment(Qt.AlignRight)

        self.__Lb_valor1.setContentsMargins(4, 4, 4, 4)
        self.__Lb_valor2.setContentsMargins(4, 4, 4, 4)
        self.__Lb_result.setContentsMargins(4, 4, 4, 4)

        self.__Lb_valor1.setAutoFillBackground(True)
        self.__Lb_valor1.setPalette(p1)

        self.__Lb_valor2.setAutoFillBackground(True)
        self.__Lb_valor2.setPalette(p1)

        self.__Lb_result.setAutoFillBackground(True)
        self.__Lb_result.setPalette(p1)

        self.__LEd_valor1=QLineEdit(self, width=28)
        self.__LEd_valor2=QLineEdit(self, width=28)
        self.__LEd_result=QLineEdit(self, width=28)

        self.__Bt_adic=QPushButton(self, text='Adicionar')
        self.__Bt_adic.clicked.connect(self.action_Bt_adic)

        self.__Bt_sub = QPushButton(self, text='Subtrair')
        self.__Bt_sub.clicked.connect(self.action_Bt_sub)

        self.__Bt_mult = QPushButton(self, text='Multiplicar')
        self.__Bt_mult.clicked.connect(self.action_Bt_mult)

        self.__Bt_div = QPushButton(self, text='Dividir')
        self.__Bt_div.clicked.connect(self.action_Bt_div)

        Grid.addWidget(self.__Lb_valor1, 0, 0)
        Grid.addWidget(self.__Lb_valor2, 1, 0)

        Grid.addWidget(self.__LEd_valor1, 0, 1, 1, 4)
        Grid.addWidget(self.__LEd_valor2, 1, 1, 1, 4)

        Grid.addWidget(self.__Bt_adic, 2, 1)
        Grid.addWidget(self.__Bt_sub, 2, 2)
        Grid.addWidget(self.__Bt_mult, 2, 3)
        Grid.addWidget(self.__Bt_div, 2, 4)

        Grid.addWidget(self.__Lb_result, 3, 0)
        Grid.addWidget(self.__LEd_result, 3, 1, 1, 4)

        self.setLayout(Grid)
        self.show()

