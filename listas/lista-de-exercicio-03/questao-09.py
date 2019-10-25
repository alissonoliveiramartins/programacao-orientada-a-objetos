numero1= int(input())
numero2= int(input())
numero3= int(input())
if numero1 < numero2 < numero3:
    pri_numero = numero1
    seg_numero = numero2
    ter_numero = numero3
elif numero1 < numero3 < numero2:
    pri_numero = numero1
    seg_numero = numero3
    ter_numero = numero2
elif numero2 < numero1 < numero3:
    pri_numero = numero2
    seg_numero = numero1
    ter_numero = numero3
elif numero2 < numero3 < numero1:
    pri_numero = numero2
    seg_numero = numero3
    ter_numero = numero1
elif numero3 < numero1 < numero2:
    pri_numero = numero3
    seg_numero = numero1
    ter_numero = numero2
elif numero3 < numero2 < numero1:
    pri_numero = numero3
    seg_numero = numero2
    ter_numero = numero1
print(ter_numero)
print(seg_numero)
print(pri_numero)

