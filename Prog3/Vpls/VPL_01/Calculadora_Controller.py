from Calculadora_Model import Model
from Calculadora_View import View

class Controller():
    __model = None
    __view = None

    def __init__(self):
        self.start()

    def start(self):
        self.__model = Model()
        self.__view = View(self, "Minha Calculadora")

    def action_Adicionar(self):
        str1 = self.__view.get_Valor1()
        str2 = self.__view.get_Valor2()

        try:
            val1 = float(str1)
            val2 = float(str2)

            self.__model.set_Valor1(val1)
            self.__model.set_Valor2(val2)
            self.__model.adiciona_valores()

            self.__view.set_Resultado(self.__model.get_Resultado())
        except ValueError as ve:
            Erro = "Erro: Favor digitar valores numéricos.\n(%s)" % ve
            self.__view.show_error(Erro)
            print(Erro)
        except Exception as ex:
            Erro = "Erro fatal: Erro inexperado.\n(%s)" % ex
            self.__view.show_error(Erro)
            print(Erro)

    def action_Subtrair(self):
        str1 = self.__view.get_Valor1()
        str2 = self.__view.get_Valor2()

        try:
            val1 = float(str1)
            val2 = float(str2)

            self.__model.set_Valor1(val1)
            self.__model.set_Valor2(val2)
            self.__model.subtrai_valores()

            self.__view.set_Resultado(self.__model.get_Resultado())
        except ValueError as ve:
            Erro = "Erro: Favor digitar valores numéricos.\n(%s)" % ve
            self.__view.show_error(Erro)
            print(Erro)
        except Exception as ex:
            Erro = "Erro fatal: Erro inexperado.\n(%s)" % ex
            self.__view.show_error(Erro)
            print(Erro)

    def action_Multiplicar(self):
        str1 = self.__view.get_Valor1()
        str2 = self.__view.get_Valor2()

        try:
            val1 = float(str1)
            val2 = float(str2)

            self.__model.set_Valor1(val1)
            self.__model.set_Valor2(val2)
            self.__model.multiplica_valores()

            self.__view.set_Resultado(self.__model.get_Resultado())
        except ValueError as ve:
            Erro = "Erro: Favor digitar valores numéricos.\n(%s)" % ve
            self.__view.show_error(Erro)
            print(Erro)
        except Exception as ex:
            Erro = "Erro fatal: Erro inexperado.\n(%s)" % ex
            self.__view.show_error(Erro)
            print(Erro)

    def action_Dividir(self):
        str1 = self.__view.get_Valor1()
        str2 = self.__view.get_Valor2()

        try:
            val1 = float(str1)
            val2 = float(str2)

            self.__model.set_Valor1(val1)
            self.__model.set_Valor2(val2)
            self.__model.divide_valores()

            self.__view.set_Resultado(self.__model.get_Resultado())
        except ValueError as ve:
            Erro = "Erro: Favor digitar valores numéricos.\n(%s)" % ve
            self.__view.show_error(Erro)
            print(Erro)
        except ZeroDivisionError as zde:
            Erro = "Erro: Divisao por zero: %s" % zde
            self.__view.show_error(Erro)
            print(Erro)
        except Exception as ex:
            Erro = "Erro fatal: Erro inexperado.\n(%s)" % ex
            self.__view.show_error(Erro)
            print(Erro)

