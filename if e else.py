tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=5:
    print('Carro novo')
else:
    print('Carro velho')
print('Fim')

print('carro novo' if tempo<=5 else 'carro velho')


