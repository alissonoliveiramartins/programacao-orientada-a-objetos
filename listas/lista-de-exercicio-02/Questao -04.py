notas = input('Digite suas notas separadas por espaço : ').split()
soma= 0
media= 0
for i in notas:
	i = int(i)
	soma += i
print('Sua media é : ',soma/4)
