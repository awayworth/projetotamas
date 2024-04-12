import sys
from PyQt5.QtWidgets import *
from IMC_Controller import Controller

App=QApplication(sys.argv)
Cntr=Controller()
App.exec_()

