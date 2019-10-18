peso= float(input('Digite o peso do peixe : '))
excesso = 0
multa = 0
if peso > 50:
    multa= (peso - 50 ) * 4
    excesso= peso - 50
    print('O excesso do peso é {}Kg'.format(excesso))
    print('A multa é : {}R$'.format(multa))
else:
    print('Não teve excesso de peso')
          
