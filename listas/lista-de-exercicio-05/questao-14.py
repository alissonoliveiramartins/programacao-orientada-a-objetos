import random

matriz=[]
quadrado=[]
lista = ['']
 
 
while len(quadrado) < 9:
 
 numero=(random.randint(1,9))
 if numero not in quadrado:
   quadrado.append(numero)
matriz.append(quadrado[6:9])
matriz.append(quadrado[3:6])
matriz.append(quadrado[:3])
 
print(matriz)

#IMCOMPLETA
