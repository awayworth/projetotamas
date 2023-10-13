import sys
from Data import Data

try:

    file = open('./Banco_Alunos.txt', 'w')
    for Aluno in Data:
        file.write('%s\n' % Aluno)
            
except IOError as e:
    print('um erro ocorreu:',e)
    
except FileNotFoundError:
    print('Nao achou')
    
sys.exit(0)

