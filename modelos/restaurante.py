from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import IntemCardapio
class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = True
        self._cardapio = []
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self) :
         return f'{self._nome} | {self._categoria} | {self.media_avaliacoes} |{self.ativo}' 
    
    @property
    def ativo(self):
        return '✅' if self._status else '❌'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f' {'Nome'.ljust (25)}  | {'Categoria'.ljust (25)} | {'Avaliações'.ljust (25)} | {'Status'.ljust (25)}')
        
        for restaurante in cls.restaurantes :
            print(f' {restaurante._nome.ljust(28)} {restaurante._categoria.ljust(28)} {str(restaurante.media_avaliacoes).ljust(28)} {restaurante.ativo.ljust (28)}')
        
        
    def alternar_status(self):
        self._status = not self._status
        
    def adicionar_cardapio(self,item):
        if isinstance(item, IntemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do {self._nome}\n')

        for cardapio,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{cardapio}. Nome: {item.nome } | {cardapio}. Descrição: {item.descricao} | Preço: {item.preco}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{cardapio}. Nome: {item.nome } | {cardapio}. Tamanho: {item.tamanho} | Preço: {item.preco}'
                print(mensagem_bebida)

    def receber_avaliacoes(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
    
    @property      
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        
        soma_de_notas = 0
        for avaliacoes in self._avaliacoes:
            soma_de_notas = soma_de_notas + avaliacoes.nota
        quantidade_de_notas = len(self._avaliacoes)
        media = round(soma_de_notas / quantidade_de_notas, 1)
        return media
    