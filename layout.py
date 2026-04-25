from common import *

def introducao():
    intro = '''Essa foi a minha tentativa de replicar (para fins de estudo) o jogo Termo.
    Espero que goste! Aqui está um breve tutorial:

    - Você terá 8 tentativas para acertar a palavra.

    - [on yellow] AMARELO [/] significa que a letra existe, mas não está na posição correta!

    - [on dark_green] VERDE [/] significa que a letra está na posição correta!

    - Atenção, pode haver mais de uma letra igual por palavra!'''

    painel_intro = Panel(intro, title='[bold underline bright_cyan]Bem vindo ao FatoTermo!',
                         subtitle='[bold underline bright_yellow]Selecione um modo de jogo para começar!',
                         border_style='green')
    print(painel_intro)


def frase_vitoria(tentativas, max_tentativas):
    proporcao = tentativas/max_tentativas
    if tentativas <= max_tentativas:
        if tentativas == 1:
            frase = f'[bold green]INACREDITÁVEL![/] Você acertou [cyan]DE PRIMEIRA[/]!'
        elif proporcao < 0.2:
            frase = f'[bold_cyan]INCRÍVEL![/] Você acertou a palavra em [cyan]{tentativas} tentativas[/]!'
        elif proporcao < 0.4:
            frase = f'[bold_cyan]EXCELENTE![/] Você acertou a palavra em [cyan]{tentativas} tentativas[/]!'
        elif proporcao < 0.6:
            frase = f'[bold_cyan]BOA![/] Você acertou a palavra  em [cyan]{tentativas} tentativas[/]!'
        elif proporcao < 0.8:
            frase = f'Você acertou a palavra em [cyan]{tentativas} tentativas[/]!'
        else:
            frase = f'[bold_cyan]UFA![/]Você acertou a palavra em [cyan]{tentativas} tentativas[/]!'
    else:
        frase = f'[red]Você perdeu![/] Boa sorte na próxima!'
    return frase


def valida_int(txt, ini=0, fim=None, exceto=None, negativo = False, erro = f'[bold red]Opção inválida! Digite novamente.'):
    """
    ->Valida um número inteiro positivo ou um str definido como exceção.
    :param txt: Valor a ser analisado.
    :param ini: Intervalo inicial da validação
    :param fim: Intervalo final da validação. Se não especificado, não haverá limite final.
    :param exceto: Define a str que será a exceção da validação.
    :param negativo: Caso False, valida somente valores positivos.
    :param erro: Mensagem de erro personalizada.
    :return: Retorna um número inteiro positivo dentro do intervalo exigido
    OU uma mensagem solicitando novo input.
    """
    while True:
        num=str(console.input(txt)).strip()
        if exceto is not None and num.upper()==exceto.upper():
            return str(num)
        if num.isdecimal():
            num=int(num)
            if num>=ini and (fim is None or num<=fim):
                if (num<0 and negativo) or num>=0:
                    return int(num)

        print(erro)