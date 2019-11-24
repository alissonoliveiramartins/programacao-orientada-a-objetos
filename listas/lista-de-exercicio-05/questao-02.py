lista=[1,] 
numero = int(input())
print(' '.join(map(str, lista)))
for numeros in range(2,numero+1):
	lista.append(numeros)
	print(' '.join(map(str, lista)))

