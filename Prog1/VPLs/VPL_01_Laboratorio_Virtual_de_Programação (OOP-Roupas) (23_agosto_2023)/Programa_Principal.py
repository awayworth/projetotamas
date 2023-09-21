import sys
from Roupa import Roupa

def main():
    r1=Roupa()
    
    r1.Leitura()
    
    r1.Calcula_Total()
    
    print(r1.toString())
    
    del(r1)
main()

sys.exit(0)

