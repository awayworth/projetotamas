import math

class Model():
    __peso=None
    __altura=None
    __imc=None
    __classif=None

    def __init__(self):
        self.__peso=0.0
        self.__altura=0.001
        self.__imc=0.0
        self.__classif="Magreza"
    
    def set_Peso(self,peso):
        self.__peso = peso

    def set_Altura(self,altura):
        self.__altura = altura

    def get_imc(self):
        return self.__imc

    def get_classif(self):
        return self.__classif

    def calcula_imc(self):

        self.__imc = self.__peso / (self.__altura ** 2)
        
        if self.__imc < 18.5:
            self.__classif = "Magreza"
        elif 18.5 <= self.__imc < 24.9:
            self.__classif = "Saudável"
        elif 25 <= self.__imc < 29.9:
            self.__classif = "Sobrepeso"
        elif 30 <= self.__imc < 34.9:
            self.__classif = "Obesidade Grau I"
        elif 35 <= self.__imc < 39.9:
            self.__classif = "Obesidade Grau II (severa)"
        else:
            self.__classif = "Obesidade Grau III (mórbida)"
        
