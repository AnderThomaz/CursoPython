num = int(input('Digital um numero para ver sua tabuada: '))

for c in range(1,150):
    print('{} X {:2} = {}'.format(num,c,num*c))

