altura=float(input('DIGITE SUA ALTURA: '))
sexo= input('DIGITE O SEU SEXO: ')
peso_ideal = 0
if sexo.lower() == 'masculino' :
	peso_ideal = (72.7 * altura - 58)
elif sexo.lower() == 'feminino' :
	peso_ideal = (62.1 * altura - 44.7)
print('Seu peso Ideal é ',peso_ideal)

