print('-' * 27)
print('\033[7;0;40m Analisador de triangulos \033[m')
print('-'* 27)

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
print('-'* 27)
if n1 == n2 == n3:
    print('Esses segmentos pode formar um trinagulo EQUILÁTERO')
elif n1 == n2 or n2 == n1 or n1 == n3 or n3 == n2 and n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Esse segmentos pode se tonar um triangulo ISÓSCELES')

elif n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Esses segmentos pode formar um trinagulo ESCALENO')

else:
    print('Não pode se tonar trangulo')