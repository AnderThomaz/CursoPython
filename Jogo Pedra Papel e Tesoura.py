from random import randint
from time import sleep

print('=-=-=-=-=- Jo Ken Po -=-=-=-=-=-=')

print('''
[2] Pedra
[1] Papel
[0] Tesoura
''')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('-='*17)

player = int(input('Qual é a sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-='*17)
print('O Computador jogou {}'.format(itens[computador]))
print('O Você jogou {}'.format(itens[player]))

if computador == 0:
    if player == 0:
        print('Empate')
    elif player == 1:
        print('Você ganhou!')
    elif player == 2:
        print('O computador ganhou!')
    else:
        print('Jogada invalida!')

elif computador == 1:
    if player == 0:
        print('O computador ganhou!')
    elif player == 1:
        print('Empate')
    elif player == 2:
        print('Você ganhou!')
    else:
        print('Jogada invalida!')

elif computador == 2:
    if player == 0:
        print('Você ganhou!')
    elif player == 1:
        print('O computador ganhou!')
    elif player == 2:
        print('Empate')
    else:
        print('Jogada invalida!')