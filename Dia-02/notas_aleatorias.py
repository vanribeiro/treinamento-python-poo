cesta_de_frutas = ["caqui", "goiaba", "manga", "uva", "laranja", "melancia"]
quantidade_de_frutas = len(cesta_de_frutas)
print("Quantas frutas tem na cesta de frutas?", quantidade_de_frutas)

print("Tem manga?", cesta_de_frutas.__contains__("manga"))
print("Tem maçã?", cesta_de_frutas.__contains__("maçã"))

cesta_de_frutas.pop()
print(cesta_de_frutas)

cesta_de_frutas.append("abacaxi")
print(cesta_de_frutas)

class Pessoa:
    def __init__(self, *args, **kwargs) -> None:
        self.nome = args[0]
        self.idade = args[1]
        self.sexo = kwargs['sexo']
    
    def imprime(self):
        print(f"Pessoa: {self.nome, self.idade, self.sexo}")
    
    def __str__(self) -> str:
        return f"Pessoa{self.nome, self.idade, self.sexo}"


pessoa = Pessoa("Carlos", 18, sexo='M')
pessoa.imprime()
print(str(pessoa))