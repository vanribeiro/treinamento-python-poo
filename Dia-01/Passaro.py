# classes 

class Passaro:
    estado = 'indefinido'
    asas = 2
    bico = 1

    def voar(self):
        self.estado = 'Voando'
        print(self.estado)

    def pousar(self):
        self.estado = 'Parado'
        print(self.estado)

# Instância vem Instance e quer dizer exemplo

# self, sempre que quero falar só com a instância
# cls, sempre que quero falar com a class 

passaro = Passaro()
print("asas: ", passaro.asas)
print("bico: ", passaro.bico)
passaro.voar()
passaro.pousar()