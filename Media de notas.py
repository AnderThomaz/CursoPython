n1 = float(input('primiera nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))

media = float (n1+n2+n3) / 3
print('Sua nota é {:.1f}'.format(media))

if media < 5.0:
    print('Voce foi reprovado')

elif media >= 5.0 < 6.9:
    print('Voê esta de recuperação')

else:
    print('Aprovado')