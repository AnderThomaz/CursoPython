import random
n1 = input('Digite o primeiro nome')
n2 = input('Digite o Segundo nome')
n3 = input('Digite o Terceiro nome')
n4 = input('Digite o Quarto nome')
list = [n1, n2, n3, n4]

random.shuffle(list)

print('A Lista de aluno foi: ')
print(list)
