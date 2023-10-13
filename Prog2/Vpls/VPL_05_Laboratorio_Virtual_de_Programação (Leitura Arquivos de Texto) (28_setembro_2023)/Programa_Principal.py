import sys

try:
    with open('Banco_Alunos.txt', 'r') as f:

        Vect_Str = f.readlines()
except FileNotFoundError as e:
    print("O arquivo no foi encontrado.")
except IOError as e:
    print("O arquivo no pode ser aberto.")
except Exception as e:
    print("O arquivo est corrompido.")
    
for str in Vect_Str:
    str = str.strip()
    print('%s' % str)
    
sys.exit(0)

