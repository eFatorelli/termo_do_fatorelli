from rich.console import Console
from rich import print
import json

console = Console()
remover = list()
fechar = False
with open('termo.json','r', encoding= 'utf-8') as a:
    lista = json.load(a)

while True:
    inicio = input('Digite as letras iniciais de onde começar:\n → ').strip().upper()
    for indice, p in enumerate(lista):
        if p.startswith(inicio):
            inicio = indice
            break
    else:
        print('Palavra não encontrada! Tente novamente.')
        continue
    break

print('REMOVA AS PALAVRAS INVÁLIDAS:')
for cont, palavra in enumerate(lista[inicio:]):
    contador = cont + inicio
    print(' '*10 + f'[bold underline cyan]{palavra}[/]')
    for p in lista[contador+1:contador+10]:
        print(' '*10 + p)
    while True:
        opcao = input('Remover palavra [ S / N / FECHAR]?\n → ').upper().strip()
        console.clear()
        match opcao:
            case 'S'|'':
                print(f'[bright_red]{palavra} REMOVIDA')
                remover.append(palavra)
                break
            case 'N':
                print(f'[green]{palavra} MANTIDA')
                break
            case 'FECHAR':
                fechar = True
                break
            case _:
                print('Opção inválida')
    if fechar:
        break

while True:
    print('Palavras a serem removidas: ')
    print(remover)
    confirma = input('Digite uma palavra que deseja restaurar da lista\n'
                     'ou digite REMOVER para remover todas as palavras:\n → ').upper().strip()
    if not confirma == 'REMOVER':
        if confirma in remover:
            remover.remove(confirma)
            print(f'Palavra [cyan]{confirma}[/] restaurada!')
        else:
            print('Confirmação ou palavra inválida!')
    else:
        for r in remover:
            lista.remove(r)
        print(f'{len(remover)} palavras removidas da lista.')
        print(f'A lista atual possui {len(lista)} palavras!')
        with open('termo.json','w',encoding='utf-8') as t:
            json.dump(lista,t,ensure_ascii=False, indent= 4)
        break