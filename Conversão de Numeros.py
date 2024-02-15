print('Base de conversão')
print('---' * 7)
num = int(input('Digite um numero: '))

print('Agora, escolha qual a base de conversão')
print('Digite 1 para Binário')
print('Digite 2 para Octal')
print('Digite 3 para Hexadecimal')

base = int(input('Qual A Base? '))

if base == 1:
    print('{} convertido em BINARIO é igual a {}'.format(num, bin(num)[2:]))

elif base == 2:
    print('{} convertido em OCTAL é igual a {}'.format(num, oct(num)[2:]))

elif base == 3:
    print('{} convetido em HEXADECIMAL é igual a {}'. format(num, hex(num)[2:]))

else:
    print('Opcão invalida')
