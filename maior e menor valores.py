a = int(input('primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O menor valor foi {}'.format(menor))

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior valor foi {}'.format(maior))
