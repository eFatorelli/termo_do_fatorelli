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
            # Isso iguala caracteres com acento aos sem acento.

# print(resposta) #Temporário, para ver se ta funcionando
introducao = '''Essa foi a minha tentativa de replicar (para fins de estudo) o jogo Termo.
Espero que goste! Aqui está um breve tutorial:

- Você terá 8 tentativas para acertar a palavra.

- [on yellow] AMARELO [/] significa que a letra existe, mas não está na posição correta!

- [on green] VERDE [/] significa que a letra está na posição correta!

- Atenção, pode haver mais de uma letra igual por palavra!'''

painel_intro = Panel(introducao,title='[bold underline bright_cyan]Bem vindo ao FatoTermo!',
                     subtitle='[bold underline bright_yellow]Digite uma palavra de 5 letras para começar!',
                     border_style= 'green')
print(painel_intro)
acertou = False
qtde_tentativas = 0
frase_vitoria = conteudo = ''
teclado = '|'.join([f' {l} ' for l in 'qwertyuiop\nasdfghjkl\nzxcvbnm'.upper()])
display = ['0','1','2','3','4']
acerto = list()
while not acertou:
    acertou = True

     #Validação input 5 letras
    tentativa = input(' → ').upper()
    if not len(tentativa) == 5:
        acertou = False
        console.clear()
        print('[bold yellow]Digite uma palavra com 5 letras!')

    else:
        qtde_tentativas += 1
        tentativa = [l for l in tentativa]

        # VERIFICA O QUE FOR VERDE
        for posicao, letra in enumerate(tentativa):
            if letra == resp_sem_acento[posicao]: #Letra na posição correta
                display[posicao] = f'[on dark_green] {letra} [/]'
                teclado = teclado.replace(f' {letra.upper()} ',f'[on dark_green] {letra.upper()} [/]')
                acerto.append(letra)

        # VERIFICA O RESTO
        for posicao, letra in enumerate(tentativa):
            qtde_l_resp = resp_sem_acento.count(letra)
            qtde_l_tentativa = tentativa.count(letra)
            aparicao = tentativa[:posicao + 1].count(letra)
            if letra != resp_sem_acento[posicao]:
                # VERIFICA SE É AMARELO (LETRA NA POSIÇÃO ERRADA)
                if letra in resp_sem_acento:
                    if qtde_l_tentativa <= qtde_l_resp or qtde_l_tentativa > qtde_l_resp >= (aparicao + acerto.count(letra)):
                        # Verifica se a quantidade de letras da tentativa é menor que a da resposta
                        # ou se a soma das letras AMARELAS e VERDES é maior que a quantidade dessa letra na resposta.
                        display[posicao] = f'[on yellow] {letra} [/]'

                    else:
                        display[posicao] = f' {letra} '
                    acertou = False
                    teclado = teclado.replace(f' {letra.upper()} ',f'[on yellow] {letra.upper()} [/]')
                # NADA
                else:
                    display[posicao] = f' {letra} '
                    acertou = False
                    if letra not in termo:
                        teclado = teclado.replace(letra.upper(),f'[black]{letra.upper()}[/]')

        match qtde_tentativas:
            case 1:
                conteudo = '|'.join(display)
                frase_vitoria = (f'[bold green]INCRÍVEL![/] Você acertou a palavra '
                                 f'[bold underline]{termo.upper()}[/]'
                                 f' em [cyan]DE PRIMEIRA[/]!')
            case 2|3:
                conteudo += '\n' + '|'.join(display)
                frase_vitoria = (f'[bold_cyan]EXCELENTE![/] Você acertou a palavra '
                                 f'[bold underline]{termo.upper()}[/]'
                                 f' em [cyan]{qtde_tentativas} tentativas[/]!')
            case 4|5|6:
                conteudo += '\n' + '|'.join(display)
                frase_vitoria = (f'[bold_cyan]BOA![/] Você acertou a palavra '
                                 f'[bold underline]{termo.upper()}[/]'
                                 f' em [cyan]{qtde_tentativas} tentativas[/]!')
            case 7:
                conteudo += '\n' + '|'.join(display)
                frase_vitoria = (f'[bold_cyan]FOI QUASE![/] Você acertou a palavra '
                                 f'[bold underline]{termo.upper()}[/]'
                                 f' em [cyan]{qtde_tentativas} tentativas[/]!')
            case 8:
                frase_vitoria = f'[bright_red] VOCÊ PERDEU[/]! A palavra era {termo}!!!'
                break
        console.clear()

    painel_termo = Panel(f'[bold]{conteudo}[/]', width=23, height=10)
    painel_teclado = Panel(teclado, width=44, title= 'Teclado',subtitle= f'Tentativas: {qtde_tentativas}')

    print(painel_termo)
    print(painel_teclado)
console.rule(style='default')
print(frase_vitoria)





