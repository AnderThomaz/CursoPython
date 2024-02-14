from random import randint
from time import sleep

computador = randint(0,5) #valor sorteador
print('-' * 60)
print('Vou pensar em um numero de 0 e 5, Tenta adivinhar...')
print('-' * 60)
jogador = int(input('Em qual numero eu pensei? '))#valor que jogar acha que é
print('Processando...')
sleep(3)

if jogador == computador:
    print('Parabens, você consegiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e não no {}'.format(computador, jogador))


