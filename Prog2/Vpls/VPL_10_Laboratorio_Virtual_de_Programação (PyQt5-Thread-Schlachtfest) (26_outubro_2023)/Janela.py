import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ThreadSchlacht import ThreadSchlacht

##################################################

class Janela(QWidget):  ## (Complete o código que declara a classe Janela)
    __LEd1=None
    __LEd2 = None
    __LEd3 = None
    __Bt_Abertura=None
    __Bt_Fechamento=None
    __Barraca1 = None
    __Barraca2 = None
    __Barraca3 = None

    ## Questão 07:  (Criar o construtor da classe Janela)
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

    def closeEvent(self, event):
        self.__Barraca1.parar()
        self.destroy()
        sys.exit(0)
        ## Questão 08:  (Criar o código para encerrar o programa clicando
        ##               no ícone do canto superior direito da janela)

    def action_abertura(self):
        self.__Barraca1.iniciar(60)
        self.__Barraca2.iniciar(60)
        self.__Barraca3.iniciar(60)

    def action_fechamento(self):
        self.__Barraca1.parar()
        self.__Barraca2.parar()
        self.__Barraca3.parar()
        
    def inicialize(self):
        Grid = QGridLayout()
        
        self.__LEd1 = QLineEdit()
        self.__LEd2 = QLineEdit()
        self.__LEd3 = QLineEdit()
        
        self.__LEd1.setText('0')
        self.__LEd2.setText('0')
        self.__LEd3.setText('0')
        
        self.__Bt_Abertura = QPushButton('Abertura')
        self.__Bt_Abertura.clicked.connect(self.action_abertura)
        
        self.__Bt_Fechamento = QPushButton('Fechamento')
        self.__Bt_Fechamento.clicked.connect(self.action_fechamento)

        Grid.addWidget(self.__LEd1, 0, 1, 1, 2)
        Grid.addWidget(self.__LEd2, 1, 1, 1, 2)
        Grid.addWidget(self.__LEd3, 2, 1, 1, 2)
        
        Grid.addWidget(self.__Bt_Abertura, 3, 0, 1, 2)
        Grid.addWidget(self.__Bt_Fechamento, 3, 2, 1 , 2)
        
        self.__Barraca1=ThreadSchlacht(self.__LEd1)
        self.__Barraca2=ThreadSchlacht(self.__LEd2)
        self.__Barraca3=ThreadSchlacht(self.__LEd3)

        self.setLayout(Grid)
        self.show()

##################################################
