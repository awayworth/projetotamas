import sys
import json

with open('Banco_Alunos.json.txt', 'r') as f:
    Data = json.load(f)

def print_items():
    output_string = ""
    for p in Data['Aluno']:
        print(f'Aluno_Key: { p["Aluno_Key"] }')
        print(f'Cidade_Key: { p["Cidade_Key"] }')
        print(f'Aluno_Nome: { p["Aluno_Nome"] }')
        print(f'Aluno_Idade: { p["Aluno_Idade"] }\n')
        
    for p in Data['Cidade']:
        print(f'Cidade_Key: { p["Cidade_Key"] }')
        print(f'Cidade_Nome: { p["Cidade_Nome"] }')
        print(f'Cidade_Abrev: { p["Cidade_Abrev"] }\n')
    
try:
    print_items()
  
except IOError:
    print('Erro de acesso aos dados')
    
except FileNotFoundError:
    print('Arquivo não encontrado')

sys.exit(0)
