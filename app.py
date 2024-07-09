from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_l = Restaurante('LaCasita', 'Humburgueria')

# restaurante_l.receber_avaliacoes('Marcos', 5)
# restaurante_l.receber_avaliacoes('Bruno', 4)

# Restaurante.listar_restaurantes()

suco = Bebida('Suco de uva', '500ml', 8.0)
humburguer  = Prato('BigArte', 'Picanha', 32.0)

suco.desconto()
humburguer.desconto()

restaurante_l.adicionar_cardapio(suco)
restaurante_l.adicionar_cardapio(humburguer)


print('  Cadapio do LaCasita')
restaurante_l.exibir_cardapio
