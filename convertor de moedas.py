valor = float(input('Quantos voce tem na sua carteira? '))

dolar = 4.91

conver = valor / dolar

print('Você consegue comprar com o R${} cerca de U${:.2f}.'.format(valor, conver))