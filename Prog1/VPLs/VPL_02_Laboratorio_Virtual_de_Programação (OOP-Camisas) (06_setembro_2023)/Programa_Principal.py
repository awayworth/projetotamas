import sys
from Camisa import Camisa

def main():
    C1=Camisa()
    C1.Leitura()
    C1.Calcula_Total()
    print(C1.toString())
    del(C1)
main()

sys.exit(0)

