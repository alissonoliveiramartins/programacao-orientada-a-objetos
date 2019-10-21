quantidade_de_notas = int(input('Quantas notas serão calculadas ? '))
soma_das_notas = 0
for notas in range(0,quantidade_de_notas):
    nota_obitidas = int(input('DIGITE SUA {}ª NOTA : '.format(notas+1)))
    soma_das_notas += nota_obitidas
media = soma_das_notas / quantidade_de_notas
if media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
elif media == 10:
    print('Aprovado com Distinção')
