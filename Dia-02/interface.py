# Interface para usuários de python é um protocólos

from abc import ABC, abstractclassmethod

class MeuProtocolo(ABC):

    @abstractclassmethod
    def meu_metodo_abstrato(self):
        """meu método abstrado"""
    
    @staticmethod()
    @abstractclassmethod
    def meu_metodo_estatico(self):
        """meu método abstrato e estático"""
