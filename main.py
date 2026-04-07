from rich import print
from rich.panel import Panel
from rich.console import Console
from random import choice
import json

console = Console()
acentos = {'A':('Ã','Á','À'),'E':'É','I':'Í','O':('Õ','Ó'),'U':'Ú'}

with open('termo.json','r', encoding= 'utf-8') as t:
    termo = choice(json.load(t))

resposta = [f' {l} ' for l in termo.upper()]
resposta_sa = resposta[:]

for index, letra in enumerate(resposta):
    for k, v in acentos.items():
        if letra.strip() in v:
            resposta_sa[index] = f' {k} '
print(resposta)
print('Digite uma palavra com 5 letras: ')
acertou = False
qtde_tentativas = 0
conteudo = ''
while not acertou:
    qtde_tentativas += 1
    acertou = True
    while True:
        tentativa = input(' → ').upper()
        if len(tentativa) == 5:
            break
        print('[bold yellow]Digite uma palavra com 5 letras!')
    tentativa = [f' {l} ' for l in tentativa]
    for pos_letra in range(5):
        if tentativa[pos_letra] == resposta_sa[pos_letra]:
            tentativa[pos_letra] = f'[on dark_green]{tentativa[pos_letra]}[/]'
        elif tentativa[pos_letra] in resposta_sa:
            tentativa[pos_letra] = f'[on yellow]{tentativa[pos_letra]}[/]'
            acertou = False
        else:
            acertou = False
    if qtde_tentativas == 1:
        conteudo = '|'.join(tentativa)
    else:
        conteudo += '\n' + '|'.join(tentativa)
    painel_termo = Panel(conteudo, width=23)
    teclado = '|'.join([l for l in 'qwertyuiop'.upper()]) + '\n'
    teclado += ' ' + '|'.join([l for l in 'asdfghjkl'.upper()]) + '\n'
    teclado += '   ' + '|'.join([l for l in 'zxcvbnm'.upper()]).center(13)
    painel_teclado = Panel(teclado, width=23, title= 'Teclado')
    console.clear()
    print(painel_termo)
    print(painel_teclado)
print('Você acertou!')





