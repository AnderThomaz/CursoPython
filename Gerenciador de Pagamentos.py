preco = float(input('Qual o valor do produto? '))

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
if pag == 1:
    valor = preco - (preco * 10 / 100)
    print('Total a pagar R${:.2f}'.format(valor))

elif pag == 2:
    valor = preco - (preco * 5 / 100)
    print('Total a pagar R${:.2f}'.format(valor))

elif pag == 3:
    valor = preco / 2
    print('Total a pagar 2x de R${:.2f}'.format(valor))

else:
    par = int(input('Quantas vezes? '))

if  par == 2:
    valor = preco / par
    print('Total a pagar sem juros é de {}x de R${:.2f}'.format(par, valor))

elif par == 1:
    valor = preco - (preco * 5 / 100)
    print('Total a pagar é de {}x de R${:.2f}'.format(par, valor))

else:
    valor = (preco + (preco * 20 /100)) / par
    print('Total a pagar é de {}x de R${:.2f}'.format(par,valor))