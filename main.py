from rich import print
from rich.panel import Panel
from rich.console import Console
from random import choice
import json

console = Console()
acentos = {'A':('Ã','Á','À'),'E':'É','I':'Í','O':('Õ','Ó'),'U':'Ú'}

with open('termo.json','r', encoding= 'utf-8') as t:
    termo = choice(json.load(t))

resposta = [l for l in termo.upper()]
resp_sem_acento = resposta[:]

for index, letra in enumerate(resposta):
    for k, v in acentos.items():
        if letra in v:
            resp_sem_acento[index] = k
print(resposta) #Temporário, para ver se ta funcionando
print('Digite uma palavra com 5 letras: ')
acertou = False
qtde_tentativas = 0
frase_vitoria = conteudo = ''
teclado = '|'.join([l for l in 'qwertyuiop\nasdfghjkl\nzxcvbnm'.upper()])
while not acertou:
    qtde_tentativas += 1
    acertou = True

     #Validação input 5 letras
    tentativa = input(' → ').upper()
    if not len(tentativa) == 5:
        acertou = False
        console.clear()
        print('[bold yellow]Digite uma palavra com 5 letras!')

    else:
        tentativa = [l for l in tentativa]
        for posicao, letra in enumerate(tentativa):
            if letra == resp_sem_acento[posicao]: #Letra na posição correta
                tentativa[posicao] = f'[on dark_green]{letra}[/]'
                teclado = teclado.replace(letra.upper(),f'[on dark_green]{letra.upper()}[/]')

            elif letra in resp_sem_acento: #Letra na posição errada
                tentativa[posicao] = f'[on yellow]{letra}[/]'
                acertou = False
                teclado = teclado.replace(letra.upper(),f'[on yellow]{letra.upper()}[/]')

            else:
                acertou = False
                teclado = teclado.replace(letra.upper(),f'[black]{letra.upper()}[/]')

        if qtde_tentativas == 1:
            conteudo = '|'.join(tentativa)
            frase_vitoria = (f'[bold green]INCRÍVEL![/] Você acertou a palavra '
                             f'[bold][underline]{termo.upper()}[/][/]'
                             f' em [cyan]DE PRIMEIRA[/]!')
        else:
            conteudo += '\n' + '|'.join(tentativa)
            frase_vitoria = (f'[bold_cyan]BOA![/] Você acertou a palavra '
                             f'[bold][underline]{termo.upper()}[/][/]'
                             f' em [cyan]{qtde_tentativas} tentativas[/]!')
        console.clear()

    painel_termo = Panel(conteudo, width=19, height=10)
    painel_teclado = Panel(teclado, width=24, title= 'Teclado')

    print(painel_termo)
    print(painel_teclado)
print(frase_vitoria)





