import json
import sys
from Data import Data

def Programa_Principal():
    try:
        with open('Banco_Alunos.json.txt', 'w') as file:
            json.dump(Data, file)
    except FileNotFoundError:
        print("Erro: Arquivo no encontrado.")
        sys.exit(0)
    except IOError:
        print("Erro: Erro de entrada e sada.")
        sys.exit(0)

Programa_Principal()