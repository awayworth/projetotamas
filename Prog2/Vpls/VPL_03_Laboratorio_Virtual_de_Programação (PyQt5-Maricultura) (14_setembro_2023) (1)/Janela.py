import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Janela( QWidget ):
    __Lb_TituloRegiao=None
    __Lb_TituloPeixe=None
    __Lb_TituloCamarao=None
    __Lb_TotalProd=None

    __Lb_Regiao=[]
    __LEd_Peixe=[]
    __LEd_Camarao=[]
    __LEd_TotalProd=[]

    __LEd_MaiorRegiao=None
    __Bt_Calc=None

    def __init__(self, Str="Janela"):
        super().__init__()
        self.setWindowTitle(Str)
        self.setGeometry(400, 200, 456, 200)
        
        self.setAutoFillBackground(True)
        p=self.palette()
        p.setColor(self.backgroundRole(), QColor("orange"))
        self.setPalette(p)
        
        self.inicialize()

    def total_producao(self):
        for i, tot in enumerate(self.__LEd_TotalProd):
            try:
                tot.setText("%8.2f" % (float(self.__LEd_Peixe[i].text()) + float(self.__LEd_Camarao[i].text())))
            except:
                pass
            
    def maior_regiao(self):
        big_index = -1
        big_tot = -1
        for i, tot in enumerate(self.__LEd_TotalProd):
            try:
                if float(self.__LEd_TotalProd[i].text()) > big_tot:
                    big_tot = float(self.__LEd_TotalProd[i].text());
                    big_index = i
            except:
                pass

        self.__LEd_MaiorRegiao.setText(self.__Lb_Regiao[big_index].text())
            
    def closeEvent(self, event):
        self.destroy()
        sys.exit(0)           
        
    def action_Bt_Calc(self):
        self.total_producao()
        self.maior_regiao()

        pass
    
    def inicialize(self):
        Grid=QGridLayout()
        
        self.__Lb_TituloRegiao= QLabel(self, text="Região")
        self.__Lb_TituloPeixe= QLabel(self, text="Peixe")
        self.__Lb_TituloCamarao= QLabel(self, text="Camarão")
        self.__Lb_TotalProd= QLabel(self, text="Total da Prod.")
        
        self.__Lb_Regiao = [
            QLabel(self, text="Norte"),
            QLabel(self, text="Nordeste"),
            QLabel(self, text="Centro-Oeste"),
            QLabel(self, text="Sudeste"),
            QLabel(self, text="Sul")
            ]
            
        self.__LEd_Peixe = [
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self)
            ]
            
        self.__LEd_Camarao = [
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self)
            ]
            
        self.__LEd_TotalProd = [
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self)
            ]
        
        self.__Bt_Calc=QPushButton(self, text='Calcular')
        self.__Bt_Calc.clicked.connect(self.action_Bt_Calc)
        
        self.__LEd_MaiorRegiao=QLineEdit(self)
        
        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)
        
        self.__Lb_TituloRegiao.setAutoFillBackground(True)
        self.__Lb_TituloRegiao.setPalette(p1)
        
        self.__Lb_TituloPeixe.setAutoFillBackground(True)
        self.__Lb_TituloPeixe.setPalette(p1)
        
        self.__Lb_TituloCamarao.setAutoFillBackground(True)
        self.__Lb_TituloCamarao.setPalette(p1)
        
        self.__Lb_TotalProd.setAutoFillBackground(True)
        self.__Lb_TotalProd.setPalette(p1)
        
        try:
            for i in range(len(self.__Lb_Regiao)):
                self.__Lb_Regiao[i].setAutoFillBackground(True)
                self.__Lb_Regiao[i].setPalette(p1)
        except:
            pass
            
        Grid.addWidget(self.__Lb_TituloRegiao, 0, 0, 1, 1)
        Grid.addWidget(self.__Lb_TituloPeixe, 0, 1, 1, 1)
        Grid.addWidget(self.__Lb_TituloCamarao, 0, 2, 1, 1)
        Grid.addWidget(self.__Lb_TotalProd, 0, 3, 1, 1)
        
        try:
        
            for i, reg in enumerate(self.__Lb_Regiao):
                Grid.addWidget(self.__Lb_Regiao[i], i + 1, 0, 1, 1)
                
            for i, reg in enumerate(self.__LEd_Peixe):
                Grid.addWidget(self.__LEd_Peixe[i], i + 1, 1, 1, 1)
                
            for i, reg in enumerate(self.__LEd_Camarao):
                Grid.addWidget(self.__LEd_Camarao[i], i + 1, 2, 1, 1)
                
            for i, reg in enumerate(self.__LEd_TotalProd):
                Grid.addWidget(self.__LEd_TotalProd[i], i + 1, 3, 1, 1)
            
        except IndexError:
            pass
        
        Grid.addWidget(self.__Bt_Calc, 6,1 ,1 ,1)
        Grid.addWidget(self.__LEd_MaiorRegiao, 6,2 ,1 ,1)
        
        self.setLayout(Grid)
        self.show()

