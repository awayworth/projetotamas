import os
import re

def format_file(filepath):
    with open(filepath, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        previous_line = ''
        for line in lines:
            # Remove comentários de linha única na mesma linha do código
            line = re.sub(r'\s*#.*$', "", line)
            # Remove linhas em branco extras
            if line.strip() == '' and previous_line.strip() == '':
                continue
            f.write(line)
            previous_line = line

def format_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                format_file(filepath)
                print(f'Arquivo {filepath} formatado')

# Substitua 'caminho_para_sua_pasta' pelo caminho da pasta que você deseja limpar
format_files('Prog2')
format_files('Prog3')
format_files('Prog1')
input()
