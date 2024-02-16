from datetime import date

dts = int(input('Ano de nascimento: '))
ano = date.today().year

idade = ano - dts

if dts > ano:
    print('Dana de nascimento invalida')

elif idade <= 9:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: MIRIM')

elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: INFANTIL')


elif idade > 14  and idade <= 19:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: JÚNIOR')

elif idade > 19  and idade <= 25:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: SÊNIOR')

else:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: MASTER')

