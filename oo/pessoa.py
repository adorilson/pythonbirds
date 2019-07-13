class Pessoa:
    def __init__(self, *filhos, nome = None, idade=39):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)} '

if __name__=='__main__':
    alice = Pessoa(nome='Alice')
    alexia = Pessoa(nome='Alexia')

    p = Pessoa(alice, alexia, nome='Adorilson')

    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Adorilson'
    print(p.nome)
    print(p.idade)

    for filho in p.filhos:
        print(filho.nome)
