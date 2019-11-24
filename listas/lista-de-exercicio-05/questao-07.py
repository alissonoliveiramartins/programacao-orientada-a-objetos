def valor_pagamento(valor, dias):
 multa= ((3 * valor) / 100) * dias
 juros= ((0.1 * valor) / 100) * dias
 valor_a_pagar = valor + multa + juros
 return valor_a_pagar
 
quantidade = 0
valor_total= 0
valor = 1
 
while valor > 0:
 
 valor = int(input('DIGITE O VALOR DA PRESTAÇÃ0 : '))
 if valor == 0:
   break
 dias = int(input('DIGITE NUMEROS DE DIAS EM ATRASO :  '))
 
 print('VALOR A PAGAR: {:.2f}'.format(valor_pagamento(valor,dias)))
 valor_total += valor_pagamento(valor,dias)
 quantidade += 1

print(' ') 
print('VALOR TOTAL = {:.2f}'.format(valor_total))
print('QUANTIDADES DE PRESTAÇÃO PAGA = {}'.format(quantidade))
