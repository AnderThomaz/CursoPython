n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print('O primeiro numero é maior'.format(n1))

elif n2 == n1:
    print('Os valores são iguais')

else:
    print('O segundo numero é maior'.format(n2))