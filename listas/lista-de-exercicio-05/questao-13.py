def desenho_retangulo(linha, coluna):
 while linha > 20 :
   linha -= 1
 while coluna > 20:
   coluna -= 1
 print('+',coluna*'-','+')
 while linha > 0:
   linha-= 1
   print('|',coluna*' ','|')
 print('+',coluna*'-','+')

desenho_retangulo(3,4)

