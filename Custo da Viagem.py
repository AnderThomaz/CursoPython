distancia = int (input('Qual a distancia da viagem? '))
if distancia <= 200:
    valor = distancia * 0.50
    print('O valor da viagem de {}km é de R${:.2f}'.format(distancia, valor))
else:
    valor = distancia * 0.45
    print('O valor da viagem de {}km é de R${:.2f}'.format(distancia, valor))