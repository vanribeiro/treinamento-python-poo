from abc import ABC, abstractclassmethod

class Fila(ABC):

    @abstractclassmethod
    def __init__(self) -> None:
        self.lista = []

    @abstractclassmethod
    def entrar(self, obj) -> None:
        pass

    @abstractclassmethod
    def sair(self, obj) -> None:
        pass
    
    @abstractclassmethod
    def __len__(self) -> None:
        pass

    @abstractclassmethod
    def __contains__(self, obj) -> None:
        pass

    @abstractclassmethod
    def __repr__(self) -> str:
        pass
   