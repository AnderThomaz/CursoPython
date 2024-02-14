valor = float(input('Qual o preço do produto? '))

desconto = valor * 10/100
promo = valor - desconto

print('O produto na promoção de 10% de desconto esta no valor de R${:.2f}'.format(promo))

salario = float(input('Qual o Salario do funcionario? '))

aumento = salario * 10/100
sal = salario + aumento

print('O salario do funcionario de R${:.2f} com aumento de 10% teve aumento para R${:.2f}'.format(salario,sal))


