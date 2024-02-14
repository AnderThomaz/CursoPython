salario = int(input('Salario do funcionario '))

if salario < 1250:
    aumento = salario + (salario * 15 /100)
    print('Salario de R${:.2f} com aumento de 15% agora é R${:.2f}'.format(salario, aumento))

else:
    aumento = salario + (salario * 10 /100)
    print('Salario de R${:.2f} com aumento de 10% agora é R${:.2f}'.format(salario, aumento))
