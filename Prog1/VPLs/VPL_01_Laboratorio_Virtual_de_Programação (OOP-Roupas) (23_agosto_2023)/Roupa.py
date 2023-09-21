class Roupa:

    __Roupa_Marca=str
    __Roupa_Cor=str
    __Roupa_Tam=int
    __Roupa_Quant=int
    __Roupa_Preco=float
    __Total_Roupa=float

    def __init__(self):
        self.__Roupa_Marca=""
        self.__Roupa_Cor=""
        self.__Roupa_Tam=0
        self.__Roupa_Quant=0
        self.__Roupa_Preco=0.0
        self.__Total_Roupa=0.0
    def Leitura(self):

        self.__Roupa_Marca=input("")
        self.__Roupa_Cor=input("")
        self.__Roupa_Tam=int(input(""))
        self.__Roupa_Quant=int(input(""))
        self.__Roupa_Preco=float(input(""))
        
    def Calcula_Total(self):

        self.__Total_Roupa=float(self.__Roupa_Quant*self.__Roupa_Preco)

    def toString(self):
        string="\nImpressão das Roupas\nMarca da roupa=%s\nCor da roupa=%s\nTamanho da roupa=%d\nQuantidade de roupas=%d\nPreço da peça de roupa=%5.2f\nTotal=%5.2f\n" % (self.__Roupa_Marca, self.__Roupa_Cor, self.__Roupa_Tam, self.__Roupa_Quant, self.__Roupa_Preco, self.__Total_Roupa)
        return string

    def __del__(self):
        self.__Roupa_Marca=""
        self.__Roupa_Cor=""
        self.__Roupa_Tam=0
        self.__Roupa_Quant=0
        self.__Roupa_Preco=0.0
        self.__Total_Roupa=0.0
        self.Calcula_Total()
        print("Passei no destrutor da classe Roupa...")

