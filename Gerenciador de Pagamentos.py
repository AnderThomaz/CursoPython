print('=' * 10, end='')

print(' Loja Thomaz ', end='')
print('=' * 10)

preco = float(input('Qual o valor do produto? R$ '))

print('R$ {:.2f}'.format(preco))

print('')
print('Qual a forma de pagamento?')

print('[ 1 ] à vista 10% de desconto')
print('[ 2 ] à vista no cartão 5% de desconto')
print('[ 3 ] em até 2x no cartão sem juros')
print('[ 4 ] em 3x ou mas no cartão com 20% de juros')
print('')
pag = int(input('Selecione a forma de pagamento? '))
print('')
if pag == 0 or pag > 4:
    print('valor invalido, tente novamente!')

elif pag == 1:
    valor = preco - (preco * 10 / 100)
    print('Total a pagar R${:.2f}'.format(valor))

elif pag == 2:
    valor = preco - (preco * 5 / 100)
    print('Total a pagar R${:.2f}'.format(valor))

elif pag == 3:
    valor = preco / 2
    print('Total a pagar 2x de R${:.2f}'.format(valor))

else:
    parcerlas = int(input('Quantas vezes? '))
    valor = (preco + preco * 20 / 100) / parcerlas
    print('')
    print('Total a pagar é de {}x de {:.2f}'.format(parcerlas, valor))
    print('Valor a vista R${:.2f}'.format(preco))
    print('Valor a total com juros R${:.2f}'.format((valor * parcerlas)))