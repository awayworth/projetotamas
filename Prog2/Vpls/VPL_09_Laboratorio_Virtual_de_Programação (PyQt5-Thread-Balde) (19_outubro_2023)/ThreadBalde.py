import threading
import time

class ThreadBalde:
    __Total = None
    __LEd = None
    __PBar = None
    __Thr = None

    def __init__(self, LEd_a, PBar_a):
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

    def isRunning(self):
        return True if self.__Thr else False

    def run(self):
        self.__LEd.setText("Tchaise")
        
