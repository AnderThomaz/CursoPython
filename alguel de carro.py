d = int(input('Quantos os dias vc alugou com carro?'))
km = float(input('Quantos Km você Percorreu?'))

valorkm = 0.15 * km
valordia = 60 * d

total = valorkm + valordia

print('Total a pagar R${:.2f} '.format(total))