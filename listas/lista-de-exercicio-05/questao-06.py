def converso_de_hora(hora_completa):
 hora, minuto= hora_completa.split(':')
 hora =int(hora)
 if (hora) > 12:
   hora -= 12
 return ('{}:{}'.format(hora,minuto))
 
def saida(hora_completa):
 hora, minuto= hora_completa.split(':')
 hora =int(hora)
 if hora > 12:
   return 'P.M.'
 elif hora <= 12:
   return 'A.M.'
 
resposta = 1
 
while resposta == 1:
 hora_completa = input('DIGITE A HORA A SER CONVERTIDA: ')
 
 print('HORA CONVERTIDA :',converso_de_hora(hora_completa),saida(hora_completa))
 
 resposta= int(input('DESEJA REALIZAR O POGRAMA NOVAMENTE ? \nSIM(1) NÃO(2)\n'))
