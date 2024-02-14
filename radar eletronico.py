velocidade = int(input('Qual a velocidade atual do carro? '))
limite = 80
print('Velocidade {}km/h'.format(velocidade))
if velocidade <= limite:
    print('Sempre dirija com segurança. boa viagem!')
else:
    print('MULTADO! Você excedeu o limita permitido que de 80km/h')
    multa = (velocidade - limite) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
    print('Sempre dirija com segurança. boa viagem!')

