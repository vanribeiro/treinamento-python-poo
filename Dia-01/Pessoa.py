class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

class Conta:
    def __init__(self, numero) -> None:
        self.numero = numero

class Usuario(Pessoa, Conta):
    
    # semelhante ao método construtor
    def __init__(self, nome, idade, numero, nome_de_usuario) -> None:
        Pessoa.__init__(self, nome, idade)
        Conta.__init__(self, numero)
        self.nome_de_usuario = nome_de_usuario

user = Usuario('Vanessa', 35, '1223-1', 'vanribeiro')
print("Nome: ", user.nome)
print("Idade: ", user.idade)
print("Nome de Usuário:", user.nome_de_usuario)
print("Conta ", user.numero)
