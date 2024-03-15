print('-' * 34)

print('\033[1;20;40m Calculo de Financiamento \033[m')
print('-' * 34)

valorCasa = float(input('Qual o valor do finaciamento? '))
print('-' * 34)

print('\033[1;20;40m Certo, Agora por favor informe o valor do seu salario \033[m')
print('-' * 34)

salario = float(input('Qual o seu salario? '))
print('-' * 34)

print('\033[1;20;40m Em Quantas parcelas voce deseja pagar? MAXIMO 480vezes \033[m')

parcelas = int(input('Numeros de parcelas '))
print('-' * 34)


Nparcerlas = valorCasa / parcelas
FraSalario = salario * 30/100

if parcelas > 480:
    print('Numeros de Parcelas Muito Alto')

elif FraSalario >= Nparcerlas and parcelas > 5 < 480:
    print('Seu Financimento foi APROVADO! Parabens')
    print('Valor da Parcela sera de R${:.2f} de {}vezes'.format(Nparcerlas, parcelas))

elif FraSalario <= Nparcerlas and parcelas < 480:
    print('O Seu financimento foi REPROVADO! Aumente o valor de parcelas')
    print('O valor da Parcela é de R${:.2f}, e ultrapassa os 30% R${:.2f} do seu salario'.format(Nparcerlas, FraSalario))

else:
    print('Seu Financimento foi Reprovado!')
    print('O valor da Parcela é de R${:.2f}, e ultrapassa os 30% R${:.2f} do seu salario'.format(Nparcerlas, FraSalario))
