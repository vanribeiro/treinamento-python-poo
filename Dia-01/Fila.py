class Fila:
    c_fila = []

    # self, sempre que quero falar só com a instância
    # cls, sempre que quero falar com a class
    @classmethod
    def c_entrar(cls, obj):
        cls.c_fila.append(obj)
        print(cls.c_fila)

    def __init__(self):
        self.s_fila = []

    def s_entrar(self, obj):
        self.s_fila.append(obj)
        print(self.s_fila)

    @staticmethod
    def nome_da_fila():
        print('fila qualquer')


fila = Fila()
fila.c_entrar(2)
fila.c_entrar(1)
fila.c_entrar(5)
fila.c_entrar(7)
print(fila.c_fila)
print(Fila.nome_da_fila())