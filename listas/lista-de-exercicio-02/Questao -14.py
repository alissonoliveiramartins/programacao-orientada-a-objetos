ganho_por_hora= float(input('Quanto voce ganha por hora : '))
horas_trabalhada = float(input('Quantas horas voce trabalhou : '))
salario_bruto = ganho_por_hora * horas_trabalhada
print('+ Salário Bruto :{} R$'.format(salario_bruto))
print('- IR (11%) : {} R$'.format(salario_bruto * 0.11))
print('- INSS (8%) : {} R$'.format(salario_bruto * 0.08))
print('- Sindicato ( 5%) : {} R$'.format(salario_bruto * 0.05))
print('= Salário Liquido : {} R$'.format(salario_bruto - (100 * 0.24)))
