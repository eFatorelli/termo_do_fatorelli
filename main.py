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
conteudo = ''
teclado = '|'.join([l for l in 'qwertyuiop\nasdfghjkl\nzxcvbnm'.upper()])
while not acertou:
    qtde_tentativas += 1
    acertou = True

    while True: #Validação input 5 letras
        tentativa = input(' → ').upper()
        if len(tentativa) == 5:
            break
        print('[bold yellow]Digite uma palavra com 5 letras!')

    tentativa = [l for l in tentativa]
    for pos_letra in range(5):
        if tentativa[pos_letra] == resp_sem_acento[pos_letra]: #Letra na posição correta
            tentativa[pos_letra] = f'[on dark_green]{tentativa[pos_letra]}[/]'

        elif tentativa[pos_letra] in resp_sem_acento: #Letra na posição errada
            tentativa[pos_letra] = f'[on yellow]{tentativa[pos_letra]}[/]'
            acertou = False

        else:
            acertou = False
    if qtde_tentativas == 1:
        conteudo = '|'.join(tentativa)
    else:
        conteudo += '\n' + '|'.join(tentativa)
    painel_termo = Panel(conteudo, width=19, height=10)

    # Teclado

    painel_teclado = Panel(teclado, width=24, title= 'Teclado')

    console.clear()
    print(painel_termo)
    print(painel_teclado)
print(f'Você acertou em {qtde_tentativas} tentativas!')





