cont = 3
menor = 0
while cont > 0:
    cont -= 1
    numero= float(input())
    if menor == 0:
        menor = numero
    elif numero < menor:
        menor = numero
print('O produto a ser comprado é o de valor: {:.2f}R$'.format(menor))
