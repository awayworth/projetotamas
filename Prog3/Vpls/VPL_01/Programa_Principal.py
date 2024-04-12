import sys
from PyQt5.QtWidgets import *
from Calculadora_Controller import Controller

if __name__ == "__main__":
    App=QApplication(sys.argv)
    Cntr=Controller()
    App.exec_()

