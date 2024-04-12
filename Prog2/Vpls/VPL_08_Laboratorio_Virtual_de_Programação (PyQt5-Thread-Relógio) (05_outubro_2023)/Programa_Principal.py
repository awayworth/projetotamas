import sys
from PyQt5.QtWidgets import *
from Janela import Janela

App=QApplication(sys.argv)
Jan1=Janela("Relógio Digital")
App.exec_()