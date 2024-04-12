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
        self.__Total = Total_a
        self.__Thr = threading.Thread(target=self.run)
        self.__Thr.start()
    def parar(self):
        self.__Total = 0;
        self.__Thr = None;
    def run(self):
        while self.__Total >= 0:
            self.__LEd.setText(str(int(self.__LEd.text()) + 1))
            time.sleep(random.randint(1,7))
            
            self.__Total += -1

