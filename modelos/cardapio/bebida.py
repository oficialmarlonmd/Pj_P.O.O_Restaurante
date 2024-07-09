from modelos.cardapio.item_cardapio import  IntemCardapio

class Bebida(IntemCardapio):
    bebidas = []
    
    def __init__(self, nome, tamanho, preco=0.0):
        super().__init__(nome, preco)
        self._tamanho = tamanho
        
        
    def __str__(self) :
         return f'{self._nome.ljust(15)} | {self._tamanho.ljust(15)} | R$ {str(self._preco).ljust(15)} | R$ {str(self.desconto).ljust(15)}' 

    def desconto(self, desconto_ativo=0.0):
        desconto_ativo = float((input('Digite o valor do desconto da bebida "%": ')))
        self._desconto = self._preco - (desconto_ativo/100)
        return self._desconto