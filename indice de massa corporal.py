peso = float(input('Qual é seu peso? KG '))
altura = float(input('Qual sua altura? CM '))

imc = peso / (altura ** 2)

print('Pontuação {:.2f}'.format(imc))

if imc <= 18.5:
    print('Você esta abaixo do Peso')

elif imc > 18.5 and imc <= 25:
    print('Você esta no peso Ideal')

elif imc > 25 and imc <=30:
    print('Você esta em sobrepeso')

elif imc > 30 and imc <=40:
    print('Você esta com Obesidade')

else:
    print('Você esta com obesidade mórbida, Cuidado!')