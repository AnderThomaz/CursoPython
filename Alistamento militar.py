from datetime import date

ano = date.today().year

dtns = int(input('Ano de Nascimento: '))
idade = ano - dtns

if dtns > ano:
    print('Data de nascimento invalida!')

elif idade < 17:
    resIdade = 17 - idade
    anoAli = resIdade + ano
    print('Voce tem {} anos. '.format(idade))
    print('O ano de seu alistamento sera em {}'.format(anoAli))

elif idade == 17:
    print('Procure um serviço militar mas proximos de voce, para se alistar.')

elif idade == 18:
    print('Procure um serviço militar URGENTE para se alistar')

else:
    resIdade = idade - 18
    anoAli = resIdade - ano
    print('Voce ja tem {} anos, esta atrasado {} anos.'.format(idade,resIdade))
    print('Seu ano de alistamento era em {}'.format(abs(anoAli)))
    print('Corra para regularizar seu alistamento')
