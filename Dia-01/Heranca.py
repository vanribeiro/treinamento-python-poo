class Pizza:
    def ingredientes(self):
        return 'Ingredientes'
    
class Mussarela(Pizza):
    def ingredientes(self):
        return [
            'queijo mussarela', 
            'molho de tomate', 
            'oregano'
        ]
    

pizza = Pizza()
print("[Classe Pizza Pai]:", pizza.ingredientes())

mussarela = Mussarela()
print("[Classe Mussarela Filha]:", mussarela.ingredientes())
