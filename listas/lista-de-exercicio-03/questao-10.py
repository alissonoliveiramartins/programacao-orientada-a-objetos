periodo= input('DIGITE M (Matutino), V (Vespertino) ou N (Noturno) : ')
if periodo.upper() == 'M':
    print('Bom Dia!')
elif periodo.upper() == 'V':
    print('Boa Tarde!')
elif periodo.upper() == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido')
