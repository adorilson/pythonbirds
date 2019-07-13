class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=39):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)} '

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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


    adorilson.sobrenome = 'Bezerra'
    print(adorilson.sobrenome)


    del adorilson.filhos

    adorilson.olhos = 1
    print(alice.__dict__)
    print(adorilson.__dict__)

    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(adorilson.olhos)
    print(alice.olhos)

    print(id(Pessoa.olhos), id(adorilson.olhos), id(alice.olhos))

    print(Pessoa.metodo_estatico(), adorilson.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), adorilson.nome_e_atributos_de_classe())