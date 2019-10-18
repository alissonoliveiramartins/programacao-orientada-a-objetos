ganho_por_hora= float(input('Quanto voce ganha por hora : '))
horas_trabalhada = float(input('Quantas horas voce trabalhou : '))
salario_bruto = ganho_por_hora * horas_trabalhada
print('+ Salário Bruto :{:.2f} R$'.format(salario_bruto))
print('- IR (11%) : {:.2f} R$'.format(salario_bruto * 0.11))
print('- INSS (8%) : {:.2f} R$'.format(salario_bruto * 0.08))
print('- Sindicato ( 5%) : {:.2f} R$'.format(salario_bruto * 0.05))
print('= Salário Liquido : {:.2f} R$'.format(salario_bruto - (salario_bruto * 0.24)))
