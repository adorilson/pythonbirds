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

    adorilson = Pessoa(alice, alexia, nome='Adorilson')

    print(Pessoa.cumprimentar(adorilson))
    print(id(adorilson))
    print(adorilson.cumprimentar())
    print(adorilson.nome)
    adorilson.nome = 'Adorilson'
    print(adorilson.nome)
    print(adorilson.idade)

    for filho in adorilson.filhos:
        print(filho.nome)


