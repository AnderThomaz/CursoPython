
print('-' * 27)
print('\033[7;0;40m Analisador de triangulos \033[m')
print('-'* 27)

r1 = float(input('Primeiro seguimento '))
r2 = float(input('Segundo seguimento '))
r3 = float(input('Terceiro seguimento '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses seguimentos poder ser triangulos')
else:
    print('Não pode se tonar trangulo')