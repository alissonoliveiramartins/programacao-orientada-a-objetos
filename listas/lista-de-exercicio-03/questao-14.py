nota1 = float(input('PRIMEIRA NOTA : '))
nota2 = float(input('SEGUNDA NOTA: '))
media = (nota1+nota2)/2
conceito= ' '
if 9 <= media <= 10:
    conceito = 'A'
elif 7.5 <= media < 9:
    conceito = 'B'
elif 6 <= media < 7.5:
    conceito = 'C'
elif 4 <= media < 6:
    conceito = 'D'
elif 0 <= media < 4:
    conceito = 'E'
print('Suas Notas foram: {} e {}'.format(nota1,nota2))
print('Sua Media foi: {}'.format(media))
print('O seu Conceito foi : {}'.format(conceito))
if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print('APROVADO')
else:
    print('REPROVADO')
    
