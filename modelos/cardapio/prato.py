from modelos.cardapio.item_cardapio import  IntemCardapio

class Prato(IntemCardapio):
    def __init__(self, nome, descricao, preco=0.0):
        super().__init__(nome, preco)
        self._descricao = descricao
        
    def __str__(self) :
         return f'{self._nome.ljust(15)} | {self._descricao.ljust(15)} | R$ {str(self._preco).ljust(15)} | R$ {str(self._desconto).ljust(15)}'
    
    def desconto(self, desconto_a=0.0):
        desconto_a = float((input('Digite o valor do desconto do prato "%": ')))
        self._desconto = self._preco - (desconto_a/100)
        return self._desconto