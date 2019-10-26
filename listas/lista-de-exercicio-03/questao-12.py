valor_por_hora = float(input('Valor por hora: '))
quantidade_de_hora = float(input('Quantidade de horas: '))
valor_ir= int(0)
salario = valor_por_hora * quantidade_de_hora
print('Salário Bruto ({} * {})     : R$ {:.2f}'.format(quantidade_de_hora,valor_por_hora,salario))

if salario <= 900:
    print('IR Isento')
elif 900 < salario <= 1500:
    print('(-) IR (5%)                     : R$ {:.2f}'.format(salario * 0.05))
    valor_ir = 5
elif 1500 < salario <= 2500:
    print('(-) IR (10%)                    : R$ {:.2f}'.format(salario * 0.1))
    valor_ir = 10
elif 2500 < salario :
    print('(-) IR (20%)                    : R$ {:.2f}'.format(salario * 0.2))
    valor_ir = 20
 
print('(-) INSS ( 10%)                 : R$ {:.2f}'.format(salario * 0.1))
print('FGTS (11%)                      : R$ {:.2f}'.format(salario * 0.11))
print('Total de descontos              : R$ {:.2f}'.format(salario * ((valor_ir/100) + 0.1  )))
print('Salário Liquido                 : R$ {:.2f}'.format(salario- salario * ((valor_ir/100) + 0.1  )))
