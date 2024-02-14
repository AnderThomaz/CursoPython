nome = str(input('Qual é seu nome ')).strip()
if nome == 'Gustavo':
    print('Quem nome lindo vc tem!')
else:
    print('Seu nome e bem comum!')
print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primera nota '))
n2 = float(input('Digite a segunda nota'))

media = (n1+n2)/2

print('Sua nota foi {:.2F}'.format(media))
if media <= 5:
    print('voce foi reprovado na materia')
else:
    print('Voce passou na materia. parabens!')