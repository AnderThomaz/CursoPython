print('-' * 25)
print('  Progressão Aritmetica')
print('-' * 25)

num = int(input('Digite o primeiro numero: '))
razao = int(input('Razão: '))
decimo = num + (10) * razao
for c in range(num, decimo, razao):
    print('',format(c), end=' > ')
print('Acabou')

