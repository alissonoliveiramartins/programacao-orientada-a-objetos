salario=float(input())
novo_salario= 0
porcentagem =(' ')
if salario <= 280 :
    novo_salario = salario + salario * 0.2
    porcentagem =('20%') 
elif 280 < salario <= 700:
    novo_salario = salario + salario * 0.15
    porcentagem =('15%')
elif 700 < salario <= 1500:
    novo_salario = salario + salario * 0.10
    porcentagem =('10%')
elif 1500 < salario:
    novo_salario = salario + salario * 0.05
    porcentagem =('5%')
print('Salário antes do reajuste {:.2f}'.format(salario))
print('Percentual de aumento aplicado {}'.format(porcentagem))
print('Valor do aumento {}'.format(novo_salario - salario))
print('Novo salário {}'.format(novo_salario))

    
    
    
