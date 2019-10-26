numero_dia= int(input())
numero_dia -= 1
dias =['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado']
if 0 <= numero_dia <= 6: 
    print(dias[numero_dia])
else:
    print('Valor Invalido')
