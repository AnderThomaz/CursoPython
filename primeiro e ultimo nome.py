

nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print('Muito Prazer te conhcer!')
print('Seu primeiro numero é {}'.format(nome[0]))
print('Seu ultimo nome é {}'. format(nome[len(nome)-1]))