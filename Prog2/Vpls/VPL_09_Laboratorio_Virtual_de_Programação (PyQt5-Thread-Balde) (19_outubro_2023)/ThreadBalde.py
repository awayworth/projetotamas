import threading
import time

##########################################################

class ThreadBalde:
    __Total = None
    __LEd   = None
    __PBar  = None
    __Thr   = None

    def __init__(self, LEd_a, PBar_a):
        self.__LEd  = LEd_a
        self.__PBar = PBar_a

    def iniciar(self, Total_a):
        try:
            if self.__Thr is None:
                self.__Total = Total_a
                self.__Thr   = threading.Thread(target=self.run)
                self.__Thr.start()
        except Exception as ex:
            print("Error: unable to start thread: %s\n" % (ex))

    def parar(self):
        try:
            self.__Total = 0
            self.__Thr   = None
        except Exception as ex:
            print("Error: unable to stop thread: %s\n" % (ex))

    def isRunning(self):
        if self.__Thr is None:
            return False
        else:
            return True

    def run(self):
        tempo = 0.04  # 0.08 / 2, dividido entre LEd e PBar

        # Enchendo: 0 -> 100
        valor = 0
        while valor <= 100 and self.__Total > 0:
            self.__LEd.setText("%d" % valor)
            time.sleep(tempo)
            self.__PBar.setValue(valor)
            time.sleep(tempo)
            valor += 1

        # Esvaziando: 100 -> 0
        valor = 100
        while valor >= 0 and self.__Total > 0:
            self.__LEd.setText("%d" % valor)
            time.sleep(tempo)
            self.__PBar.setValue(valor)
            time.sleep(tempo)
            valor -= 1

        self.__Thr = None

##########################################################
