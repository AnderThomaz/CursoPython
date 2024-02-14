text = str(input('Digite um texto... ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(text.count('A')))
print('A primeira letra A apareceu na posição {}'.format(text.find('A') +1))
print('A ultima letra A apareceu na posição {}'.format(text.rfind('A') +1))