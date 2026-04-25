from random import choice, choices
from common import *
from classes import Quadro
from rich.table import Table
from layout import frase_vitoria
import json


def unico():
    with open('termo.json', 'r', encoding='utf-8') as t:
        termo = choice(json.load(t))

    print()
    max_tentativas = 8
    intro = f'[default]O CLÁSSICO TERMO ÚNICO. TENTE ACERTAR EM {max_tentativas} TENTATIVAS!'.center(76)
    painel = Panel(intro, title='[bright_cyan]ÚNICO',
                   subtitle= '[underline bold yellow]Digite uma palavra para começar!',
                   width=80, style= 'green')
    print(painel)
    q1 = Quadro(termo, max_tentativas)
    while True:
        print(q1.mostrar(input(' → ')))
        tentativas = q1.acertar()
        if tentativas:
            print(frase_vitoria(tentativas,max_tentativas))
            if tentativas>max_tentativas:
                print(f'A palavra era [underline cyan]{termo.upper()}[/]!')
            break


def multiplo(dificuldade = 2):
    with open('termo.json', 'r', encoding='utf-8') as t:
        max_tentativas = 7 + dificuldade
        lista = choices(json.load(t), k=dificuldade)
    intro = f'[default]UM DESAFIO A MAIS! TENTE ACERTAR {dificuldade} PALAVRAS EM {max_tentativas} TENTATIVAS!'.center(85)
    painel = Panel(intro, title='[bright_cyan]MÚLTIPLO',
                   subtitle='[underline bold yellow]Digite uma palavra para começar!',
                   width=80, style= 'green')
    print(painel)
    obj = [Quadro(termo, max_tentativas) for termo in lista]
    finalizar = False
    tentativas = list()
    while not finalizar:
        tabela = Table(show_edge=False,show_lines=False, box= None)
        finalizar = True
        tentativa = input(' → ')
        for jogo in range(dificuldade):
            tabela.add_column(obj[jogo].mostrar(tentativa))
            nr_tenta = obj[jogo].acertar()
            if not nr_tenta:
                finalizar = False
            else:
                tentativas.append(nr_tenta)

        console.clear()
        print(tabela)
    if all(tentativas):
        tentativa = max(tentativas)
        print(frase_vitoria(tentativa, max_tentativas))
        if tentativa > max_tentativas:
            termo = ' / '.join(lista)
            print(f'As palavras eram [underline cyan]{termo}[/]!')