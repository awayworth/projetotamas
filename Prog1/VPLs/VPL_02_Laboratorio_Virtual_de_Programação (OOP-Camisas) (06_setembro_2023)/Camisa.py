from Roupa import Roupa

class Camisa(Roupa):

    __Cam_Tipo=str
    __Cam_Botoes=int
    __Cam_Bolsos=int
    __Cam_Gola=bool
    
    def __init__(self):
        super().__init__()
        self.__Cam_Tipo=""
        self.__Cam_Botoes=0
        self.__Cam_Bolsos=0
        self.__Cam_Gola=True
        
    def Leitura(self):

        self.__Cam_Tipo=input("")
        self.__Cam_Botoes=int(input(""))
        self.__Cam_Bolsos=int(input(""))
        string=input("")
        if (string=='s'):
            self.__Cam_Gola=True
        else:
            self.__Cam_Gola=False
        super().Leitura()

    def toString(self):

        str="\nImpressão das Camisas\n"
        str+="Tipo de camisa=%s\n" % self.__Cam_Tipo
        str+="Quantidade de botões=%d\n" % self.__Cam_Botoes
        str+="Quantidade de bolsos=%d\n" % self.__Cam_Bolsos
        str+="Tem gola=%s\n" % self.__Cam_Gola
        str+=super().toString()
        return str

    def __del__(self):
        super().__del__()
        print("Passei no destrutor da classe Camisa...")

