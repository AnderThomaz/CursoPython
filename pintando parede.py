largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))

area = largura * altura

tinta = float (area / 2 )

print('Sua Parede tem as dimensões de {:.2f}x{:.2f} e sua area e de {:.3f}m².'.format(largura,altura,area))
print('Para pintar toda a parede vc precisara de {}'.format(tinta))