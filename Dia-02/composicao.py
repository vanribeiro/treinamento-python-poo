
# composição é uma maneira de ligar objetos sem herança


class Pizzaria:
    def __init__(self) -> None:
        self.forno = Forno()
    
    def pedido(self, pizza):
        self.forno.assar(pizza)


class Forno:
    def __init__(self):
        self.pizzas = []
        self.lenha = None

