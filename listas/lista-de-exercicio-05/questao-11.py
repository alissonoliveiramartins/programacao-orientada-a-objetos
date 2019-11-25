
def mes_por_extenso(data):
    meses= ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Agosto','Novembro','Dezembro']
    dia, mes, ano= data.split('/')
    dia=int(dia)
    mes=int(mes)
     
    for x in range(1,12+1):
        if x == mes:
            mes = meses[x-1]
            
    if (mes == 'Janeiro' or mes == 'Março' or mes == 'Maio' or mes == 'Julho' or mes == 'Agosto' or mes == 'Dezembro') and 0 < dia <= 31:
        return('{} de {} de {}'.format(dia,mes,ano))
    elif (mes == 'Abril' or mes == 'Junho' or mes == 'Setembro' or mes == 'Novembro') and 0 < dia <= 30:
        return('{} de {} de {}'.format(dia,mes,ano))
     
    elif mes == 'Fevereiro' and (0 < dia <= 28):
        return('{} de {} de {}'.format(dia,mes,ano))
     
    elif mes == 'Fevereiro' and (0 < dia <= 29) and int(ano) % 4 == 0:
        return('{} de {} de {}'.format(dia,mes,ano))
    else:
        print('NULL')
        

