class Model():
    __valor1=None
    __valor2=None
    __resultado=None

    def __init__(self):
        self.__valor1=0
        self.__valor2=0.0
        self.adiciona_valores()

    def set_Valor1(self, val1):
        self.__valor1=val1

    def set_Valor2(self, val2):
        self.__valor2=val2

    def get_Resultado(self):
        return(self.__resultado)

    def adiciona_valores(self):
        self.__resultado=(self.__valor1 + self.__valor2)

    def subtrai_valores(self):
        self.__resultado=(self.__valor1 - self.__valor2)

    def multiplica_valores(self):
        self.__resultado=(self.__valor1 * self.__valor2)

    def divide_valores(self):
        self.__resultado=(self.__valor1 / self.__valor2)

