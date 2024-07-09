from abc import ABC, abstractmethod
class IntemCardapio():
    
    def __init__(self, nome, preco=0.0):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def desconto(self):
        pass
        
