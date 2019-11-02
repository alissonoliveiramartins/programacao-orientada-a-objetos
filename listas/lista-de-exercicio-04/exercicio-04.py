with open("amazon.csv") as arquivo:
	
	ano = 0
	cidade= ' '
	mes = ' '
	casos= 0
	data = 0
	item_a = 0
	item_b = 0
	item_c = 0
	item_d = 0

	for linha in arquivo:
		linha = linha.strip(' ')
		ano, cidade, mes, casos, data = linha.split(',')
		casos= casos.replace(".", "")
		#Item A
		if '"Acre"' == cidade and ano == '2015':
			item_a += int(casos)

		#Item B
		elif '"Ceara"' == cidade and ano == '2014':
			item_b += int(casos)

		#Item C
		elif '"Amazonas"' == cidade:
			item_c += int(casos)

		#Item D
		if ano == '"year"':
			continue

		elif int(ano) >= 2010 and cidade == '"Mato Grosso"':
			item_d += int(casos)

	print('Resposta item A : {}'.format(item_a))
	print('Resposta item B : {}'.format(item_b))
	print('Resposta item C : {}'.format(item_c))
	print('Resposta item D : {}'.format(item_d))

if arquivo.closed:
	print('ARQUIVO FECHADO')