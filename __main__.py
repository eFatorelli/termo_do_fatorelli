from jogos import unico, multiplo
from layout import *


def main():
    introducao()
    selecao = valida_int(
    '   [ 1 ] - ÚNICO\n'
        '   [ 2 ] - DUETO\n'
        '   [ 3 ] - QUARTETO\n'
        '   [ 4 ] - PERSONALIZADO\n'
        '       → ',1,4)
    match selecao:
        case 1:
            unico()
        case 2:
            multiplo(2)
        case 3:
            multiplo(4)
        case 4:
            multiplo(valida_int('Digite o número de jogos que quer fazer ao mesmo tempo!'
                                '\n       → ',
                                2,erro='Digite um número maior que 1!'))

if __name__ == '__main__':
    main()