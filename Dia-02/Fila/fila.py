from fila_protocolo import Fila

class Padaria(Fila):

    def __init__(self) -> None:
        return super().__init__()

    def entrar(self, obj) -> None:
        self.lista.append(obj)

    def sair(self, pos = 0) -> None:
        return self.lista.pop(pos)
    
    def __len__(self) -> None:
        return self.lista.__len__()

    def __contains__(self, obj) -> None:
        return obj in self.lista

    def __repr__(self) -> str:
        return f"Fila({self.lista})"
    

def format_string_numbers_from_zero_to_ten(obj):
    return len(obj) if (len(obj) >= 10) else f"0{len(obj)}"

filaPadaria = Padaria()
filaPadaria.entrar("Márcia")
filaPadaria.entrar("Carlos")
filaPadaria.entrar("Soraia")
filaPadaria.entrar("Aninha")
print(
    "Tamanho da Fila: ", 
    format_string_numbers_from_zero_to_ten(filaPadaria)
)
print(filaPadaria.sair())
print(filaPadaria.__repr__())