import threading
import time

##################################################

class ThreadBalde:
    __Total = None
    __LEd = None
    __PBar = None
    __Thr = None

    def __init__(self, LEd_a, PBar_a):  # Questão 01
        self.__LEd = LEd_a
        self.__PBar = PBar_a

    def iniciar(self, Total_a):
        try:
            self.__Total = Total_a
            self.__Thr = threading.Thread(target=self.run)
            self.__Thr.start()
        except:
            pass

    def parar(self):
        try:
            self.__Total = 0;
            self.__Thr = None;
        except:
            pass
        ## Questão 03:  (Criar o método que encerra a ThreadBalde)

    def isRunning(self):
        return True if self.__Thr else False
        ## Questão 04:  (Criar o método isRunning)

    def run(self):
        self.__LEd.setText("Tchaise")
        
        ## Questão 05:  (Criar o método que realize a ThreadBalde)

##################################################
