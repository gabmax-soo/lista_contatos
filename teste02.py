class Pessoa:
    def __init__(self,idade) :
        self.idade = idade


p = Pessoa(18)

p.__setattr__('nome','Joao')
print(p.nome)
print(p.idade)



