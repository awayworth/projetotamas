import datetime
import threading
import time

class ThreadClock:
    __Total = None
    __LEd = None
    __Thr = None

    def __init__(self, LEd):
        self.__LEd = LEd
       
    def iniciar(self, Total_a):
        try:
            self.__Total = Total_a
            self.__Thr = threading.Thread(target=self.run)
            self.__Thr.start()
        except Exception as ex:
            print("Error: unable to start thread: %s\n" % (ex))
        
    def parar(self):
        try:
            
            self.__Total = 0;
            self.__Thr = None
        except:
            print("Error: unable to start thread: %s\n" % (ex))
            
    def isRunning(self):
        return self.__Thr.is_alive() if self.__Thr else False

    def run(self):
        count = 0
        while count < self.__Total:
            count += 1
            now = datetime.datetime.now()
            time_str = now.strftime("%H:%M:%S")
            self.__LEd.setText(time_str)
            time.sleep(1)
        self.__Thr = None