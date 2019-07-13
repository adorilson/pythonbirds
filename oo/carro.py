


"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Metodo acelerar, que deverá incrementar a velocidade de uma unidade
3) Metodo frear, que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste
2) Metodo girar_a_direita
3) Metodo girar_a_esquerda

    N
O       L
    S

    Exemplo:
    >>> # testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # testando a direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'

"""

class Motor():
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade<0:
            self.velocidade = 0


class Direcao():
    NORTE = 'Norte'
    LESTE = 'Leste'
    SUL = 'Sul'
    OESTE = 'Oeste'

    def __init__(self):
        self.valor = Direcao.NORTE

    def girar_a_direita(self):
        if self.valor == Direcao.NORTE:
            self.valor = Direcao.LESTE
        elif self.valor == Direcao.LESTE:
            self.valor = Direcao.SUL
        elif self.valor == Direcao.SUL:
            self.valor = Direcao.OESTE
        else:
            self.valor = Direcao.NORTE

    def girar_a_esquerda(self):
        if self.valor == Direcao.NORTE:
            self.valor = Direcao.OESTE
        elif self.valor == Direcao.OESTE:
            self.valor = Direcao.SUL
        elif self.valor == Direcao.SUL:
            self.valor = Direcao.LESTE
        else:
            self.valor = Direcao.NORTE


class Carro():

    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()
