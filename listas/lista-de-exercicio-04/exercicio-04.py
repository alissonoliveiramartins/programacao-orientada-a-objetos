with open("amazon.csv") as arquivo:
	
	item_a = 0
	item_b = 0
	item_c = 0
	item_d = 0
	todos_estados = set()

	for linha in arquivo:
		linha = linha.strip(' ')
		ano, estado, mes, casos, data = linha.split(',')
		casos= casos.replace(".", "")
		estado= estado.replace('"','')
		#Item A
		if 'Acre' == estado and ano == '2015':
			item_a += int(casos)

		#Item B
		elif 'Ceara' == estado and ano == '2014':
			item_b += int(casos)

		#Item C
		elif 'Amazonas' == estado:
			item_c += int(casos)

		#Item D
		if ano == '"year"':
			continue

		elif int(ano) >= 2010 and estado == 'Mato Grosso':
			item_d += int(casos)

		#PERGUNTA ADICIONAL	
		todos_estados.add(estado)
		
        #Respostas 
	print('Resposta item A : {}'.format(item_a))
	print('Resposta item B : {}'.format(item_b))
	print('Resposta item C : {}'.format(item_c))
	print('Resposta item D : {}'.format(item_d))
	print('\nPERGUNTA ADICIONAL:')

        #Pergunta Adicional - Quantos estados participaram da pesquisa? E quais foram eles ?
	
	print('Foram {} Estados.\nSão eles : {}.'.format(len(todos_estados),', '.join(map(str, todos_estados))))
	
#if arquivo.closed:
#	print('ARQUIVO FECHADO')
