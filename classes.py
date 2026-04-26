from common import *


class Quadro:
    acentos = {'A': ('Ã', 'Á', 'À', 'Â'),
               'E': ('É', 'Ê'),
               'I': 'Í',
               'O': ('Õ', 'Ó','Ô'),
               'U': ('Ú', 'Ü'),
               'C': 'Ç'}

    def __init__(self, palavra, max_tentativas, tamanho = 5):
        self.palavra = palavra
        self.sem_acento = [l for l in palavra.upper()]
        self.tentativas = 0
        self.max_tentativas = max_tentativas
        self.tamanho = tamanho
        self.acertou = False
        self.conteudo = ''

        for index, letra in enumerate(self.sem_acento):
            for k, v in self.acentos.items():
                if letra in v:
                    self.sem_acento[index] = k


    def verificar_tamanho(self, tentativa):
        if not len(tentativa) == self.tamanho:
            console.clear()
            print('[bold yellow]Digite uma palavra com 5 letras!')
            return False
        else:
            return True

    def tentar(self, tentativa):
        if self.acertou:
            return None
        display = ['' for _ in range(self.tamanho)]
        if not self.verificar_tamanho(tentativa):
            return None
        self.acertou = True
        self.tentativas += 1
        tentativa = [l for l in tentativa.upper()]
        acerto = list()

        # VERIFICA O QUE FOR VERDE
        for posicao, letra in enumerate(tentativa):
            if letra == self.sem_acento[posicao]: #Letra na posição correta
                display[posicao] = f'[on dark_green] {letra} [/]'
                # teclado = teclado.replace(f' {letra.upper()} ',f'[on dark_green] {letra.upper()} [/]')
                acerto.append(letra)

        # VERIFICA O RESTO
        for posicao, letra in enumerate(tentativa):
            qtde_l_resp = self.sem_acento.count(letra)
            qtde_l_tentativa = tentativa.count(letra)
            aparicao = tentativa[:posicao + 1].count(letra)
            if letra != self.sem_acento[posicao]:
                # VERIFICA SE É AMARELO (LETRA NA POSIÇÃO ERRADA)
                if letra in self.sem_acento:
                    if qtde_l_tentativa <= qtde_l_resp or qtde_l_tentativa > qtde_l_resp >= (aparicao + acerto.count(letra)):
                        # Verifica se a quantidade de letras da tentativa é menor que a da resposta
                        # ou se a soma das letras AMARELAS e VERDES é maior que a quantidade dessa letra na resposta.
                        display[posicao] = f'[on yellow] {letra} [/]'

                    else:
                        display[posicao] = f' {letra} '
                    # teclado = teclado.replace(f' {letra.upper()} ',f'[on yellow] {letra.upper()} [/]')
                # NADA
                else:
                    display[posicao] = f' {letra} '
                    # if letra not in self.sem_acento:
                    #     teclado = teclado.replace(letra.upper(),f'[black]{letra.upper()}[/]')
                self.acertou = False
        console.clear()
        return display

    def mostrar(self, tentativa):
        if self.acertou:
            pass
        else:
            display = self.tentar(tentativa)
            if display is not None:
                if self.tentativas == 1:
                    self.conteudo = '|'.join(display)
                else:
                    self.conteudo += '\n' + '|'.join(display)
        painel = Panel(f'[bold]{self.conteudo}[/]', width=23, height=self.max_tentativas+2)
        return painel

    def acertar(self):
        if self.acertou:
            return self.tentativas
        elif self.tentativas == self.max_tentativas:
            self.tentativas += 1
            return self.tentativas
        else:
            return False