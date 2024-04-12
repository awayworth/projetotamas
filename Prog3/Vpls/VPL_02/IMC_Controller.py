from IMC_Model import Model
from IMC_View import View

class Controller():
    __model = None
    __view = None

    def __init__(self):
        self.start()
    
    def start(self):

        self.__model = Model()
        self.__view = View(self, "Calculadora IMC")

    def action_Calcular(self):

        altura = self.__view.get_Altura()
        peso = self.__view.get_Peso()

        try:
            altura = float(altura)
            peso = float(peso)

            self.__model.set_Peso(peso)
            self.__model.set_Altura(altura)
            self.__model.calcula_imc()

            self.__view.set_imc(self.__model.get_imc())
            self.__view.set_classif(self.__model.get_classif())
        except ValueError as ve:
            Erro = "Erro: Favor digitar valores numéricos.\n(%s)" % ve
            self.__view.show_error(Erro)
            print(Erro)
        except Exception as ex:
            Erro = "Erro fatal: Erro inexperado.\n(%s)" % ex
            self.__view.show_error(Erro)
            print(Erro)
        pass

