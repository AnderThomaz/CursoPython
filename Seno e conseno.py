import math
angulo = float (input('Didite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))

print('O angulo de {} tem um Seno de {}'. format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print(('O Angulo do {} tem o coseno de {:.2f}'.format(angulo, cosseno)))

tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o tangente de {}'.format(angulo, tangente))