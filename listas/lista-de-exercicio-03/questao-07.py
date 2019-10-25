cont=3
maior= 0
menor= 0
while cont > 0:
    cont -= 1
    numero= int(input())
    if numero > maior:
        maior = numero
    else:
        menor = numero
print('O maior entre eles é o numero: ',maior)
print('O menor entre eles é o numero: ',menor)
