import random
import threading
import time

class ThreadSchlacht:
    __Total=None
    __LEd=None
    __Thr=None

    def __init__(self, LEd_a):
        self.__LEd = LEd_a

    def iniciar(self, Total_a):
        try:
            if self.__Thr is None:
                self.__Total = Total_a
                self.__Thr = threading.Thread(target=self.run)
                self.__Thr.start()
        except Exception as ex:
            print("Error: unable to start thread: %s\n" % (ex))

    def parar(self):
        try:
            self.__Total = -1
            self.__Thr = None
        except Exception as ex:
            print("Error: unable to stop thread: %s\n" % (ex))

    def isRunning(self):
        if self.__Thr is None:
            return False
        else:
            return True

    def run(self):
        while self.__Total > 0:
            valor = int(self.__LEd.text()) + 1
            self.__LEd.setText(str(valor))
            tempo = random.random()
            time.sleep(tempo)
            self.__Total += -1
        self.__Thr = None

