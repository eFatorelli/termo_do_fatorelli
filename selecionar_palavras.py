from rich.console import Console
from rich import print
import json

console = Console()
remover = list()
fechar = False
with open('termo.json','r', encoding= 'utf-8') as a:
    lista = json.load(a)

inicio = int(input('Digite o número de onde começar:\n → '))
print('SELECIONE AS PALAVRAS VÁLIDAS:')
for cont, palavra in enumerate(lista[inicio:]):
    contador = cont + inicio
    print(' '*10 + f'[cyan]{palavra}[/]')
    for p in lista[contador+1:contador+10]:
        print(' '*10 + p)
    while True:
        opcao = input('Remover palavra [ S / N / FECHAR]?\n → ').upper().strip()
        match opcao:
            case 'S'|'':
                print(f'[bright_red]PALAVRA {palavra} REMOVIDA')
                remover.append(palavra)
                break
            case 'N':
                print(f'[green]PALAVRA {palavra} MANTIDA')
                break
            case 'FECHAR':
                for r in remover:
                    lista.remove(r)
                fechar = True
                break
            case _:
                print('Opção inválida')
    console.clear()
    if fechar:
        break

print('Palavras a serem removidas: ')
print(remover)

while True:
    confirma = input('Se quer realmente remover essas palavras, digite REMOVER:\n → ').upper().strip()
    if not confirma == 'REMOVER':
        print('Confirmação inválida!!!')
    else:
        print('Removendo as palavras da lista.')
        with open('termo.json','w',encoding='utf-8') as t:
            json.dump(lista,t,ensure_ascii=False, indent= 4)
        break